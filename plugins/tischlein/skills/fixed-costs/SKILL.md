---
name: fixed-costs
description: 'Fixed costs and contracts (Finanzen, pilot): capture contracts per company, read the cost report, import bank statements and decide signals (recurring payment, price change, missed payment). Reminders, cancellations, allocation, cost-list import and the tax advisor package come later. Use for "Fixkosten erfassen", "Vertrag anlegen", "Kontoauszug importieren", "Kündigungsfrist", "was kostet mich im Monat", "Buchhaltung" or "record a contract".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "fixed-costs"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
