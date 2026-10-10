---
name: dish-costing
description: 'Dish costing ("Kalkulation"): purchase prices from invoices and delivery notes, recipes and Grundrezepte, Wareneinsatz, food-cost % and Deckungsbeitrag per dish (also estimated from a dish photo or an idea), price suggestions and allergen hints. Use for "Kalkulation", "Wareneinsatz", "Was kostet die Pizza?", "Was kostet mich der Teller?", "Welche Gerichte verdienen nichts?", "Rezept anlegen", "Preise aus der Rechnung", "dish costing" or "food cost".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "dish-costing"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
