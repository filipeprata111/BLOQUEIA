import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///meubot.db",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Desculpe, não entendi. Pode reformular a pergunta?",
            "maximum_similarity_threshold": 0.9
        }
    ]
)

trainer = ListTrainer(bot)

diretorio_dados = os.path.join(os.path.dirname(__file__), "..", "dados")
diretorio_dados = os.path.abspath(diretorio_dados)

if not os.path.exists(diretorio_dados):
    print(f"❌ A pasta '{diretorio_dados}' nao existe.")
    exit()

# Percorre a pasta /dados e os ficheiros dentro das subpastas
for raiz, subpastas, arquivos in os.walk(diretorio_dados):
    for nome_arquivo in arquivos:
        caminho = os.path.join(raiz, nome_arquivo)

        # Garante que só tenta abrir ficheiros .txt
        if not nome_arquivo.endswith(".txt"):
            print(f"⚠️ Ignorado (não é .txt): {nome_arquivo}")
            continue

        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
            if linhas:
                print(f"📄 Treinando com: {nome_arquivo}")
                trainer.train(linhas)

print("✅ Bot treinado com sucesso.")
