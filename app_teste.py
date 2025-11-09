from fastapi import FastAPI
import sqlite3
import requests

DB_PATH = "pokemon.db"
app = FastAPI()

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            height INTEGER,
            weight INTEGER,
            base_experience INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_and_store(limit=30):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url).json()
    for item in response["results"]:
        poke = requests.get(item["url"]).json()
        c.execute(
            "INSERT OR REPLACE INTO pokemon (id, name, height, weight, base_experience) VALUES (?, ?, ?, ?, ?)",
            (poke["id"], poke["name"], poke["height"], poke["weight"], poke["base_experience"])
        )
    conn.commit()
    conn.close()
    print(f"✅ {limit} Pokémon salvos no banco!")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, name, height, weight, base_experience FROM pokemon WHERE name = ?", (name.lower(),))
    row = c.fetchone()
    conn.close()
    if not row:
        return {"error": f"Pokémon '{name}' não encontrado."}
    return {"id": row[0], "name": row[1], "height": row[2], "weight": row[3], "base_experience": row[4]}

if __name__ == "__main__":
    create_table()
    fetch_and_store()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
