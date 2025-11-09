# PokeIA

📋 Descrição do Projeto

O PokeIA é um projeto que desenvolvi como parte do Desafio Técnico TOTVS — Governança e Dados.
Ele demonstra, na prática, como aplicar conceitos de governança de dados usando Python e FastAPI, integrando informações reais da PokéAPI
.

A aplicação permite:

🔄 Criar automaticamente um banco SQLite com informações dos Pokémons.

🔍 Consultar altura, peso e experiência base via endpoint /pokemon/{name}.

💬 Fazer perguntas em linguagem natural via /ask.

📜 Listar Pokémons cadastrados com o endpoint extra /list (feature extra adicionada por mim).

🚀 Tecnologias Utilizadas
Tecnologia	Função
🐍 Python 3.11+	Linguagem principal
⚡ FastAPI	Framework para APIs REST
💾 SQLite	Banco de dados local e leve
🌐 Requests	Consumo da PokéAPI
🔥 Uvicorn	Servidor ASGI para rodar a API
🧩 Estrutura do Projeto
pokemon-data-agent/
│
├── ingest.py          # Faz ingestão da PokéAPI → cria e popula o banco
├── agent.py           # Lógica de busca e integração com o GPT
├── api.py             # API FastAPI com endpoints /pokemon, /ask e /list
├── pokemon.db         # Banco de dados SQLite gerado automaticamente
├── .venv/             # Ambiente virtual Python
└── README.md          # Documentação do projeto

⚙️ Como Executar o Projeto
1️⃣ Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate

2️⃣ Instalar as dependências
pip install fastapi uvicorn requests

3️⃣ Popular o banco de dados
python ingest.py


💡 Esse script:

Cria o banco pokemon.db

Coleta dados reais da PokéAPI

Insere os primeiros 30 Pokémons no banco

4️⃣ Rodar a API
uvicorn api:app --reload


Depois, abra no navegador:

http://127.0.0.1:8000/docs

🔍 Endpoints Principais
Método	Endpoint	Descrição
GET	/pokemon/{name}	Retorna informações detalhadas do Pokémon
GET	/ask?question=	Interpreta perguntas em linguagem natural
GET	/list	(Feature extra) Lista Pokémons salvos no banco
💬 Exemplos de Uso
🧠 Pergunta:
http://127.0.0.1:8000/ask?question=Qual%20é%20o%20peso%20do%20Pikachu?

✅ Resposta:
O Pokémon Pikachu possui as seguintes informações:
- Altura: 0.4 m
- Peso: 6.0 kg
- Experiência base: 112

🆕 Endpoint Extra /list

Mostra uma lista de Pokémons já inseridos no banco.

http://127.0.0.1:8000/list

Exemplo de resposta:
{
  "pokemons": [
    "bulbasaur",
    "ivysaur",
    "venusaur",
    "charmander",
    "charmeleon",
    "charizard",
    ...
  ]
}

🧠 Lógica do Projeto

ingest.py → coleta e grava dados da PokéAPI no SQLite.

agent.py → faz buscas locais e responde perguntas via GPT.

api.py → organiza as rotas HTTP (/pokemon, /ask, /list).

A arquitetura foi pensada pra ser simples, rastreável e modular — princípios centrais da governança de dados.

📈 Diferenciais Técnicos

✅ Código limpo, comentado e modularizado
✅ Uso real de API externa (PokéAPI)
✅ Feature adicional /list
✅ Logs amigáveis e tratamento de erro na ingestão
✅ Compatível com Python 3.10+

🧩 Aprendizados e Reflexões

Durante o desenvolvimento, reforcei vários conceitos importantes:

Governança de Dados: entendi como aplicar rastreabilidade e padronização em um pipeline simples.

Integração de APIs: pratiquei o consumo de dados externos e a persistência local.

Boas práticas: modularização, logs e clareza de código foram prioridades.

Escolhi manter o projeto enxuto e didático — com código legível, mensagens intuitivas e um fluxo claro entre ingestão, API e consulta.
Mais do que um desafio técnico, foi uma oportunidade real de unir governança + prática de engenharia de dados. 💡

👩‍💻 Autora

Vivianne Ribeiro Fábrio
💼 Engenheira de Software / Data Engineer
📍 São Paulo — SP
📧 [vivi_fabrio@hotmail.com]
🔗 LinkedIn

✨ Desenvolvido com dedicação e curiosidade — combinando dados, tecnologia e um toque de criatividade.
⚡ Complemento — Código do endpoint /list

Pra completar o README e deixar o avaliador ver a feature adicional, adicione esse trecho no final do seu api.py 👇

@app.get("/list")
def list_pokemons():
    import sqlite3
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()
    c.execute("SELECT name FROM pokemon ORDER BY id LIMIT 20")
    data = [row[0] for row in c.fetchall()]
    conn.close()
    return {"pokemons": data}
