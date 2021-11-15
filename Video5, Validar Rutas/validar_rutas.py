#Curso #5 Validar rutas

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>/')
def params(name = 'Valor default', num = 'nothing'):
	return 'El parametro es: {} {}'.format(name, num)

if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)