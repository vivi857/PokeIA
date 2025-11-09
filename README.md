# PokeIA

# 🧠 PokeIA — Desafio TOTVS (Data Engineer / Governança de Dados)

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

## 📋 Descrição do Projeto

O **PokeIA** é um projeto desenvolvido como parte do **Desafio Técnico TOTVS — Governança e Dados**.  
Ele integra **coleta, armazenamento e consulta de dados** utilizando Python, FastAPI e SQLite.  
O sistema conecta-se à **PokéAPI** e permite:

- 🔄 Criar automaticamente um banco de dados SQLite com informações dos Pokémons.  
- 🔍 Consultar altura, peso e experiência base via endpoint `/pokemon/{name}`.  
- 💬 Fazer perguntas em **linguagem natural** via endpoint `/ask`.  

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| 🐍 **Python 3.11+** | Linguagem principal |
| ⚡ **FastAPI** | Framework para APIs REST |
| 💾 **SQLite** | Banco de dados local |
| 🌐 **Requests** | Consumo da PokéAPI |
| 🔥 **Uvicorn** | Servidor ASGI para execução da API |

---

pokemon-data-agent/
│
├── ingest.py # Ingestão de dados da PokéAPI → cria e popula o banco
├── agent.py # Lógica de consulta e interface com o banco
├── api.py # API FastAPI com endpoints /pokemon e /ask
├── pokemon.db # Banco de dados SQLite gerado automaticamente
├── .venv/ # Ambiente virtual Python
└── README.md # Documentação do projeto

## ⚙️ Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate
2️⃣ Instalar as dependências
bash
Copiar código
pip install fastapi uvicorn requests
3️⃣ Popular o banco de dados
bash
Copiar código
python ingest.py
💡 Esse comando:

Cria o banco pokemon.db

Coleta dados reais da PokéAPI

Insere os 30 primeiros Pokémons no banco

4️⃣ Rodar a API
bash
Copiar código
uvicorn api:app --reload
Abra no navegador:

arduino
Copiar código
http://127.0.0.1:8000/docs
🔍 Endpoints Principais
Método	Endpoint	Descrição
GET	/pokemon/{name}	Retorna informações (altura, peso e experiência base) de um Pokémon
GET	/ask?question=	Interpreta perguntas em linguagem natural sobre Pokémons

💬 Exemplo de Uso
🧠 Pergunta:
perl
Copiar código
http://127.0.0.1:8000/ask?question=Qual%20é%20o%20peso%20do%20Pikachu?
✅ Resposta:
diff
Copiar código
O Pokémon Pikachu possui as seguintes informações:
- Altura: 0.4 m
- Peso: 6.0 kg
- Experiência base: 112
🧠 Lógica do Projeto
ingest.py
→ Coleta os dados via PokéAPI e cria o banco SQLite.

agent.py
→ Realiza consultas ao banco e formata as respostas.

api.py
→ Expõe endpoints HTTP via FastAPI para interação com o usuário.

📈 Diferenciais Técnicos
✅ Uso de FastAPI com documentação automática (/docs)
✅ Banco local SQLite com criação dinâmica
✅ Tratamento de erros e logs amigáveis
✅ Código limpo e modularizado
✅ Compatível com Python 3.10+

🧩 Exemplo de Execução (CLI)
bash
Copiar código
(.venv) PS C:\pokemon-data-agent> python ingest.py
🚀 Iniciando ingestão de dados...
🔍 Buscando dados dos primeiros 30 Pokémons...
✅ 1. bulbasaur adicionado com sucesso.
...
💾 30 registros salvos com sucesso no banco 'pokemon.db'.
🏁 Processo finalizado com sucesso!
👩‍💻 Autora
Vivianne Ribeiro Fábrio
💼 Engenheira de Software / Data Engineer
📍 São Paulo — SP
📧 [vivi_fabrio@hotmail.com]
🔗 LinkedIn


