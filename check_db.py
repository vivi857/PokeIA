import sqlite3

conn = sqlite3.connect("pokemon.db")
c = conn.cursor()
rows = c.execute("SELECT name, height, weight FROM pokemon LIMIT 5").fetchall()
for r in rows:
    print(r)
conn.close()
