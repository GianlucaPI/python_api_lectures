# Flask POST Endpoints - Documentazione Tecnica

Questo progetto è il secondo step del tutorial Flask e dimostra come creare e consumare endpoint API di tipo **POST**.
A differenza delle richieste GET, le richieste POST permettono di inviare dati strutturati (es. JSON) al server per essere elaborati.

## Tabella dei Contenuti
1. [Endpoint Disponibili](#endpoint-disponibili)
2. [Installazione e Avvio](#installazione-e-avvio)
3. [Strategie di Invio Dati (Client)](#strategie-di-invio-dati-client)

---

## Endpoint Disponibili

Il server espone le seguenti rotte sulla porta **5002**:

| Metodo | Endpoint | Tipo Risposta | Descrizione |
|--------|----------|---------------|-------------|
| `GET` | `/` | `text/plain` | Root dell'applicazione. Messaggio di benvenuto. |
| `POST` | `/api/processa` | `application/json` | Riceve un JSON nel body, lo elabora e restituisce una risposta confermando la ricezione. |
| `GET` | `/client` | `text/html` | Pagina Web (form) per testare l'invio POST via browser. |

---

## Installazione e Avvio

### Prerequisiti
- Python 3.x installato

### Setup
1. Apri il terminale in questa cartella (`2_endpoint_post`).
2. (Opzionale) Crea e attiva un ambiente virtuale (o usa quello esistente se condiviso):
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
* Running on http://127.0.0.1:5002
```
*Nota: Usiamo la porta 5002 per poter eventualmente tenere acceso anche l'esempio GET sulla 5001.*

---

## Strategie di Invio Dati (Client)

I file nella cartella `client_templates` mostrano come inviare una richiesta POST con payload JSON in diversi linguaggi.

### 1. Client Python (`client.py`)
Utilizza `requests.post(url, json=data)`.
- **Comando**: `python client_templates/client.py`
- È il metodo standard per script di automazione o comunicazione tra backend Python.

### 2. Client PHP (`client.php`)
Utilizza `file_get_contents` con un contesto HTTP configurato per POST.
- **Comando**: `php client_templates/client.php`
- Dimostra come integrare l'API in siti PHP esistenti senza librerie esterne.

### 3. Client Web HTML/JS (`client_templates/index.html`)
Un'interfaccia web con un form.
- **Uso**: 
  1. Assicurati che il server sia attivo.
  2. Apri il browser su [http://127.0.0.1:5002/client](http://127.0.0.1:5002/client).
  3. Compila i campi e clicca "Invia Dati".
- Usa `fetch()` con `method: 'POST'` e headers `Content-Type: application/json`.

### 4. curl (`curl_client.sh`)
Script bash per testare l'API da riga di comando.
- **Comando**: `bash client_templates/curl_client.sh`
- Utile per debug rapido.

---
**Struttura JSON attesa dall'endpoint `/api/processa`:**
```json
{
    "qualsiasi_chiave": "qualsiasi_valore"
}
```
Il server accetta qualsiasi JSON valido.
