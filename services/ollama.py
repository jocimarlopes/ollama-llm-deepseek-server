import requests
import json
import base64
#  https://e63e-143-0-229-90.ngrok-free.app
OLLAMA_LOCAL_URL = "http://localhost:11434/api/"  # Ajuste conforme necessário

def get_payload(prompt, stream=False, model = 'mistral:7b'):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Você é uma IA criada por Jocimar Lopes, seu nome é Jolo Chat, Responda apenas em português, seja objetivo, responda o que for perguntado!"},
            {"role": "user", "content": str(prompt)}
        ],
        "stream": stream
    }
    return payload

def generate_streaming(payload):
    response = ''
    with requests.post(OLLAMA_LOCAL_URL + 'chat', json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                response = response + str(data['message']['content'])
                yield data["message"]['content']
    print('AI Response: ', response)
    print('=' * 15)

def get_models_ai():
    response = requests.get(OLLAMA_LOCAL_URL + 'tags', json={}, stream=False)
    res = response.json()
    lista = []
    for item in res['models']:
        lista.append(item['model'])
    return lista

# Função para enviar imagem ao modelo Llava via API do Ollama
def send_image_to_llava(image_path, prompt, model='llava:7b', stream=False):
    """
    Envia uma imagem junto com um prompt para o modelo Llava via API local do Ollama.
    """
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode("utf-8")
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": stream,
        "images": [image_base64]
    }

    with requests.post(OLLAMA_LOCAL_URL + 'chat', json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                yield data["message"]['content']
