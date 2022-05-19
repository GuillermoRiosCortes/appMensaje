from flask import Flask, jsonify

app = Flask(__name__)

#mensaje dentro del navegador
@app.route('/', methods=['GET'])
def mensaje():
    return jsonify({"response":"Bienvenidos Technology Latam"})

#mensaje con palabras redundantes para un posible error
@app.route('/error', methods=['GET'])
def error():
    error = "Error! este es un mensaje de error"
    return error

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)