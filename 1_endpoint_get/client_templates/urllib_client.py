import urllib.request
import json
import urllib.error

# Configurazione dell'URL base
# Nota: Assicurati che la porta corrisponda a quella definita in app.py (default 5001 in questo progetto)
BASE_URL = "http://127.0.0.1:5001"

def fetch_endpoint(path, is_json=False):
    """
    Esegue una richiesta GET all'endpoint specificato usando urllib.
    
    PERCHÉ HA SENSO USARE URLLIB?
    -----------------------------
    1.  **Standard Library**: `urllib` è inclusa in Python. Non devi installare nulla con `pip`.
        Questo è ottimo per script di sistema, ambienti isolati o container minimi dove 
        non si vuole o non si può installare pacchetti esterni come `requests`.
    2.  **Leggerezza**: Per una semplice chiamata GET, importare una libreria esterna gigante 
        potrebbe essere eccessivo.

    PERCHÉ POTREBBE NON AVER SENSO (MEGLIO REQUESTS)?
    -------------------------------------------------
    1.  **Verbosità**: Come vedi qui sotto, devi decodificare manualmente i byte (.decode('utf-8'))
        e gestire la serializzazione JSON esplicitamente. Con `requests` è automatico via `.json()`.
    2.  **Usabilità**: `requests` ha un'API molto più umana (es. gestione parametri, header, auth).
    3.  **Gestione Errori**: `urllib` lancia eccezioni per status code non-200, mentre `requests` 
        permette di controllare `response.status_code` senza blocchi try/except obbligatori 
        (a meno che non si usi raise_for_status).
    """
    url = f"{BASE_URL}{path}"
    print(f"\n--- Chiamata a: {url} ---")

    try:
        # urlopen restituisce un oggetto response che va letto e decodificato
        with urllib.request.urlopen(url) as response:
            # Lettura dei byte e decodifica in stringa
            response_body = response.read().decode('utf-8')
            
            print(f"Status Code: {response.status}")
            
            if is_json:
                # Parsing manuale del JSON
                data = json.loads(response_body)
                print("Risposta JSON formattata:")
                print(json.dumps(data, indent=4))
            else:
                print("Risposta Testuale:")
                print(response_body)

    except urllib.error.URLError as e:
        # Gestione errori di connessione o HTTP error codes (es. 404, 500)
        print(f"Errore durante la chiamata: {e}")
        print("Suggerimento: Controlla che app.py sia in esecuzione sulla porta corretta.")

if __name__ == "__main__":
    print("Avvio test con urllib (Libreria Standard)...")
    
    # 1. Fetch della root (testo semplice)
    fetch_endpoint("/", is_json=False)
    
    # 2. Fetch dell'API JSON
    fetch_endpoint("/api/saluto", is_json=True)
