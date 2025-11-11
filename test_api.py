import sqlite3
import requests
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_api_running():
    """Verifica se a API está respondendo corretamente"""
    response = client.get("/")
    assert response.status_code in (200, 404)

def test_pokemon_count():
    """Verifica se há Pokémons no banco"""
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM pokemon")
    total = c.fetchone()[0]
    conn.close()
    assert total >= 151  

def test_pokeapi_access():
    """Verifica se a PokéAPI está acessível"""
    url = "https://pokeapi.co/api/v2/pokemon?limit=1"
    response = requests.get(url)
    assert response.status_code == 200
