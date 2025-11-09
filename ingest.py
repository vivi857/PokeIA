import requests
import sqlite3
from time import sleep

DB_PATH = "pokemon.db"

def create_table():
    """Cria a tabela 'pokemon' no banco de dados, caso ainda não exista."""
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

def fetch_pokemon_data(limit=251):
    """Busca dados da PokéAPI e retorna uma lista com as informações principais."""
    print(f"🔍 Buscando dados dos primeiros {limit} Pokémons...")
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()  # Lança erro se falhar
    data = response.json()["results"]
    results = []

    for i, item in enumerate(data, start=1):
        try:
            pokemon_data = requests.get(item["url"]).json()
            results.append((
                pokemon_data["id"],
                pokemon_data["name"],
                pokemon_data["height"],
                pokemon_data["weight"],
                pokemon_data["base_experience"]
            ))
            print(f"✅ {i}. {pokemon_data['name']} adicionado com sucesso.")
            sleep(0.2)  # Evita sobrecarregar a API
        except Exception as e:
            print(f"⚠️ Erro ao coletar dados de {item['name']}: {e}")
    return results

def save_to_db(pokemons):
    """Insere ou atualiza os dados no banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany(
        "INSERT OR REPLACE INTO pokemon VALUES (?, ?, ?, ?, ?)",
        pokemons
    )
    conn.commit()
    conn.close()
    print(f"💾 {len(pokemons)} registros salvos com sucesso no banco '{DB_PATH}'.")

def main():
    print("🚀 Iniciando ingestão de dados...")
    create_table()
    pokemons = fetch_pokemon_data(limit=251)
    save_to_db(pokemons)
    print("🏁 Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()
