---
name: online-ordering
description: 'Online ordering for guests (pickup and delivery on the venue''s own website): set up per location (zones, payment, dishes), switch on, handle orders — accept with a time, decline, status, pause, sold out online, cancel and refund, delivery tours with drivers and cash, numbers. Use for "Online-Bestellung einrichten", "Abholung", "Lieferung", "Liefertouren", "Fahrer", "Bestellungen annehmen", "online ausverkauft", "Bestellungen pausieren" or "online ordering".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "online-ordering"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
