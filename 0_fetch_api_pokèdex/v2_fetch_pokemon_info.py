import requests  # Importiamo la libreria standard 'de facto' per le chiamate HTTP in Python

def cerca_pokemon(nome_pokemon):
    """
    Funzione che cerca un Pokemon tramite API e stampa le sue informazioni.
    """
    
    # 1. Definizione dell'ENDPOINT
    # L'URL base della PokeAPI. Usiamo f-string per inserire il nome dinamico.
    # .lower() è importante perché l'API accetta solo minuscolo.
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"

    try:
        # 2. Effettuare la RICHIESTA (Request)
        # Usiamo il metodo .get() perché vogliamo solo leggere dati.
        print(f"🔍 Cerco {nome_pokemon} nel database...")
        response = requests.get(url)

        # 3. Controllo dello STATUS CODE
        # 200 significa "OK" (Trovato).
        # 404 significa "Not Found" (Non trovato).
        if response.status_code == 200:
            
            # 4. Parsing del JSON
            # Convertiamo la risposta grezza (stringa) in un dizionario Python
            data = response.json()

            # 5. Estrazione dei dati
            # Navighiamo nel dizionario per prendere solo ciò che ci serve
            nome = data['name'].capitalize()
            peso = data['weight']
            altezza = data['height']
            
            # I "types" sono una lista di dizionari, usiamo una list comprehension
            # per estrarre solo i nomi dei tipi.
            tipi = [t['type']['name'] for t in data['types']]
            
            # Output formattato per l'utente
            print("\n" + "="*30)
            print(f"🌟 POKEMON TROVATO: {nome}")
            print("="*30)
            print(f"⚖️  Peso: {peso} hg")
            print(f"📏 Altezza: {altezza} dm")
            print(f"🔥 Tipi: {', '.join(tipi)}")
            print("="*30 + "\n")

        elif response.status_code == 404:
            print(f"❌ Errore 404: Il Pokemon '{nome_pokemon}' non esiste.")
        
        else:
            print(f"⚠️ Qualcosa è andato storto. Codice errore: {response.status_code}")

    except requests.exceptions.ConnectionError:
        # Gestione del caso in cui l'utente non ha internet
        print("⛔ Errore di connessione: Controlla la tua rete internet.")

# --- Blocco Main ---
# Questo codice viene eseguito solo se lanciamo il file direttamente
if __name__ == "__main__":
    while True:
        user_input = input("Inserisci il nome di un Pokemon (o 'esci' per chiudere): ")
        
        if user_input.lower() == 'esci':
            print("Alla prossima! 👋")
            break
            
        if user_input.strip(): # Controlla che non sia vuoto
            cerca_pokemon(user_input)