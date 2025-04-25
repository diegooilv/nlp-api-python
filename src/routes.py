from flask import Flask
from src.handlers.resumo import resumo_blueprint
from src.handlers.pergunta import qa_blueprint

def register_routes(app: Flask):
    app.register_blueprint(resumo_blueprint, url_prefix='/resumo')
    app.register_blueprint(qa_blueprint, url_prefix='/pergunta')
