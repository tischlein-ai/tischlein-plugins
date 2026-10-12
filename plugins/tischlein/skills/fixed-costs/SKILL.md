---
name: fixed-costs
description: 'Fixed costs and contracts (Finanzen, free Beta): capture contracts per company, read the cost report, import bank statements and decide signals, track deadlines and cancellations (only after an explicit yes), allocation keys, cost-list import, tax advisor package. Use for "Fixkosten erfassen", "Vertrag anlegen", "Kontoauszug importieren", "Kündigungsfrist", "was kostet mich im Monat", "Buchhaltung" or "record a contract".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "fixed-costs"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
