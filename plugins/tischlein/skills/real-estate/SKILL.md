---
name: real-estate
description: 'Property listings for real-estate agents (Makler): create a listing (Exposé) from a PDF, photos or the old web page, energy certificate (GEG §87), preview and publish it, mark it reserved, sold or rented (reference), off-market listings, the properties and references blocks, and answer property inquiries (Exposé anfordern, Besichtigung). Use for "Objekt anlegen", "neues Exposé", "Immobilie einstellen", "Wohnung verkauft", "als Referenz", "Off-Market-Liste", "Besichtigungsanfrage", "property listing" or "mark as sold".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "real-estate"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
