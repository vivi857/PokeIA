import fastapi, requests, dotenv
print("Ambiente configurado e funcionando 🎉")


import sqlite3
conn = sqlite3.connect("pokemon.db")
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM pokemon")
print("Total de pokémons:", c.fetchone()[0])
conn.close()
