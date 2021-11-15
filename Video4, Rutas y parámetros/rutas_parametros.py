#Curso #4 Rutas y parametros

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo'

@app.route('/saluda')
def saluda():
	return 'Otro Mensaje'


#http://127.0.0.1:9566/params?params1=Sergio_Rosas
@app.route('/params')
def params():
	param = request.args.get('params1', 'No contiene el parametro')
	return 'El parametro es: {}'.format(param)

if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)