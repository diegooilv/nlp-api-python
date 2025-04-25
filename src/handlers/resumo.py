from langdetect import detect
from flask import Blueprint, request, jsonify
from src.model_loader import get_resumidor

resumo_blueprint = Blueprint('resumo', __name__)

@resumo_blueprint.route('/', methods=['POST'])
def resumir_texto():
    texto = request.json.get('texto')

    try:
        idioma = detect(texto)
        if idioma != 'pt':
            return jsonify({'erro': 'O texto não está em português'}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro ao detectar o idioma'}), 500

    modelo = get_resumidor()

    resultado = modelo(texto, max_length=100, min_length=30, do_sample=False)

    return jsonify({'resumo': resultado[0]['summary_text']})
