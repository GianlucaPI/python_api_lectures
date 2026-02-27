from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Endpoint per servire la pagina HTML
@app.route('/client', methods=['GET'])
def client():
    return render_template('index.html')

# Endpoint di base (root)
@app.route('/', methods=['GET'])
def home():
    return "Benvenuto nella mia prima API con Flask!"

# Endpoint che restituisce un JSON
@app.route('/api/saluto', methods=['GET'])
def saluto():
    dati = {
        "messaggio": "Ciao studente!",
        "stato": "successo",
        "lezione": "Flask GET Endpoints"
    }
    return jsonify(dati)

if __name__ == '__main__':
    # Avvia il server in modalità debug su una porta diversa per evitare conflitti con AirPlay
    app.run(debug=True, port=5001)
