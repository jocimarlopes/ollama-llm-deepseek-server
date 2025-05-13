from flask import Flask, request, jsonify, render_template, Response
import requests
import json

app = Flask(__name__, static_url_path='/', static_folder='templates', template_folder='templates')

OLLAMA_LOCAL_URL = "http://localhost:11434/api/generate"  # Ajuste conforme necessário

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    dados = {
        "model": "deepseek-r1",  # Altere para o modelo que você está usando
        "prompt": "{}".format(str(request.json.get("prompt"))),
        "stream": False
    }
    print('\nInit Request to LLM DeepSeek-R1')
    print(dados, '<- data to send')
    print('Sending...')
    resposta = requests.post(OLLAMA_LOCAL_URL, json=dados)
    res = resposta.json()
    print(res['response'].split('</think>\n\n')[1], '<- response \n')
    return jsonify(res['response'].split('</think>\n\n')[1])

@app.route('/stream', methods=['POST'])
def stream():
    user_prompt = request.json.get("prompt", "")
    payload = {
        "model": "deepseek-r1",
        "prompt": '{}'.format(str(user_prompt)),
        "stream": True
    }
    def generate():
        with requests.post(OLLAMA_LOCAL_URL, json=payload, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    data = json.loads(line.decode('utf-8'))
                    print(data, '<- data')
                    if '<think>' in data['response']:
                        data['response'] = data['response'].replace('<think>', '')
                    print(data['response'])
                    yield data["response"]
    return Response(generate(), content_type="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # Go to http://localhost:5000/ 