from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
from services import (ollama, logs)
from waitress import serve

app = Flask(__name__, static_url_path='/', static_folder='templates', template_folder='templates')
CORS(app, origins=["*"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models', methods=['POST'])
def models():
    models = ollama.get_models_ai()
    return jsonify(models)

@app.route('/stream', methods=['POST'])
def stream():
    headers = request.headers
    user_agent = headers.get('User-Agent')
    ip = headers.get('X-Forwarded-For', request.remote_addr)
    image_file = request.files.get("image", None)
    print(image_file, '<- image_file')
    image_path = None
    if image_file:
        image_path = f"./tmp/{image_file.filename}"
        image_file.save(image_path)
        user_prompt = request.form.get("prompt", "")
        model = request.form.get("model", "")
    else:
        user_prompt = request.json.get("prompt", "")
        model = request.json.get("model", "")
    models = ollama.get_models_ai()
    if not model in models: return {}

    print('=' * 15)
    print('Model: ', model)
    print('IP: ', ip)
    print('User-Agent: ', user_agent)
    print('Prompt: ', user_prompt)
    logs.salvar_log(f'Generate: {model} | {ip} | {user_agent} | {user_prompt}')

    if model == "llava:7b" and image_path:
        return Response(ollama.send_image_to_llava(image_path=image_path, prompt=user_prompt), content_type="text/plain")

    payload = ollama.get_payload(str(user_prompt), stream=True, model=model)
    return Response(ollama.generate_streaming(payload), content_type="text/plain")

if __name__ == '__main__':
    logs.configurar_logger()
    # app.run(host='0.0.0.0', port=5000, debug=True)
    serve(app, host='0.0.0.0', port=5000, threads=4)
    # Go to http://localhost:5000/ 