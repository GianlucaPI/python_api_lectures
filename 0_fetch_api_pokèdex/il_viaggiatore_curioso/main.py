import requests

def main():
    print("Benvenuto nell'agenzia di viaggi CuriousTrip! 🧳")
    
    while True:
        country_name = input("\nInserisci il nome di un paese in inglese (es. Italy, Japan) oppure 'q' per uscire: ").strip()
        
        if country_name.lower() == 'q':
            print("Grazie per aver viaggiato con CuriousTrip. A presto!")
            break
            
        if not country_name:
            continue

        # --- FASE 1: REST Countries ---
        print(f"\nRicerca informazioni per {country_name}...")
        country_url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(country_url)
        
        if response.status_code != 200:
            print("❌ Paese non trovato. Assicurati di aver scritto il nome in inglese correttamente.")
            continue
            
        country_data = response.json()[0]
        
        official_name = country_data.get("name", {}).get("official", "N/A")
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        continents = ", ".join(country_data.get("continents", ["N/A"]))
        languages = ", ".join(country_data.get("languages", {}).values())
        
        currencies = country_data.get("currencies", {})
        currency_code = list(currencies.keys())[0] if currencies else "N/A"
        currency_name = currencies[currency_code].get("name", "N/A") if currencies else "N/A"

        # --- FASE 2: Open-Meteo ---
        # Cerchiamo le coordinate della capitale, altrimenti usiamo quelle del paese
        latlng = country_data.get("capitalInfo", {}).get("latlng")
        if not latlng:
            latlng = country_data.get("latlng", [0, 0])
            
        lat, lon = latlng[0], latlng[1]
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        try:
            weather_data = requests.get(weather_url).json().get("current_weather", {})
            temp = weather_data.get("temperature", "N/A")
            wind = weather_data.get("windspeed", "N/A")
            weathercode = weather_data.get("weathercode", -1)
            condition = "☀️ Cielo sereno" if weathercode == 0 else "☁️ Nuvoloso/Variabile"
        except Exception:
            temp, wind, condition = "N/A", "N/A", "N/A"

        # --- FASE 3: ExchangeRate API ---
        budget_input = input("Inserisci un budget in Euro per il viaggio: ").strip()
        try:
            budget_eur = float(budget_input)
        except ValueError:
            print("Valore non valido, imposto il budget a 0.")
            budget_eur = 0.0
            
        try:
            rates_url = "https://open.er-api.com/v6/latest/EUR"
            rates_data = requests.get(rates_url).json().get("rates", {})
            exchange_rate = rates_data.get(currency_code, 1)
            budget_local = budget_eur * exchange_rate
        except Exception:
            budget_local = 0.0

        # --- FASE 4: TheMealDB ---
        try:
            meal_url = "https://www.themealdb.com/api/json/v1/1/random.php"
            meal_data = requests.get(meal_url).json().get("meals", [{}])[0]
            meal_name = meal_data.get("strMeal", "N/A")
            meal_category = meal_data.get("strCategory", "N/A")
            
            ingredients = []
            for i in range(1, 6):
                ing = meal_data.get(f"strIngredient{i}")
                if ing and ing.strip():
                    ingredients.append(ing)
            ingredients_str = ", ".join(ingredients)
            meal_link = meal_data.get("strSource") or meal_data.get("strYoutube") or "N/A"
        except Exception:
            meal_name, meal_category, ingredients_str, meal_link = "N/A", "N/A", "N/A", "N/A"

        # --- FASE 5: Cat Facts & JokeAPI ---
        try:
            cat_url = "https://catfact.ninja/fact"
            cat_fact = requests.get(cat_url).json().get("fact", "N/A")
        except Exception:
            cat_fact = "N/A"

        try:
            joke_url = "https://v2.jokeapi.dev/joke/Any?type=single"
            joke = requests.get(joke_url).json().get("joke", "N/A")
        except Exception:
            joke = "N/A"

        # --- FASE 6: La scheda finale ---
        scheda = f"""
╔══════════════════════════════════════════╗
║        SCHEDA DI VIAGGIO - CURIOUSTRIP   ║
╠══════════════════════════════════════════╣

📍 DESTINAZIONE
   Paese: {official_name}
   Capitale: {capital}
   Continente: {continents}
   Popolazione: {population:,}
   Lingue: {languages}
   Valuta: {currency_name} ({currency_code})

🌤️ METEO A {capital.upper()}
   Temperatura: {temp}°C
   Vento: {wind} km/h
   Condizioni: {condition}

💰 BUDGET
   {budget_eur:.2f} EUR = {budget_local:,.2f} {currency_code}

🍽️ SUGGERIMENTO DELLO CHEF
   Piatto: {meal_name}
   Categoria: {meal_category}
   Ingredienti: {ingredients_str}
   Link ricetta: {meal_link}

🐱 CURIOSITÀ
   "{cat_fact}"

😂 BARZELLETTA DI VIAGGIO
   "{joke}"

╚══════════════════════════════════════════╝
"""
        print(scheda)
        
        # --- FASE 7: BONUS (Salvataggio) ---
        save = input("Vuoi salvare questa scheda in un file di testo? (s/n): ").strip().lower()
        if save == 's':
            filename = f"scheda_{country_name.lower().replace(' ', '_')}.txt"
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(scheda)
                print(f"✅ Scheda salvata con successo in '{filename}'!")
            except Exception as e:
                print(f"❌ Errore durante il salvataggio: {e}")

if __name__ == "__main__":
    main()
