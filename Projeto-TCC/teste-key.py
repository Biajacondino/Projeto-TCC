import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Carrega variáveis do .env

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

try:
    models = client.models.list()
    print("✅ Sua chave está funcionando!")
    print("Modelos disponíveis:")
    for model in models.data[:5]:  # Mostra só os primeiros 5
        print("→", model.id)
except Exception as e:
    print("❌ Ocorreu um erro ao testar a chave:")
    print(e)
