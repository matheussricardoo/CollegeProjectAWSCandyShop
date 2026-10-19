"""Static frontend and HTTP proxy for the candy shop API.

Academic project by Matheus Ricardo; local demonstration, not a production service.
"""
from flask import Flask, send_from_directory, jsonify, request
import requests
import os

app = Flask(__name__, static_folder='static')
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:25000')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/api/products')
def proxy_products():
    try:
        response = requests.get(f'{BACKEND_URL}/api/products', timeout=10)
        return jsonify(response.json()), response.status_code
    except (requests.RequestException, ValueError):
        return jsonify({"error": "Backend unavailable or invalid JSON response"}), 502

@app.route('/api/products/lowstock')
def proxy_products_lowstock():
    try:
        threshold = request.args.get('threshold', '10')
        response = requests.get(f'{BACKEND_URL}/api/products/lowstock?threshold={threshold}', timeout=10)
        return jsonify(response.json()), response.status_code
    except (requests.RequestException, ValueError):
        return jsonify({"error": "Backend unavailable or invalid JSON response"}), 502

@app.route('/api/orders', methods=['POST'])
def proxy_orders():
    try:
        data = request.get_json()
        response = requests.post(f'{BACKEND_URL}/api/orders', json=data, timeout=10)
        return jsonify(response.json()), response.status_code, response.status_code
    except (requests.RequestException, ValueError):
        return jsonify({"error": "Backend unavailable or invalid JSON response"}), 502

    

@app.route('/health')
def health():
    """Report 503 when the upstream API is unavailable or unhealthy."""
    try:
        response = requests.get(f'{BACKEND_URL}/health', timeout=5)
        if response.status_code == 200:
            return jsonify({"frontend": "healthy", "backend": response.json()})
    except (requests.RequestException, ValueError):
        pass
    return jsonify({"frontend": "healthy", "backend": "unhealthy"}), 503

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    print("Iniciando Frontend - Loja de Doces")
    print("Rodando na porta 8080")
    print(f"Backend configurado para: {BACKEND_URL}")
    app.run(host='0.0.0.0', port=8080, debug=False)
