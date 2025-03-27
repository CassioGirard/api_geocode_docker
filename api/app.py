from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint para geocodificação reversa
@app.route('/get_address', methods=['GET'])
def get_address():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({"error": "Parâmetros 'lat' e 'lon' são obrigatórios."}), 400
    
    # Monta a URL de consulta para o Nominatim (usando o nome do serviço definido no compose)
    nominatim_url = f"http://nominatim:8080/reverse?format=json&lat={lat}&lon={lon}"
    
    try:
        response = requests.get(nominatim_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Erro ao consultar o Nominatim", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
