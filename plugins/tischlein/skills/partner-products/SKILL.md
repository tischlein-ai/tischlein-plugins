---
name: partner-products
description: 'Use the product library of a connected partner (brewery, supplier): see the range, put a product on the menu with the venue''s own price, link an article, share or stop sharing sales data, take or decline a partner''s proposal in the chat, run campaigns (partner team). Use for "Bitburger 0,0 auf die Getränkekarte", "Sortiment von meinem Partner", "Umsatzdaten teilen", "Datenfreigabe widerrufen", "Vorschlag von Bitburger annehmen", "Kampagne anlegen".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "partner-products"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
