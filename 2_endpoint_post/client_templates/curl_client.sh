#!/bin/bash

# Endpoint API
URL="http://127.0.0.1:5002/api/processa"

echo "Invio richiesta POST a $URL con cURL..."

# curl -X POST 
# -H "Content-Type: application/json" -> Specifica che inviamo JSON
# -d '...' -> Il corpo della richiesta (i dati)
curl -X POST "$URL" \
     -H "Content-Type: application/json" \
     -d '{"nome": "Mario", "cognome": "Rossi", "ruolo": "Sviluppatore"}'

echo -e "\n\nRichiesta completata."
