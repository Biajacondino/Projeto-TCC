import os
from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcrever', methods=['POST'])
def transcrever():
    if 'audio' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['audio']
    filename = secure_filename(file.filename)
    path = os.path.join("temp_audio", filename)

    os.makedirs("temp_audio", exist_ok=True)
    file.save(path)

    try:
        with open(path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="pt",
                response_format="json"
            )
        return jsonify({"text": transcript.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(path)

if __name__ == '__main__':
    app.run(debug=True)