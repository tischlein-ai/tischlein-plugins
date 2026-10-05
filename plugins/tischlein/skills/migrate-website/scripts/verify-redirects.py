#!/usr/bin/env python3
"""Verify the redirects of a migrated website after the DNS cutover.

Usage:
    python3 verify-redirects.py redirects.csv [--base https://www.new-domain.de] [--json report.json]
        [--org <slug>] [--insecure | --cafile ca.pem]

The mapping is a CSV with the columns old,new (a header row is optional) or JSON: either
[{"old": "...", "new": "..."}] or {"old": "new"}. Relative URLs ("/speisekarte.html") are resolved
against --base. Targets written like import-redirects ("page:<id>", "media:<id>") are resolved with the
tischlein CLI (`tischlein get page <id> --json`, logged in; --org picks the organization, --locale the language of
page paths, default de = no prefix).

TLS: local Herd sites (*.test) use a CA that Python 3.13 rejects ("Missing Authority Key Identifier", strict X.509
checks). --cafile <ca.pem> trusts that CA without the strict flag; --insecure skips certificate checks entirely
(local checks only). SSL and network errors are printed with their reason.

For every old URL the check expects exactly ONE 301 redirect (max one hop) straight to the mapped target,
and the target must answer 200. An old URL equal to its target must answer 200 itself. Reported problems:
WRONG_STATUS (e.g. 302 instead of 301), WRONG_TARGET, CHAIN (more than one hop), LOOP, TARGET_NOT_200,
NOT_REDIRECTED, ERROR (network). Exit code 1 when anything failed. Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

USER_AGENT = "TischleinRedirectCheck/1.0 (+https://tischlein.ai)"
MAX_HOPS = 10
DEFAULT_PORTS = {"http": 80, "https": 443}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401 - urllib hook
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def configure_tls(insecure: bool, cafile: str | None) -> None:
    """Install the opener with the requested TLS context (default: system trust store, full verification)."""
    global OPENER
    if not insecure and not cafile:
        return
    if insecure:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
    else:
        context = ssl.create_default_context(cafile=cafile)
    # Python 3.13 enables VERIFY_X509_STRICT, which rejects local CAs such as Herd's (no Authority Key Identifier).
    if hasattr(ssl, "VERIFY_X509_STRICT"):
        context.verify_flags &= ~ssl.VERIFY_X509_STRICT
    OPENER = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=context))


def error_reason(error: BaseException) -> str:
    """A readable reason, never \"None\": SSL verification details, socket errors, timeouts."""
    reason = getattr(error, "reason", None)
    if isinstance(reason, ssl.SSLCertVerificationError):
        return f"SSL: {reason.verify_message or reason} (local CA? use --cafile <ca.pem> or --insecure)"
    if isinstance(reason, BaseException):
        return f"{type(reason).__name__}: {reason}"
    if reason:
        return str(reason)
    return f"{type(error).__name__}: {error}" if str(error) else type(error).__name__


def resolve_reference(target: str, base: str | None, org: str | None, locale: str) -> str:
    """page:<id> / media:<id> (import-redirects notation) → absolute URL via the tischlein CLI."""
    kind, _, record_id = target.partition(":")
    cli = shutil.which("tischlein")
    if not cli:
        raise SystemExit(f"{target} needs the tischlein CLI on PATH (logged in) to look up its URL, or write the URL instead.")
    command = [cli, "get", kind, record_id, "--json", "--no-interaction"] + (["--org", org] if org else [])
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"Could not look up {target}: {(completed.stderr or completed.stdout).strip()[:300]}")
    record = payload.get("data", payload) if isinstance(payload, dict) else {}
    if kind == "media":
        url = record.get("public_url") or record.get("url")
        if not url:
            raise SystemExit(f"{target} has no public URL.")
        return url if urlsplit(url).scheme else urljoin((base or "").rstrip("/") + "/", url.lstrip("/"))
    paths = record.get("path_map") or {}
    if locale not in paths:
        raise SystemExit(f"{target} has no {locale} address (path_map: {paths}).")
    if not base:
        raise SystemExit(f"{target} needs --base https://new-domain")
    path = paths[locale]
    prefix = "" if locale == "de" else f"/{locale}"
    return base.rstrip("/") + (prefix + ("/" + path if path else "") or "/")


def canonical(url: str) -> str:
    """Comparable form: lowercase scheme/host, no default port, "/" for an empty path, no fragment."""
    parts = urlsplit(url.strip())
    host = (parts.hostname or "").lower()
    port = f":{parts.port}" if parts.port and parts.port != DEFAULT_PORTS.get(parts.scheme.lower()) else ""
    return urlunsplit((parts.scheme.lower(), host + port, parts.path or "/", parts.query, ""))


