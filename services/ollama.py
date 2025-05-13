import requests
import json

OLLAMA_LOCAL_URL = "http://localhost:11434/api/generate"  # Ajuste conforme necessário

def get_payload(prompt, stream=False):
    payload = {
        "model": "deepseek-r1",
        "prompt": '{}'.format(str(prompt)),
        "stream": stream
    }
    return payload

def generate_non_streaming(payload):
    response = requests.post(OLLAMA_LOCAL_URL, json=payload)
    res = response.json()
    return res['response'].split('</think>\n\n')[1]

def generate_streaming(payload):
    with requests.post(OLLAMA_LOCAL_URL, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                if '<think>' in data['response']:
                    data['response'] = data['response'].replace('<think>', '')
                print(data['response'])
                yield data["response"]