import whisper

modelo = whisper.load_model("base")

resposta = modelo.transcribe("Gravando2.m4a")

print(resposta['text'])