def load_mapping(path: str, base: str | None, org: str | None = None, locale: str = "de") -> list[tuple[str, str]]:
    text = Path(path).read_text(encoding="utf-8-sig")
    pairs: list[tuple[str, str]] = []
    if path.lower().endswith(".json"):
        data = json.loads(text)
        items = data.items() if isinstance(data, dict) else ((row["old"], row["new"]) for row in data)
        pairs = [(str(old), str(new)) for old, new in items]
    else:
        for row in csv.reader(text.splitlines()):
            if len(row) < 2 or not row[0].strip() or row[0].strip().startswith("#"):
                continue
            if row[0].strip().lower() in ("old", "from", "source", "alt") and not pairs:
                continue
            pairs.append((row[0].strip(), row[1].strip()))

    def resolve(url: str) -> str:
        if url.split(":", 1)[0] in ("page", "media") and url.split(":", 1)[1].isdigit():
            return resolve_reference(url, base, org, locale)
        if urlsplit(url).scheme:
            return url
        if not base:
            raise SystemExit(f"Relative URL {url!r} needs --base https://new-domain")
        return urljoin(base.rstrip("/") + "/", url.lstrip("/"))

    return [(resolve(old), resolve(new)) for old, new in pairs]


def request(url: str, timeout: float) -> tuple[int, str]:
    """Status and absolute Location (may be "") of one request without following redirects."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with OPENER.open(req, timeout=timeout) as response:
            return response.status, ""
    except urllib.error.HTTPError as error:
        location = error.headers.get("Location", "") if error.headers else ""
        return error.code, urljoin(url, location) if location else ""


def check(old: str, new: str, timeout: float = 15.0) -> dict:
    result = {"old": old, "expected": new, "status": None, "location": "", "hops": [], "target_status": None, "problem": ""}
    try:
        chain: list[tuple[str, int]] = []
        url = old
        seen = set()
        while True:
            status, location = request(url, timeout)
            chain.append((url, status))
            if status not in (301, 302, 303, 307, 308) or not location:
                break
            if canonical(location) in seen or canonical(location) == canonical(url) or len(chain) > MAX_HOPS:
                chain.append((location, -1))
                result["hops"] = [hop for hop, _ in chain]
                result["status"] = chain[0][1]
                result["problem"] = "LOOP"
                return result
            seen.add(canonical(url))
            url = location
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        result["problem"] = "ERROR"
        result["error"] = error_reason(error)
        return result

    redirects = chain[:-1]
    final_url, final_status = chain[-1]
    result["status"] = chain[0][1]
    result["location"] = chain[1][0] if len(chain) > 1 else ""
    result["hops"] = [hop for hop, _ in redirects]
    result["target_status"] = final_status

    if canonical(old) == canonical(new):
        result["problem"] = "" if not redirects and final_status == 200 else ("TARGET_NOT_200" if not redirects else "CHAIN")
    elif not redirects:
        result["problem"] = "NOT_REDIRECTED"
    elif redirects[0][1] != 301:
        result["problem"] = "WRONG_STATUS"
    elif len(redirects) > 1:
        result["problem"] = "CHAIN"
    elif canonical(final_url) != canonical(new):
        result["problem"] = "WRONG_TARGET"
    elif final_status != 200:
        result["problem"] = "TARGET_NOT_200"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check that every old URL 301-redirects in one hop to its mapped target (200).")
    parser.add_argument("mapping", help="CSV (old,new) or JSON mapping")
    parser.add_argument("--base", help="New site base URL for relative paths, e.g. https://www.new-domain.de")
    parser.add_argument("--json", dest="json_out", help="Write the full report as JSON")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--org", help="Organization slug for page:<id>/media:<id> lookups with the tischlein CLI")
    parser.add_argument("--locale", default="de", help="Language of page:<id> paths (default de, no prefix)")
    tls = parser.add_mutually_exclusive_group()
    tls.add_argument("--insecure", action="store_true", help="Skip TLS certificate checks (local Herd sites only)")
    tls.add_argument("--cafile", help="Trust this CA bundle (e.g. Herd's CA) without Python 3.13's strict X.509 checks")
    args = parser.parse_args(argv)
    configure_tls(args.insecure, args.cafile)

    results = [check(old, new, args.timeout) for old, new in load_mapping(args.mapping, args.base, args.org, args.locale)]
    failures = [result for result in results if result["problem"]]

    for result in results:
        label = result["problem"] or "OK"
        detail = f" → {result['location']}" if result["location"] else ""
        extra = f" (expected {result['expected']}, target {result['target_status']})" if result["problem"] else ""
        if result.get("error"):
            extra = f" — {result['error']}"
        status = result['status'] if result['status'] is not None else '---'
        print(f"{label:15} {status} {result['old']}{detail}{extra}")

    print(f"\n{len(results) - len(failures)}/{len(results)} redirects OK, {len(failures)} failed.")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps({"results": results}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
