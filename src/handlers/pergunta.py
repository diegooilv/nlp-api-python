from langdetect import detect
from flask import Blueprint, request, jsonify
from src.model_loader import get_qa_model  # Função que retorna o modelo de question-answering

qa_blueprint = Blueprint('qa', __name__)

@qa_blueprint.route('/', methods=['POST'])
def responder_pergunta():
    data = request.json
    contexto = data.get('contexto')
    pergunta = data.get('pergunta')

    if not contexto or not pergunta:
        return jsonify({'erro': 'É necessário fornecer um contexto e uma pergunta'}), 400

    try:
        idioma = detect(contexto)
        if idioma != 'pt':
            return jsonify({'erro': 'O contexto não está em português'}), 400
    except Exception as e:
        return jsonify({'erro': 'Erro ao detectar o idioma'}), 500

    modelo_qa = get_qa_model()

    try:
        resultado = modelo_qa(question=pergunta, context=contexto)
        resposta = resultado['answer']
    except Exception as e:
        return jsonify({'erro': 'Erro ao processar a pergunta'}), 500

    return jsonify({'resposta': resposta})
