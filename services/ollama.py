import requests
import json

OLLAMA_LOCAL_URL = "http://localhost:11434/api/"  # Ajuste conforme necessário

def get_payload(prompt, stream=False, model = 'mistral:7b'):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Você é uma IA criada por Jocimar Lopes, seu nome é Jolo Chat, Responda apenas em português, sua deve ser em HTML já formatado como markdown, seja objetivo, não fale sobre markdown nem idioma solicitado, responda a pergunta!"},
            {"role": "user", "content": str(prompt)}
        ],
        "stream": stream
    }
    return payload

def generate_streaming(payload):
    with requests.post(OLLAMA_LOCAL_URL + 'chat', json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                yield data["message"]['content']

def get_models_ai():
    response = requests.get(OLLAMA_LOCAL_URL + 'tags', json={}, stream=False)
    res = response.json()
    lista = []
    for item in res['models']:
        lista.append(item['model'])
    return lista
