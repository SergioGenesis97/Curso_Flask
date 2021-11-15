#Curso #6 Templates

from flask import Flask
from flask import render_template

app = Flask(__name__)

#app = Flask(__name__, template_folder = 'prueba_template') 
#para darle una carpeta en especifico

@app.route('/')
def index():
	return render_template('index.html') #recibe el nombre de la plantilla a renderizar


if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)