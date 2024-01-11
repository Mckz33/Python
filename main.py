# app.py

from flask import Flask, request, jsonify
from ementador import Ementador
from validador import validar_json

app = Flask(__name__)

@app.route('/similaridade', methods=['POST'])
def calcular_media_similaridade():
    data = request.get_json()

    if not validar_json(data):
        return jsonify({'error': 'Formato inválido. A lista deve conter exatamente 2 elementos com as chaves "Ementa" e "Conteudo".'}), 400

    ementador = Ementador()

    similaridade_ementa = ementador.calcular_similaridade(data[0]['Ementa'], data[1]['Ementa'])

    if data[0]['Conteudo'] is not None and data[1]['Conteudo'] is not None:
        similaridade_conteudo = ementador.calcular_similaridade(data[0]['Conteudo'], data[1]['Conteudo'])
        media_similaridade = (similaridade_ementa + similaridade_conteudo) / 2
    else:
        media_similaridade = similaridade_ementa

    return jsonify({'media_similaridade': media_similaridade})

if __name__ == '__main__':
    app.run(debug=True)
