---
name: maintain-legal-pages
description: 'Create, complete and check the Impressum and the Datenschutzerklärung: check what is missing (operator, legal form, address, e-mail, representative, register, VAT ID, data-protection authority …), ask the owner in one message, save it, regenerate, preview and have it reviewed. Use for "Impressum erstellen", "Impressum vervollständigen", "Datenschutzerklärung erstellen", "Pflichtangaben fehlen", "Rechtstexte prüfen" or "complete the legal notice".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "maintain-legal-pages"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
