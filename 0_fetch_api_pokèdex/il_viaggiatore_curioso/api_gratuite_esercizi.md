# API Gratuite per Esercitarsi

Una lista di API pubbliche e gratuite da usare per esercitarsi con `requests` in Python.  
Per ognuna trovi: una breve descrizione, l'endpoint di esempio e cosa restituisce.

> **Nota:** Queste API non richiedono autenticazione (o offrono un piano gratuito). Controlla sempre la documentazione ufficiale per eventuali limiti di utilizzo (rate limit).

---

## 🐾 Animali

### Dog API — Immagini casuali di cani
- **Docs:** https://dog.ceo/dog-api/
- **Endpoint:** `https://dog.ceo/api/breeds/image/random`
- **Restituisce:** un'immagine casuale di un cane

### Cat Facts — Curiosità sui gatti
- **Docs:** https://catfact.ninja/
- **Endpoint:** `https://catfact.ninja/fact`
- **Restituisce:** un fatto casuale sui gatti

---

## 🌤️ Meteo

### Open-Meteo — Previsioni meteo
- **Docs:** https://open-meteo.com/en/docs
- **Endpoint:** `https://api.open-meteo.com/v1/forecast?latitude=41.89&longitude=12.48&current_weather=true`
- **Restituisce:** meteo attuale per Roma (modifica latitudine e longitudine per altre città)

---

## 🌍 Geografia

### REST Countries — Informazioni sui paesi
- **Docs:** https://restcountries.com/
- **Endpoint:** `https://restcountries.com/v3.1/name/italy`
- **Restituisce:** informazioni dettagliate su un paese (popolazione, capitale, lingue, bandiera...)

### IP API — Geolocalizzazione da IP
- **Docs:** https://ip-api.com/docs
- **Endpoint:** `http://ip-api.com/json/`
- **Restituisce:** posizione geografica stimata in base al tuo indirizzo IP

---

## 🚀 Spazio

### NASA APOD — Foto astronomica del giorno
- **Docs:** https://api.nasa.gov/
- **Endpoint:** `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`
- **Restituisce:** immagine astronomica del giorno con titolo e descrizione

### Open Notify — Posizione della ISS
- **Docs:** http://open-notify.org/Open-Notify-API/
- **Endpoint:** `http://api.open-notify.org/iss-now.json`
- **Restituisce:** posizione attuale della Stazione Spaziale Internazionale (latitudine e longitudine)

---

## 📚 Cultura e Intrattenimento

### Open Library — Ricerca libri
- **Docs:** https://openlibrary.org/developers/api
- **Endpoint:** `https://openlibrary.org/search.json?q=python+programming`
- **Restituisce:** lista di libri corrispondenti alla ricerca

### JokeAPI — Barzellette
- **Docs:** https://v2.jokeapi.dev/
- **Endpoint:** `https://v2.jokeapi.dev/joke/Any?lang=it`
- **Restituisce:** una barzelletta casuale (disponibile anche in italiano)

### Quotable — Citazioni famose
- **Docs:** https://github.com/lukePeavey/quotable
- **Endpoint:** `https://api.quotable.io/random`
- **Restituisce:** una citazione casuale con autore

---

## 💰 Finanza

### ExchangeRate API — Tassi di cambio valute
- **Docs:** https://www.exchangerate-api.com/
- **Endpoint:** `https://open.er-api.com/v6/latest/EUR`
- **Restituisce:** tassi di cambio attuali rispetto all'Euro

---

## 🍔 Cibo e Bevande

### TheMealDB — Ricette
- **Docs:** https://www.themealdb.com/api.php
- **Endpoint:** `https://www.themealdb.com/api/json/v1/1/random.php`
- **Restituisce:** una ricetta casuale con ingredienti e istruzioni

### TheCocktailDB — Cocktail
- **Docs:** https://www.thecocktaildb.com/api.php
- **Endpoint:** `https://www.thecocktaildb.com/api/json/v1/1/random.php`
- **Restituisce:** un cocktail casuale con ingredienti e preparazione

---

## 🎓 Università

### Hipolabs Universities — Lista università
- **Docs:** https://github.com/Hipo/university-domains-list-api
- **Endpoint:** `http://universities.hipolabs.com/search?country=Italy`
- **Restituisce:** lista delle università in un dato paese

---

## 🧪 Esercizio consigliato

Scegli una o più API dalla lista e crea un programma Python che:

1. Faccia una richiesta GET all'endpoint
2. Converta la risposta in JSON
3. Stampi a schermo le informazioni più interessanti

**Esempio di struttura:**

```python
import requests

response = requests.get("URL_DELL_API")
data = response.json()

# stampa i dati che ti interessano
print(data)
```

**Sfida extra:** prova a combinare più API in un unico programma! Ad esempio, chiedi all'utente un paese, mostra le info con REST Countries e poi il meteo della capitale con Open-Meteo.
