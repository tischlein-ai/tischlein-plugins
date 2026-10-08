---
name: month-close
description: 'Close a month of time tracking: resolve open correction requests and warnings, close the period and export hours for payroll (DATEV LODAS, Lohn und Gehalt, CSV, Excel, PDF timesheets) or send them to the tax advisor. Use for "Monatsabschluss", "Stunden abschließen", "Lohnexport", "DATEV-Export", "Stundenzettel", "an den Steuerberater schicken", "month close" or "payroll export".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "month-close"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
