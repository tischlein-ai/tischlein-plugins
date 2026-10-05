---
name: migrate-website
description: 'Migrate an existing restaurant, café or bar website to Tischlein: analyse the old site, choose a 1:1 migration or a redesign, build the theme, import pages and menus, plan redirects and hand over to go-live for the domain switch. Use for "Website umziehen", "Website migrieren", "bestehende Seite übernehmen", "von WordPress/Wix zu Tischlein", "migrate my website" or "move our site to Tischlein".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "migrate-website"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.

Helper scripts ship with this skill in `scripts/` (Python 3, standard library only; run with `--help` for usage): `scripts/crawl-site.py`. The guidance says when to use them.
