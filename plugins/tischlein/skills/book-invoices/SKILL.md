---
name: book-invoices
description: 'Book supplier invoices and hand them to the tax advisor (Warenwirtschaft): supplier, service period (Leistungszeitraum), matching with delivery notes, price differences, credit notes, due payments and Skonto, the DATEV Buchungsstapel with the documents. Use for "Rechnung verbuchen", "Eingangsrechnung buchen", "Rechnung mit Lieferschein abgleichen", "Was ist diese Woche fällig?", "Skonto", "Gutschrift", "DATEV-Export", "Steuerberater Oktober", "Kontenrahmen" or "book supplier invoice".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "book-invoices"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
