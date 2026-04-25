from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/soma', methods=['GET'])
def soma():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        resultado = num1 + num2
        return jsonify({'resultado': resultado})
    except:
        return jsonify({'erro': 'Parâmetros inválidos'})

@app.route('/subtracao', methods=['GET'])
def subtracao():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        resultado = num1 - num2
        return jsonify({'resultado': resultado})
    except:
        return jsonify({'erro': 'Parâmetros inválidos'})

@app.route('/multiplicacao', methods=['GET'])
def multiplicacao():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        resultado = num1 * num2
        return jsonify({'resultado': resultado})
    except:
        return jsonify({'erro': 'Parâmetros inválidos'})

@app.route('/divisao', methods=['GET'])
def divisao():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return jsonify({'erro': 'Divisão por zero'})
        resultado = num1 / num2
        return jsonify({'resultado': resultado})
    except:
        return jsonify({'erro': 'Parâmetros inválidos'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
