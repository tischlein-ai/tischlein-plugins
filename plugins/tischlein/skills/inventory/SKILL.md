---
name: inventory
description: 'Stock keeping in the Warenwirtschaft: correct the stock of one article ("Tomaten 4 kg", "2 Flaschen Gin kaputt", "Personalessen: 3 Schnitzel"), count the whole store room with the guided Inventur (blind, offline, several people), print the Inventurliste, transfer stock between locations. Use for "Bestand korrigieren", "Tomaten 4 kg", "Inventur", "Lager zählen", "Inventurliste", "Schwund", "Bruch", "Personalessen", "umlagern", "stock take" or "correct stock".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "inventory"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
