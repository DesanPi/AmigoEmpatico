from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configura tu clave API de OpenAI desde una variable de entorno
openai.api_key = os.getenv('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')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({"error": "El campo 'prompt' es obligatorio"}), 400

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Reemplaza con el nombre de tu modelo personalizado
        prompt=prompt,
        max_tokens=50
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
