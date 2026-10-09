---
name: migrate-website
description: 'tischlein team only (platform admins): build a venue''s website or move its existing restaurant, café or bar website to tischlein from the venue''s request: analyse the old site, choose a 1:1 move or a redesign, build the theme, import pages and menus, plan redirects and hand over to go-live. Venue users who want a website built or moved: request-website. Use for "Website-Anfrage umsetzen", "Umzug für <Betrieb> bauen", "build the requested website" or "run the migration".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "migrate-website"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.

Helper scripts ship with this skill in `scripts/` (Python 3, standard library only; run with `--help` for usage): `scripts/crawl-site.py`. The guidance says when to use them.
