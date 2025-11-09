from openai import OpenAI
import sqlite3

DB_PATH = "pokemon.db"
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # <-- carrega as variáveis do .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_pokemon_info(name: str):
    """Busca dados de um Pokémon pelo nome e retorna uma resposta formatada."""
    import sqlite3

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""
            SELECT name, height, weight, base_experience
            FROM pokemon
            WHERE LOWER(name) = LOWER(?)
        """, (name,))
        row = c.fetchone()
        conn.close()
    except Exception as e:
        return f"Erro ao acessar o banco de dados: {e}"

    if not row:
        return f"Pokémon '{name}' não encontrado no banco."

    nome, altura, peso, exp = row
    return (
        f"O Pokémon {nome.capitalize()} possui as seguintes informações:\n"
        f"- Altura: {altura/10:.1f} m\n"
        f"- Peso: {peso/10:.1f} kg\n"
        f"- Experiência base: {exp}"
    )


def ask_agent(question: str):
    """Usa o modelo GPT para interpretar perguntas sobre Pokémon, consultando o banco automaticamente."""
    import sqlite3
    import re

    # --- 1️⃣ Pega todos os nomes de Pokémon do banco ---
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name FROM pokemon")
    pokemons = [row[0].lower() for row in c.fetchall()]
    conn.close()

    # --- 2️⃣ Procura se algum nome de Pokémon aparece na pergunta ---
    found_pokemon = None
    for name in pokemons:
        if re.search(rf"\b{name}\b", question.lower()):
            found_pokemon = name
            break

    # --- 3️⃣ Se encontrou, busca no banco ---
    if found_pokemon:
        result = get_pokemon_info(found_pokemon)
        return result

    # --- 4️⃣ Caso contrário, usa o GPT normalmente ---
    context = "Você é um assistente especialista em Pokémon. Responda de forma clara e amigável."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

