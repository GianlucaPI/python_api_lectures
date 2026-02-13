"""
Pokédex con interfaccia grafica Tkinter.
Usa la PokeAPI (https://pokeapi.co/) per cercare Pokémon
e mostrare sprite, tipi, statistiche e abilità.
"""

import tkinter as tk
from tkinter import messagebox
from io import BytesIO
import requests

try:
    from PIL import Image, ImageTk
except ImportError:
    raise SystemExit(
        "Pillow è richiesto. Installalo con:  pip install Pillow"
    )

# ── Costanti ──────────────────────────────────────────────
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 1025  # Pokémon disponibili nella PokeAPI

# Colori per tipo
TYPE_COLORS = {
    "normal": "#A8A878", "fire": "#F08030", "water": "#6890F0",
    "electric": "#F8D030", "grass": "#78C850", "ice": "#98D8D8",
    "fighting": "#C03028", "poison": "#A040A0", "ground": "#E0C068",
    "flying": "#A890F0", "psychic": "#F85888", "bug": "#A8B820",
    "rock": "#B8A038", "ghost": "#705898", "dragon": "#7038F8",
    "dark": "#705848", "steel": "#B8B8D0", "fairy": "#EE99AC",
}

BG_RED = "#DC0A2D"
BG_DARK = "#2B2B2B"
FG_WHITE = "#FFFFFF"


# ── Funzioni API ──────────────────────────────────────────
def fetch_pokemon(query: str | int) -> dict | None:
    """Scarica i dati di un Pokémon dalla PokeAPI."""
    url = f"{BASE_URL}{str(query).lower().strip()}"
    try:
        r = requests.get(url, timeout=10)
    except requests.RequestException:
        return None
    if r.status_code != 200:
        return None
    data = r.json()
    return {
        "id": data["id"],
        "name": data["name"].capitalize(),
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"].capitalize() for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "weight": data["weight"] / 10,   # kg
        "height": data["height"] / 10,   # m
        "sprite": data["sprites"]["other"]["official-artwork"]["front_default"]
                  or data["sprites"]["front_default"],
    }


def load_sprite(url: str, size: tuple[int, int] = (200, 200)):
    """Scarica un'immagine e restituisce un ImageTk.PhotoImage."""
    try:
        raw = requests.get(url, timeout=10).content
        img = Image.open(BytesIO(raw)).resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


