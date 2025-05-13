import speech_recognition as sr
import os

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga algo: ")
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)

        if "navegador" in frase.lower():
            os.system("start chrome")
        if "github" in frase.lower():
            os.system("start github")

    except sr.UnknownValueError:
        frase = "Não entendi"
        print(frase)
    except Exception as e:
        frase = "Erro ao reconhecer fala"
        print("Erro inesperado:", e)

    # Caminho completo para a pasta ProjetoTCC
    documentos = os.path.join(os.environ['USERPROFILE'], 'Documents')
    destino = os.path.join(documentos, 'Github', 'Projeto-TCC')

    # Garante que a pasta existe
    os.makedirs(destino, exist_ok=True)

    caminho_arquivo = os.path.join(destino, "meuarquivo.txt")

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(frase)
        print("Arquivo salvo com sucesso em:", caminho_arquivo)
    except Exception as e:
        print("Erro ao salvar o arquivo:", e)

    return frase

# Executa a função
ouvir_microfone()