# PokeIA

# PokeIA — Desafio TOTVS (Data Engineer / Governança de Dados)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Interface](https://img.shields.io/badge/UI-Interactive%20Chat-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

## Descrição do Projeto

O **PokeIA** é uma aplicação que desenvolvi para o **Desafio Técnico TOTVS — Governança e Dados**, com o objetivo de demonstrar, de forma prática e divertida, conceitos de *governança, integração e qualidade de dados*.  

O projeto conecta-se à **PokéAPI**, armazena as informações em um banco **SQLite**, e cria uma camada de consulta inteligente usando **FastAPI** e **Python puro**, com uma **interface interativa estilo chat Pokémon**.

---

## Objetivos Técnicos

- Aplicar boas práticas de **Governança de Dados** em um mini pipeline ETL (extração, transformação e carga).  
- Expor uma **API REST** bem estruturada e documentada.  
- Criar uma **interface visual leve**, intuitiva e independente de frameworks externos.  
- Demonstrar clareza, rastreabilidade e padronização — pilares centrais em Governança.

---

## Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
|**Python 3.11+** | Linguagem principal |
|**FastAPI** | Framework para criação da API |
|**OpenAI API** | Inteligência artificial para interpretar perguntas |
|**SQLite** | Banco de dados local e leve |
|**Requests** | Consumo da PokéAPI |
|**Uvicorn** | Servidor para execução da API |
|**HTML + CSS + JS** | Interface web interativa |

---

## Estrutura do Projeto

pokemon-data-agent/
│
 PokeIA/
 | ── ingest.py          # Coleta dados da PokéAPI e salva no banco |
 ├── check_db.py        # Verifica conteúdo do banco |
 ├── agent.py           # Lógica de IA e conexão com OpenAI |
 ├── api.py             # API principal (FastAPI) |
 ├── pokemon.db         # Banco SQLite |
 ├── .env               # Chave da API (não versionado) |
 ├── requirements.txt   # Dependências do projeto |
 └── README.md          # Documentação do projeto |



---

## Como Executar o Projeto

1️ Clonar o repositório
git clone https://github.com/vivi857/PokeIA.git
cd PokeIA

2️ Criar e ativar o ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate

3️ Instalar as dependências
pip install -r requirements.txt

4️ Criar o arquivo .env (para a chave da OpenAI):

Clique em:
https://platform.openai.com/api-keys

Gere uma nova chave (começa com sk-...).

Crie um arquivo .env na raiz do projeto com o conteúdo:

OPENAI_API_KEY=sk-sua-chave-aqui

Importante: nunca envie o arquivo .env para o GitHub.
Ele já está listado no .gitignore e será ignorado automaticamente.

## Como Rodar o Projeto:

1 Popular o banco com Pokémons:
python ingest.py

2 Iniciar o servidor:
uvicorn api:app --reload

3 Acesse no navegador:
http://127.0.0.1:8000

## Como Usar:

Abra o site local.

Digite uma pergunta sobre um Pokémon, como:

“Qual é o peso do Pikachu?”

PokeIA: O Pokémon Pikachu possui as seguintes informações:
- Altura: 0.4 m
- Peso: 6.0 kg
- Experiência base: 112

O chat irá interpretar sua pergunta e responder com os dados diretamente do banco.
A interface também mantém o histórico da conversa, criando uma experiência leve e contínua.

## Destaques Visuais:

Interface colorida inspirada no tema Pokémon
Respostas estilizadas com HTML dinâmico

## Endpoints disponíveis
Método	Endpoint	Descrição
GET	/pokemon/{name}	Retorna altura, peso e experiência base de um Pokémon
GET	/ask?question=	Interpreta perguntas em linguagem natural
GET	/list	Lista Pokémons salvos no banco
GET	/	Interface interativa estilo chat Pokémon

Diferenciais Técnicos
- Arquitetura modular e clara
- Interface dinâmica em HTML/CSS/JS puro (sem dependências externas)
- Histórico de conversas em tempo real
- Imagens oficiais via PokéAPI
- Banco SQLite gerado e populado automaticamente
- Logs e tratamento de erro no processo de ingestão

Autoria
Vivianne Ribeiro Fábrio
Engenheira de Software / Data Engineer
São Paulo — SP
[vivi_fabrio@hotmail.com]


Quer que eu te mostre como incluir uma **prévia visual (print da interface)** direto no topo do README, tipo uma mini “capa do projeto” do GitHub?  
Isso dá um *impacto visual forte* quando o avaliador abrir o repositório.




