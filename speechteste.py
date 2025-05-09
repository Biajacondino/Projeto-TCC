import speech_recognition as sr
import os

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga algo: ")
        
        audio = microfone.listen(source)

    try: 
        frase = microfone.recognize_google(audio, language= 'pt-BR')
        print("Você disse: " + frase)
        if "navegador" in frase:
          os.system("start Chrome.exe")
        if "Github" in frase:
          os.system("start Github.exe")

    except sr.UnkownValueError:
        print ("Não entendi")

    return frase

ouvir_microfone()