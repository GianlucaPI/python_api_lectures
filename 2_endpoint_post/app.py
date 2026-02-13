from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Endpoint per servire la pagina HTML (Client)
@app.route('/client', methods=['GET'])
def client():
    return render_template('index.html')

# Endpoint root
@app.route('/', methods=['GET'])
def home():
    return "Benvenuto nell'API Flask POST!"

# Endpoint POST che riceve dati JSON e li restituisce con un messaggio
@app.route('/api/processa', methods=['POST'])
def processa_dati():
    # Verifica che la richiesta sia in formato JSON
    if not request.is_json:
        return jsonify({"errore": "Il contenuto deve essere JSON"}), 400
    
    # Recupera i dati dal body della richiesta
    dati = request.get_json()
    
    # Esempio di elaborazione (semplicemente aggiungiamo un campo risposta)
    risposta = {
        "messaggio": "Dati ricevuti con successo!",
        "stato": "elaborato",
        "dati_ricevuti": dati
    }
    
    return jsonify(risposta), 200

if __name__ == '__main__':
    # Avvia il server sulla porta 5002
    app.run(debug=True, port=5002)
