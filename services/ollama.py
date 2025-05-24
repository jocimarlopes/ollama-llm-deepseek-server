import requests
import json

OLLAMA_LOCAL_URL = "http://localhost:11434/api/"  # Ajuste conforme necessário

def get_payload(prompt, stream=False, model = 'mistral:7b'):
    payload = {
        "model": model,
        "prompt": 'Responda apenas em português o que os usuários irão pedir a seguir, quero que o retorno seja em HTML já formatado como markdown: {}'.format(str(prompt)),
        "stream": stream
    }
    return payload

def generate_non_streaming(payload):
    response = requests.post(OLLAMA_LOCAL_URL + 'generate', json=payload)
    res = response.json()
    return res['response'].split('</think>\n\n')[1]

def generate_streaming(payload):
    with requests.post(OLLAMA_LOCAL_URL + 'generate', json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                if '<think>' in data['response']:
                    data['response'] = data['response'].replace('<think>', '')
                print(data['response'])
                yield data["response"]

def get_models_ai():
    response = requests.get(OLLAMA_LOCAL_URL + 'tags', json={}, stream=False)
    res = response.json()
    lista = []
    for item in res['models']:
        lista.append(item['model'])
    return lista