# ── Interfaccia Grafica ───────────────────────────────────
class Pokedex(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokédex")
        self.configure(bg=BG_RED)
        self.resizable(False, False)

        self.current_id = 1
        self._sprite_ref = None  # evita garbage-collection dell'immagine

        self._build_ui()
        self._search(self.current_id)

    # ── Layout ────────────────────────────────────────────
    def _build_ui(self):
        # --- Barra di ricerca ---
        search_frame = tk.Frame(self, bg=BG_RED)
        search_frame.pack(padx=16, pady=(16, 8), fill="x")

        self.entry = tk.Entry(
            search_frame, font=("Consolas", 14), bd=0,
            highlightthickness=2, highlightcolor="#FFCB05",
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.entry.bind("<Return>", lambda _: self._on_search())

        tk.Button(
            search_frame, text="Cerca", font=("Arial", 11, "bold"),
            bg="#FFCB05", fg=BG_DARK, activebackground="#FFD740",
            bd=0, padx=14, command=self._on_search,
        ).pack(side="left", padx=(8, 0))

        # --- Schermo principale ---
        screen = tk.Frame(self, bg=BG_DARK, bd=4, relief="ridge")
        screen.pack(padx=16, pady=8)

        # Sprite
        self.sprite_label = tk.Label(screen, bg=BG_DARK)
        self.sprite_label.pack(pady=(12, 4))

        # Nome e ID
        self.name_label = tk.Label(
            screen, text="", font=("Arial", 20, "bold"),
            bg=BG_DARK, fg=FG_WHITE,
        )
        self.name_label.pack()

        self.id_label = tk.Label(
            screen, text="", font=("Arial", 12),
            bg=BG_DARK, fg="#AAAAAA",
        )
        self.id_label.pack()

        # Tipi
        self.types_frame = tk.Frame(screen, bg=BG_DARK)
        self.types_frame.pack(pady=6)

        # Info peso / altezza
        self.info_label = tk.Label(
            screen, text="", font=("Consolas", 11),
            bg=BG_DARK, fg=FG_WHITE, justify="left",
        )
        self.info_label.pack(pady=(2, 6))

        # Statistiche
        stats_container = tk.Frame(screen, bg=BG_DARK)
        stats_container.pack(padx=16, pady=(0, 8), fill="x")

        self.stat_bars: dict[str, tuple[tk.Label, tk.Canvas]] = {}
        stat_nice = {
            "hp": "HP", "attack": "ATK", "defense": "DEF",
            "special-attack": "SP.A", "special-defense": "SP.D",
            "speed": "SPD",
        }
        for key, label_text in stat_nice.items():
            row = tk.Frame(stats_container, bg=BG_DARK)
            row.pack(fill="x", pady=1)

            name_lbl = tk.Label(
                row, text=label_text, width=5, anchor="w",
                font=("Consolas", 10, "bold"), bg=BG_DARK, fg="#FFCB05",
            )
            name_lbl.pack(side="left")

            val_lbl = tk.Label(
                row, text="0", width=4, anchor="e",
                font=("Consolas", 10), bg=BG_DARK, fg=FG_WHITE,
            )
            val_lbl.pack(side="left")

            canvas = tk.Canvas(
                row, height=12, bg="#444444",
                highlightthickness=0, bd=0,
            )
            canvas.pack(side="left", fill="x", expand=True, padx=(6, 0))

            self.stat_bars[key] = (val_lbl, canvas)

        # Abilità
        self.abilities_label = tk.Label(
            screen, text="", font=("Arial", 10),
            bg=BG_DARK, fg="#CCCCCC", wraplength=340, justify="center",
        )
        self.abilities_label.pack(pady=(2, 12))

        # --- Navigazione ---
        nav_frame = tk.Frame(self, bg=BG_RED)
        nav_frame.pack(padx=16, pady=(4, 16), fill="x")

        tk.Button(
            nav_frame, text="◀  Precedente", font=("Arial", 11, "bold"),
            bg="#333333", fg=FG_WHITE, activebackground="#555555",
            bd=0, padx=12, pady=4, command=self._prev,
        ).pack(side="left")

        tk.Button(
            nav_frame, text="Successivo  ▶", font=("Arial", 11, "bold"),
            bg="#333333", fg=FG_WHITE, activebackground="#555555",
            bd=0, padx=12, pady=4, command=self._next,
        ).pack(side="right")

    # ── Logica ────────────────────────────────────────────
    def _on_search(self):
        query = self.entry.get().strip()
        if not query:
            return
        self._search(query)

    def _search(self, query: str | int):
        self.config(cursor="watch")
        self.update_idletasks()

        data = fetch_pokemon(query)

        self.config(cursor="")
        if data is None:
            messagebox.showwarning(
                "Non trovato",
                f"Pokémon '{query}' non trovato.\n"
                "Prova con un nome o un numero valido (1-1025).",
            )
            return

        self.current_id = data["id"]
        self._display(data)

    def _display(self, data: dict):
        # Sprite
        if data["sprite"]:
            photo = load_sprite(data["sprite"])
            if photo:
                self._sprite_ref = photo
                self.sprite_label.config(image=photo)
            else:
                self.sprite_label.config(image="", text="(no image)")
        else:
            self.sprite_label.config(image="", text="(no image)")

        # Nome e ID
        self.name_label.config(text=data["name"])
        self.id_label.config(text=f"#{data['id']:04d}")

        # Tipi (badge colorati)
        for w in self.types_frame.winfo_children():
            w.destroy()
        for t in data["types"]:
            color = TYPE_COLORS.get(t, "#888888")
            tk.Label(
                self.types_frame, text=t.upper(),
                font=("Arial", 10, "bold"), bg=color, fg=FG_WHITE,
                padx=10, pady=2,
            ).pack(side="left", padx=3)

        # Peso / Altezza
        self.info_label.config(
            text=f"Peso: {data['weight']:.1f} kg   |   Altezza: {data['height']:.1f} m"
        )

        # Statistiche con barre
        for key, (val_lbl, canvas) in self.stat_bars.items():
            value = data["stats"].get(key, 0)
            val_lbl.config(text=str(value))
            canvas.delete("all")
            canvas.update_idletasks()
            max_w = canvas.winfo_width() or 200
            bar_w = max(1, int(max_w * min(value, 255) / 255))
            color = self._stat_color(value)
            canvas.create_rectangle(0, 0, bar_w, 14, fill=color, outline="")

        # Abilità
        ab_text = "Abilità: " + ", ".join(data["abilities"])
        self.abilities_label.config(text=ab_text)

        # Aggiorna campo di ricerca
        self.entry.delete(0, "end")
        self.entry.insert(0, data["name"])

    @staticmethod
    def _stat_color(value: int) -> str:
        if value < 50:
            return "#F44336"
        if value < 80:
            return "#FF9800"
        if value < 120:
            return "#FFEB3B"
        return "#4CAF50"

    def _prev(self):
        new_id = self.current_id - 1
        if new_id < 1:
            new_id = MAX_POKEMON
        self._search(new_id)

    def _next(self):
        new_id = self.current_id + 1
        if new_id > MAX_POKEMON:
            new_id = 1
        self._search(new_id)


# ── Main ──────────────────────────────────────────────────
if __name__ == "__main__":
    app = Pokedex()
    app.mainloop()
