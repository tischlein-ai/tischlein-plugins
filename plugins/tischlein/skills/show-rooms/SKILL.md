---
name: show-rooms
description: 'Show rooms on a hotel or inn website: room categories with photos, amenities and prices per date (seasons, weekdays, day rates, CSV rate sheet), extras, arrangements, a Zimmer page. Use for "Zimmer anlegen", "Zimmerpreise", "Saisonpreise", "Arrangement", "Pauschale", "show rooms", "hotel rooms", "room prices".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "show-rooms"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
