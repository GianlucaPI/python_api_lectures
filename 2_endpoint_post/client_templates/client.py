import requests
import json

# URL dell'endpoint API POST
url = "http://127.0.0.1:5002/api/processa"

# Dati da inviare (Payload)
payload = {
    "nome": "Anna",
    "cognome": "Bianchi",
    "ruolo": "Data Scientist", 
    "tools": ["Python", "Pandas", "Flask"]
}

print(f"Invio dati a {url}...")

try:
    # Eseguiamo la richiesta POST
    # Il parametro 'json' converte automaticamente il dizionario in JSON e imposta l'header Content-Type
    response = requests.post(url, json=payload)
    
    print("\n--- Status Code ---")
    print(response.status_code)
    
    if response.status_code == 200:
        print("\n--- Risposta JSON ---")
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print("\nErrore o risposta inaspettata:")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("Errore: Impossibile connettersi al server. Assicurati che app.py sia in esecuzione sulla porta 5002.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
