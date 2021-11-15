#Curso #10 Macros

from flask import Flask
from flask import render_template

app = Flask(__name__)

#app = Flask(__name__, template_folder = 'prueba_template') 
#para darle una carpeta en especifico

@app.route('/')
def index():
	title = 'Curso flask'
	return render_template('index.html', titulo = title)


if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)