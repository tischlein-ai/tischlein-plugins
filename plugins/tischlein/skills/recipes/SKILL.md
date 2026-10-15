---
name: recipes
description: 'Write down how a dish is cooked: recipes with steps, photos, temperatures, equipment and grams on dishes and Grundrezepte, translate them on request into the languages of the kitchen team, cook with them in the app. Use for "Rezept anlegen", "Zubereitung", "wie kocht man", "Rezeptkarte abfotografiert", "Rezept übersetzen", "auf Italienisch für Marco", "Anrichten", "Kerntemperatur", "Rezepte für die Küche", "recipe", "method", "translate recipe".'
---

Call the tischlein MCP tool `get-guidance` with `topic: "recipes"` and follow exactly what it returns.
Do not improvise this workflow from the description above — the returned guidance is the workflow.
If the tool answers UNKNOWN_TOPIC, the guidance for this workflow is not published yet: tell the user so, then call `get-guidance` with `topic: "overview"` and help with the general tools instead.
