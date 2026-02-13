import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetches(pokemon_name:str):
	r = requests.get(f"{BASE_URL}{pokemon_name.lower()}")

	dictionary = {}

	if r.status_code == 200:
		data = r.json()

		dictionary["pokemon_name"] = data['name']
		dictionary["id"] = data['id']
		dictionary["abilities"] = data['abilities']
		dictionary["types"] = data['types']
		dictionary["error"] = None

	else:
		dictionary["error"] = f"Pokemon '{pokemon_name}' non trovato."
		print(f"Errore: Pokemon '{pokemon_name}' non trovato.")

	return dictionary

def print_pokemon_info(pokemon_data:dict):
	if pokemon_data["error"] is None:
		print(f"Nome: {pokemon_data['pokemon_name']}")
		print(f"ID: {pokemon_data['id']}")
		print("Abilità:")
		for ability in pokemon_data['abilities']:
			print(f" - {ability['ability']['name']}")
		print("Tipi:")
		for ptype in pokemon_data['types']:
			print(f" - {ptype['type']['name']}")
	else:
		print(pokemon_data["error"])

if __name__=="__main__":

	pokemon_name = input("Inserisci Pokemon da cercare: ")

	data = fetches(pokemon_name)
	print_pokemon_info(data)