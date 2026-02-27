import requests
import json

# URL dell'endpoint API
url = "http://127.0.0.1:5001/api/saluto"

try:
    # Effettuiamo la richiesta GET
    response = requests.get(url)
    
    # Controlliamo se la richiesta è andata a buon fine (codice 200)
    if response.status_code == 200:
        # Convertiamo la risposta in JSON
        data = response.json()
        
        print("--- Risposta dal Server ---")
        print(f"Status Code: {response.status_code}")
        print("Dati ricevuti:")
        # Stampiamo il JSON formattato
        print(json.dumps(data, indent=4))
        
        # Esempio di come accedere a un campo specifico
        print("\n--- Accesso ai dati ---")
        print(f"Messaggio: {data['messaggio']}")
    else:
        print(f"Errore nella richiesta: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Errore: Impossibile connettersi al server. Assicurati che app.py sia in esecuzione.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
