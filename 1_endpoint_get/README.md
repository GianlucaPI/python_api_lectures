# Flask GET Endpoints - Documentazione Tecnica

Questo progetto dimostra come creare e consumare (fetchare) endpoint API di tipo GET utilizzando Flask.
La documentazione qui sotto spiega come avviare il progetto e le diverse strategie implementate per interagire con l'API.

## Tabella dei Contenuti
1. [Endpoint Disponibili](#endpoint-disponibili)
2. [Installazione e Avvio](#installazione-e-avvio)
3. [Strategie di Fetching (Client)](#strategie-di-fetching-client)

---

## Endpoint Disponibili

Il server espone le seguenti rotte sulla porta **5001**:

| Metodo | Endpoint | Tipo Risposta | Descrizione |
|--------|----------|---------------|-------------|
| `GET` | `/` | `text/plain` | Root dell'applicazione. Restituisce un messaggio di benvenuto. |
| `GET` | `/api/saluto` | `application/json` | Esempio di API REST che restituisce dati strutturati (JSON). |
| `GET` | `/client` | `text/html` | Pagina Web che funge da client grafico per testare le chiamate. |

---

## Installazione e Avvio

### Prerequisiti
- Python 3.x installato

### Setup
1. Apri il terminale in questa cartella (`1_endpoint_get`).
2. (Opzionale) Crea e attiva un ambiente virtuale:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   # venv\Scripts\activate   # Windows
   ```
3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

### Esecuzione del Server
Lancia l'applicazione Flask:
```bash
python app.py
```
Dovresti vedere nel terminale:
```
* Running on http://127.0.0.1:5001
```
*Nota: La porta 5001 è stata scelta per evitare conflitti con la porta 5000 usata da servizi di sistema macOS (AirPlay).*

---

## Strategie di Fetching (Client)

In questa cartella sono presenti diversi modi per "fetchare" (recuperare) i dati dagli endpoint. Ognuno ha un suo caso d'uso specifico.

### 1. Client Python Standard (`client.py`)
Utilizza la libreria esterna `requests`. È il metodo più comune e "Pythonic" per interagire con API.

- **Come eseguirlo**: `python client.py`
- **Perché ha senso**:
  - Sintassi estremamente leggibile e pulita.
  - Gestione automatica della decodifica JSON (`response.json()`).
  - Gestione semplificata di header, parametri e autenticazione.
- **Quando usarlo**: In quasi tutte le applicazioni Python reali dove è possibile installare dipendenze.

### 2. Client Python Nativo (`urllib_client.py`)
Utilizza la libreria `urllib.request` inclusa nativamente in Python.

- **Come eseguirlo**: `python urllib_client.py`
- **Perché ha senso**:
  - **Zero dipendenze**: Funziona su qualsiasi macchina con Python installato, senza bisogno di `pip install`.
  - Utile per script di sistema, installatori, o ambienti containerizzati minimi (es. Alpine Linux) dove si vuole risparmiare spazio.
- **Perché è meno comodo**:
  - Richiede la gestione manuale dei byte e della decodifica (`.decode('utf-8')`).
  - È molto più verboso per fare le stesse operazioni di `requests`.

### 3. Client PHP (`client.php`)
Utilizza la funzione nativa `file_get_contents`.

- **Come eseguirlo**: `php client.php`
- **Perché ha senso**:
  - **Integrazione Legacy/CMS**: Moltissimi siti web girano su PHP (WordPress, Joomla). Questo script simula come un sito PHP esistente potrebbe consumare la nostra nuova API Flask.
  - **Semplicità**: Per chiamate GET semplici, `file_get_contents` è immediato (one-liner).
- **Perché è meno comodo**:
  - `file_get_contents` è bloccante (sincrono).
  - Richiede che `allow_url_fopen` sia abilitato nel `php.ini` del server, altrimenti serve usare cURL (più complesso).

### 4. Client Web HTML/JS (`templates/index.html`)
Un client che gira nel browser dell'utente.

- **Come usarlo**: Apri il browser e vai su [http://127.0.0.1:5001/client](http://127.0.0.1:5001/client)
- **Tecnologia**: JavaScript `fetch()` API.
- **Perché ha senso**: Mostra come un frontend (es. React, Vue, o semplice HTML) interagisce con il backend Flask in modo asincrono.

### 5. Riga di Comando (cURL)
Per test rapidi senza scrivere codice.
```bash
curl http://127.0.0.1:5001/api/saluto
```
