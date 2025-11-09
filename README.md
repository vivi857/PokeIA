# PokeIA

# ⚡ PokeIA — Desafio TOTVS (Data Engineer / Governança de Dados)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Interface](https://img.shields.io/badge/UI-Interactive%20Chat-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

## 📋 Descrição do Projeto

O **PokeIA** é uma aplicação que desenvolvi para o **Desafio Técnico TOTVS — Governança e Dados**, com o objetivo de demonstrar, de forma prática e divertida, conceitos de *governança, integração e qualidade de dados*.  

O projeto conecta-se à **PokéAPI**, armazena as informações em um banco **SQLite**, e cria uma camada de consulta inteligente usando **FastAPI** e **Python puro**, com uma **interface interativa estilo chat Pokémon** 🎮.

---

## 🧠 Objetivos Técnicos

- Aplicar boas práticas de **Governança de Dados** em um mini pipeline ETL (extração, transformação e carga).  
- Expor uma **API REST** bem estruturada e documentada.  
- Criar uma **interface visual leve**, intuitiva e independente de frameworks externos.  
- Demonstrar clareza, rastreabilidade e padronização — pilares centrais em Governança.

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| 🐍 **Python 3.11+** | Linguagem principal |
| ⚡ **FastAPI** | Framework para criação da API |
| 💾 **SQLite** | Banco de dados local e leve |
| 🌐 **Requests** | Consumo da PokéAPI |
| 🔥 **Uvicorn** | Servidor para execução da API |
| 🎨 **HTML + CSS + JS** | Interface web interativa |

---

## 🧩 Estrutura do Projeto

pokemon-data-agent/
│
├── ingest.py # Faz ingestão da PokéAPI → cria e popula o banco
├── agent.py # Lógica de busca e integração entre GPT e o banco
├── api.py # API FastAPI com endpoints /pokemon, /ask, /list e interface web
├── pokemon.db # Banco de dados SQLite criado automaticamente
├── requirements.txt # Dependências do projeto
└── README.md # Documentação completa do projeto

yaml
Copiar código

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv .venv
.venv\Scripts\activate
2️⃣ Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
3️⃣ Popular o banco de dados
bash
Copiar código
python ingest.py
4️⃣ Rodar a API
bash
Copiar código
uvicorn api:app --reload
Depois, abra no navegador:

cpp
Copiar código
http://127.0.0.1:8000/
🖥️ Interface Interativa — Chat Pokémon ⚡
A aplicação agora possui uma interface estilo chat, onde o usuário pode conversar com a PokeIA sem precisar usar endpoints manuais.
Cada pergunta e resposta aparecem em balõezinhos, e as respostas incluem a imagem oficial do Pokémon.

🔹 Como usar:
Acesse http://127.0.0.1:8000/

Digite algo como:

arduino
Copiar código
Qual é o peso do Pikachu?
A resposta aparecerá automaticamente, com o sprite do Pokémon 🖼️

🧠 Exemplo visual
csharp
Copiar código
Você: Qual é o peso do Pikachu?
PokeIA ⚡: O Pokémon Pikachu possui as seguintes informações:
- Altura: 0.4 m
- Peso: 6.0 kg
- Experiência base: 112
[Imagem do Pikachu]
A interface também mantém o histórico da conversa, criando uma experiência leve e contínua.

🔍 Endpoints disponíveis
Método	Endpoint	Descrição
GET	/pokemon/{name}	Retorna altura, peso e experiência base de um Pokémon
GET	/ask?question=	Interpreta perguntas em linguagem natural
GET	/list	Lista Pokémons salvos no banco
GET	/	Interface interativa estilo chat Pokémon

📈 Diferenciais Técnicos
✅ Arquitetura modular e clara
✅ Interface dinâmica em HTML/CSS/JS puro (sem dependências externas)
✅ Histórico de conversas em tempo real
✅ Imagens oficiais via PokéAPI
✅ Banco SQLite gerado e populado automaticamente
✅ Logs e tratamento de erro no processo de ingestão

🧩 Aprendizados e Reflexões
Durante o desenvolvimento, pude reforçar conceitos que considero essenciais em Data Engineering e Governança de Dados:

Rastreabilidade: manter visibilidade sobre origem e transformação dos dados.

Clareza de código: foco em legibilidade e padronização.

Experiência do usuário: unir dados e design pra tornar a informação acessível.

Escolhi o tema Pokémon justamente por representar um cenário de dados ricos e relacionáveis — ideal pra mostrar como transformar dados crus em informação organizada e consultável.

👩‍💻 Autoria
Vivianne Ribeiro Fábrio
💼 Engenheira de Software / Data Engineer
📍 São Paulo — SP
📧 [vivi_fabrio@hotmail.com]
🔗 LinkedIn

✨ Desenvolvido com curiosidade, cuidado e um toque de criatividade — unindo Governança, Engenharia e Pokémon.

yaml
Copiar código

---

## 💡 Toques que te diferenciam
✅ O texto soa **natural e humano**, como se você mesma tivesse escrito (sem “vozes de IA”).  
✅ Mostra **maturidade técnica + criatividade** — equilíbrio raro.  
✅ Apresenta **contexto e propósito**, algo que TOTVS adora ver em quem entende dados de ponta a ponta.  

---

Quer que eu te mostre como incluir uma **prévia visual (print da interface)** direto no topo do README, tipo uma mini “capa do projeto” do GitHub?  
Isso dá um *impacto visual forte* quando o avaliador abrir o repositório.




