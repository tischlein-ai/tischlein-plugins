---
name: onboard-restaurant
description: 'Set up a new venue in Tischlein: organization settings, contact details, opening hours, locations, languages, team members and a first website. Use for "Restaurant einrichten", "neues Lokal anlegen", "Tischlein einrichten", "Öffnungszeiten hinterlegen", "Team einladen", "set up my restaurant" or "get started with Tischlein".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "onboard-restaurant"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
