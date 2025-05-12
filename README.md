# 🧠 Was macht diese Route?

```python
@app.route('/search')
def search():
    query = request.args.get('q', 'Keine Suchanfrage')
    sort_by = request.args.get('sort', 'Standard-Sortierung')
    return f'Suche nach: {query}, Sortierung: {sort_by}'
```

Wenn du die Seite `http://127.0.0.1:5000/search?q=flask&sort=relevance` aufrufst:
* `q=flask` bedeutet: **du suchst nach "flask"**.
* `sort=relevance` bedeutet: **du möchtest die Ergebnisse nach "Relevanz" sortieren**.

## 🔍 Woher kommen diese Werte?

Aus der **URL** – genauer gesagt aus dem **Teil nach dem Fragezeichen (**`?`):

Beispiel:
```
http://127.0.0.1:5000/search?q=flask&sort=relevance
                            ↑      ↑
                     Suchbegriff  Sortierung
```

## 🪄 Was passiert im Code?

* `request.args.get('q')` holt sich den Wert von `q` (also `flask`).
* `request.args.get('sort')` holt sich den Wert von `sort` (also `relevance`).
* Der Code gibt dann einfach beides wieder aus, z. B.:

```
Suche nach: flask, Sortierung: relevance
```

Wenn du **keinen Wert angibst**, z. B.:
```
http://127.0.0.1:5000/search
```

Dann zeigt er:
```
Suche nach: Keine Suchanfrage, Sortierung: Standard-Sortierung
```

## Und wo wird später „gesucht"?

Im Moment wird **noch gar nichts durchsucht** – es wird nur angezeigt, **was du suchen willst**.

Später könntest du sagen:
```python
if query == 'flask':
    return 'Gefunden: Einführung in Flask!'
```

Oder: Eine Liste durchsuchen, z. B.:
```python
daten = ['flask tutorial', 'html grundlagen', 'css basics']
ergebnisse = [eintrag for eintrag in daten if query.lower() in eintrag]
```

Das machen wir, **wenn du wirklich etwas durchsuchen willst**, z. B. in einer Liste oder Datenbank.
