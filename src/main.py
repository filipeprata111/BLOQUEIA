from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot

app = Flask(__name__)

bot = ChatBot("chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///meubot.db",
    debug=True,
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Eu não entendi, por favor reformule a pergunta.",
            "maximum_similarity_threshold": 0.9
        }
    ]
)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
  try:
    dados = request.get_json()
    pergunta = dados.get("mensagem", "")
    resposta = str(bot.get_response(pergunta))
    return jsonify({"resposta": resposta})
  except Exception as e:
    return jsonify({"resposta": "Desculpe, houve um erro ao processar sua pergunta."}), 500
  

if __name__ == "__main__":
    app.run(debug=True)
