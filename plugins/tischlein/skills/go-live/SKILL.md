---
name: go-live
description: 'Take a finished tischlein website live: final readiness check, set the website live, connect the own domain, switch DNS, verify SSL and every redirect, compare PageSpeed and review 404s after launch. Use for "Website live schalten", "Domain verbinden", "DNS umstellen", "eigene Domain", "Seite veröffentlichen", "go live", "connect my domain" or "launch the website".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "go-live"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.

Helper scripts ship with this skill in `scripts/` (Python 3, standard library only; run with `--help` for usage): `scripts/verify-redirects.py`. The guidance says when to use them.
