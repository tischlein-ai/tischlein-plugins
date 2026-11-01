---
name: table-plan
description: 'Set up and run Reservierungen & Tischplan: build the floor plan from a description, table list (CSV), room scan, photo, sketch, screenshot, walls, doors, counter and table kinds, reservations from OpenTable, resmio or Quandoo, booking rules, activate table booking, block tables, rooms, seasonal layouts, why a time is full. Use for "Tischplan einrichten", "Tischplan aktivieren", "von OpenTable umsteigen", "Terrasse heute zu", "Verweildauer ändern", "warum ist Samstag ausgebucht" or "floor plan".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "table-plan"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
