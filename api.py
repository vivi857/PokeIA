
from fastapi import FastAPI
from agent import get_pokemon_info, ask_agent
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    return {"info": get_pokemon_info(name)}



@app.get("/ask", response_class=PlainTextResponse)
def ask(question: str):
    resposta = ask_agent(question)
    return resposta



@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>PokeIA ⚡</title>
            <style>
                body {
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(180deg, #ffcb05 0%, #fff 100%);
                    text-align: center;
                    padding: 40px;
                }
                h1 {
                    color: #e3350d;
                    text-shadow: 1px 1px 2px #00000020;
                }
                #chat-box {
                    background: white;
                    width: 70%%;
                    margin: 40px auto;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
                    text-align: left;
                    max-height: 500px;
                    overflow-y: auto;
                }
                .user {
                    background: #dbeafe;
                    padding: 10px 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                    text-align: right;
                    color: #1e3a8a;
                    font-weight: 500;
                }
                .bot {
                    background: #fff8dc;
                    padding: 10px 15px;
                    border-radius: 10px;
                    margin: 10px 0;
                    text-align: left;
                    color: #92400e;
                    font-weight: 500;
                }
                img {
                    margin-top: 10px;
                    width: 100px;
                    border-radius: 10px;
                    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
                }
                #input-area {
                    margin-top: 30px;
                }
                input[type=text] {
                    width: 60%%;
                    padding: 10px;
                    border-radius: 10px;
                    border: 1px solid #ccc;
                    font-size: 16px;
                }
                button {
                    margin-left: 10px;
                    padding: 10px 20px;
                    border: none;
                    background: #3b4cca;
                    color: white;
                    font-weight: bold;
                    border-radius: 10px;
                    cursor: pointer;
                    transition: 0.2s;
                }
                button:hover { background: #2a2a8c; }
                footer {
                    margin-top: 50px;
                    color: #444;
                    font-size: 13px;
                }
            </style>
        </head>
        <body>
            <h1>⚡ PokeIA — Chat Pokémon</h1>
            <div id="chat-box">
                <div class="bot">🧠 Olá treinadora! Me pergunte algo sobre um Pokémon!</div>
            </div>
            <div id="input-area">
                <input id="question" type="text" placeholder="Ex: Qual é o peso do Pikachu?" required>
                <button onclick="askQuestion()">Perguntar</button>
            </div>
            <footer>Desenvolvido por Vivianne Ribeiro Fábrio 💡</footer>

            <script>
                async function askQuestion() {
                    const question = document.getElementById("question").value;
                    const chatBox = document.getElementById("chat-box");

                    if (!question.trim()) return;

                    // adiciona pergunta no chat
                    const userMsg = document.createElement("div");
                    userMsg.className = "user";
                    userMsg.textContent = question;
                    chatBox.appendChild(userMsg);
                    document.getElementById("question").value = "";

                    // scroll automático
                    chatBox.scrollTop = chatBox.scrollHeight;

                    // adiciona indicador de "pensando"
                    const botMsg = document.createElement("div");
                    botMsg.className = "bot";
                    botMsg.textContent = "⏳ Consultando dados...";
                    chatBox.appendChild(botMsg);
                    chatBox.scrollTop = chatBox.scrollHeight;

                    try {
                        const res = await fetch(`/ask?question=${encodeURIComponent(question)}`);
                        const text = await res.text();

                        // substitui texto
                        botMsg.innerHTML = "⚡ " + text.replace(/\\n/g, "<br>");

                        // tenta detectar o nome do Pokémon e exibir imagem
                        const match = text.match(/Pok[eé]mon\\s(\\w+)/i);
                        if (match && match[1]) {
                            const name = match[1].toLowerCase();
                            const img = document.createElement("img");
                            img.src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${name}.png`;
                            img.onerror = () => img.remove();
                            botMsg.appendChild(img);
                        }

                    } catch (err) {
                        botMsg.textContent = "⚠️ Erro ao obter resposta.";
                    }

                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            </script>
        </body>
    </html>
    """
