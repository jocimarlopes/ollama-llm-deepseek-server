from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import requests
import json
from services import ollama
from waitress import serve

app = Flask(__name__, static_url_path='/', static_folder='templates', template_folder='templates')
CORS(app, origins=["*"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    payload = ollama.get_payload(str(request.json.get("prompt", "")))
    res = ollama.generate_non_streaming(payload)
    return jsonify(res['response'].split('</think>\n\n')[1])

@app.route('/models', methods=['POST'])
def models():
    models = ollama.get_models_ai()
    return jsonify(models)

@app.route('/stream', methods=['POST'])
def stream():
    user_prompt = request.json.get("prompt", "")
    model = request.json.get("model", "")
    models = ollama.get_models_ai()
    if not model in models: return {}
    print('=' * 15)
    print(user_prompt)
    print('=' * 15)
    payload = ollama.get_payload(str(user_prompt), stream=True, model=model)
    return Response(ollama.generate_streaming(payload), content_type="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    serve(app, host='0.0.0.0', port=5000, threads=4)
    # Go to http://localhost:5000/ 