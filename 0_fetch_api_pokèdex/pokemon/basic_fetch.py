# importiamo la libreria "requests" che ci permette di fare richieste HTTP
import requests

# facciamo una richiesta GET all'API di Pokemon, chiedendo i dati di Pikachu
# è come aprire questo URL nel browser: https://pokeapi.co/api/v2/pokemon/pikachu
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# la risposta dell'API è in formato JSON (simile a un dizionario Python)
# con .json() convertiamo la risposta in un dizionario Python
data = response.json()

# ora possiamo accedere ai dati come in un normale dizionario
print(data["name"])        # nome del Pokemon
print(data["id"])          # numero nel Pokedex
print(data["types"])       # tipi (es. electric)
print(data["abilities"])   # abilità
