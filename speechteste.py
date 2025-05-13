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

        # Executa programas com base na fala
        if "navegador" in frase.lower():
            os.system("start chrome")
        if "github" in frase.lower():
            os.system("start github")

    except sr.UnknownValueError:
        frase = "Não entendi"
        print(frase)

    # Escreve a frase (ou "Não entendi") no arquivo .txt
    with open("meuarquivo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)

    import os
    print("Salvando arquivo em:", os.getcwd())

    return frase

# Executa a função
ouvir_microfone()