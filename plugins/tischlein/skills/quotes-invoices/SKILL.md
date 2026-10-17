---
name: quotes-invoices
description: 'Quotes and invoices (Angebote & Rechnungen): quote from an event or catering inquiry (with AI), send it, record acceptance, deposit and final invoice, cancellation by the guest, payments, Mahnungen, credit notes, open items, DATEV export. Use for "Angebot machen", "Angebot senden", "Anzahlung", "Schlussrechnung", "Rechnung stellen", "Rechnung stornieren", "Gutschrift", "Wer hat noch nicht bezahlt", "Mahnung", "offene Posten", "Veranstaltung absagen", "quote", "invoice" or "dunning".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "quotes-invoices"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
