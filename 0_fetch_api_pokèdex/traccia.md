# 🧭 Traccia — "Il Viaggiatore Curioso"

**Durata stimata:** ~2 ore  
**Prerequisiti:** Python base, concetto di dizionario, uso di `requests`  
**File di riferimento:** `basic_fetch.py`, `api_gratuite_esercizi.md`

---

## 📖 Scenario

Sei uno sviluppatore che lavora per un'agenzia di viaggi molto particolare: **CuriousTrip**.  
I clienti di CuriousTrip non vogliono solo prenotare un viaggio — vogliono sapere **tutto** sulla loro destinazione prima di partire: meteo, informazioni sul paese, una ricetta tipica, e persino una curiosità sugli animali locali.

Il tuo compito è creare un programma Python che, dato il nome di un paese, costruisca una **scheda di viaggio completa** raccogliendo dati da diverse API gratuite.

---

## 🎯 Obiettivi

Alla fine dell'esercitazione sarai in grado di:
- Fare richieste HTTP GET con `requests`
- Leggere e navigare risposte JSON complesse
- Combinare dati provenienti da fonti diverse
- Gestire errori di base nelle chiamate API

---

## 📋 Fasi di sviluppo

### Fase 1 — Setup e primo fetch (20 min)

1. Crea un file `viaggiatore.py`
2. Chiedi all'utente di inserire il nome di un paese in inglese (es. `Italy`, `Japan`, `Brazil`)
3. Usa **REST Countries** per ottenere le informazioni su quel paese:
   - `https://restcountries.com/v3.1/name/{nome_paese}`
4. Dalla risposta, stampa:
   - Nome ufficiale del paese
   - Capitale
   - Popolazione
   - Continente
   - Lingue parlate
   - Valuta utilizzata

**Suggerimento:** la risposta è una lista, prendi il primo elemento con `data[0]`.

---

### Fase 2 — Che tempo fa? (20 min)

1. Dalla risposta di REST Countries, estrai le coordinate della capitale (cerca il campo `capitalInfo` → `latlng`)
2. Usa quelle coordinate per chiamare **Open-Meteo** e ottenere il meteo attuale:
   - `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`
3. Stampa:
   - Temperatura attuale
   - Velocità del vento
   - Se il campo `weathercode` è 0 stampa "☀️ Cielo sereno", altrimenti stampa "☁️ Nuvoloso/Variabile"

---

### Fase 3 — Quanto costa il viaggio? (15 min)

1. Dalla risposta di REST Countries, trova il codice della valuta locale (es. `JPY` per il Giappone, `BRL` per il Brasile)
2. Usa **ExchangeRate API** per ottenere il tasso di cambio rispetto all'Euro:
   - `https://open.er-api.com/v6/latest/EUR`
3. Chiedi all'utente un budget in Euro (es. `500`)
4. Stampa quanto vale quel budget nella valuta locale del paese scelto

---

### Fase 4 — Cosa si mangia? (15 min)

1. Usa **TheMealDB** per ottenere una ricetta casuale:
   - `https://www.themealdb.com/api/json/v1/1/random.php`
2. Stampa:
   - Nome del piatto
   - Categoria (es. Seafood, Dessert...)
   - I primi 5 ingredienti (i campi si chiamano `strIngredient1`, `strIngredient2`, ecc.)
   - Link alle istruzioni (campo `strSource` oppure `strYoutube`)

**Nota:** TheMealDB restituisce ricette internazionali, quindi il piatto potrebbe non essere del paese scelto — va bene così! Presentalo come "suggerimento dello chef".

---

### Fase 5 — Curiosità del giorno (15 min)

1. Usa **Cat Facts** per ottenere una curiosità sui gatti:
   - `https://catfact.ninja/fact`
2. Usa **JokeAPI** per ottenere una barzelletta:
   - `https://v2.jokeapi.dev/joke/Any?lang=it&type=single`
3. Stampa entrambe come "intrattenimento di viaggio"

---

### Fase 6 — La scheda finale (20 min)

Assembla tutto in un output ordinato e leggibile. Il programma deve stampare una scheda così strutturata:

```
╔══════════════════════════════════════════╗
║        SCHEDA DI VIAGGIO - CURIOUSTRIP   ║
╠══════════════════════════════════════════╣

📍 DESTINAZIONE
   Paese: Japan
   Capitale: Tokyo
   Continente: Asia
   Popolazione: 125,836,021
   Lingue: Japanese
   Valuta: Japanese yen (JPY)

🌤️ METEO A TOKYO
   Temperatura: 12°C
   Vento: 15 km/h
   Condizioni: ☀️ Cielo sereno

💰 BUDGET
   500 EUR = 78,500 JPY

🍽️ SUGGERIMENTO DELLO CHEF
   Piatto: Sushi
   Categoria: Seafood
   Ingredienti: Rice, Nori, Salmon, Avocado, Soy Sauce

🐱 CURIOSITÀ
   "Cats sleep for 70% of their lives."

😂 BARZELLETTA DI VIAGGIO
   "Perché il computer è andato dal dottore? Perché aveva un virus!"

╚══════════════════════════════════════════╝
```

---

### Fase 7 — BONUS (15 min, facoltativo)

Scegli uno o più bonus da implementare:

- **🔁 Loop:** alla fine della scheda, chiedi all'utente se vuole cercare un altro paese o uscire
- **📸 Foto spaziale:** aggiungi alla scheda la foto astronomica del giorno dalla **NASA APOD** (`https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`) — stampa il titolo e l'URL dell'immagine
- **🐶 Random dog:** al posto (o in aggiunta) del cat fact, mostra il link a un'immagine casuale di cane con **Dog API** (`https://dog.ceo/api/breeds/image/random`)
- **🎓 Università:** usa **Hipolabs Universities** per stampare le prime 3 università del paese scelto
- **💾 Salvataggio:** salva la scheda di viaggio in un file `.txt` con il nome del paese (es. `scheda_japan.txt`)

---

## ⚠️ Consigli

- Lavora **una fase alla volta**. Testa ogni fase prima di passare alla successiva.
- Usa `print(data)` o `print(data.keys())` per esplorare la struttura delle risposte JSON quando non sai cosa contengono.
- Se un'API non risponde, non bloccarti: vai avanti con le altre e torna dopo.
- Non serve creare funzioni — puoi scrivere tutto in sequenza. Se però vuoi organizzare meglio il codice, sentiti libero di farlo.

---

**Buon viaggio! 🧳**
