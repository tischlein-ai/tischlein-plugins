---
name: audit-allergens
description: 'Audit dishes for missing or inconsistent allergen and additive labelling (the 14 EU allergens, LMIV) and propose corrections for review. Use for "Allergene prüfen", "Allergenkennzeichnung", "Zusatzstoffe prüfen", "LMIV-Check", "fehlen Allergene", "audit allergens" or "check allergen labels".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "audit-allergens"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
