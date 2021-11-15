#Curso #7 Templates tags

from flask import Flask
from flask import render_template

app = Flask(__name__)

#app = Flask(__name__, template_folder = 'prueba_template') 
#para darle una carpeta en especifico

@app.route('/')
def index():
	name = 'Sergio'
	return render_template('index.html', nombre = name)

@app.route('/client')
def client():
	list_nombres = ['test1', 'test2', 'test3', 'test4']
	return render_template('client.html', list = list_nombres)


if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)