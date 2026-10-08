---
name: complete-impressum
description: 'Complete the Impressum: find the required legal data that is still missing (operator, legal form, address, e-mail, representative, register entry, VAT ID …), ask the owner for it in one message, save it and refresh the legal pages. Use for "Impressum vervollständigen", "Impressum ergänzen", "fehlende Angaben im Impressum", "Pflichtangaben Impressum", "Rechtstexte: es fehlen noch Angaben" or "complete the legal notice".'
---

Call the Tischlein MCP tool `get-guidance` with `topic: "complete-impressum"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
