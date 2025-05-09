import SpeechRecognition as sr

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microfone() as source:

        microfone.adjust_for_ambient_noise(source)

        print("Diga algo: ")
        
        audio = microfone.listen(source)

    try: 
        frase = microfone.recognize_google(audio, language= 'pt-BR')
        print("Você disse; " + frase)

    except sr.UnkownValueError:
        print ("Não entendi")

    return frase

ouvir_microfone()