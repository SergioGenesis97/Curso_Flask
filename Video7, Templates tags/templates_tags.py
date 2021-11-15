#Curso #7 Templates tags

from flask import Flask
from flask import render_template

app = Flask(__name__)

#app = Flask(__name__, template_folder = 'prueba_template') 
#para darle una carpeta en especifico

@app.route('/user/<name>')
def user(name='Sergio'):
	age = 17
	myList = [1, 2, 3, 4, 5]
	return render_template('user.html', nombre = name, edad = age, list = myList) #recibe el nombre de la plantilla a renderizar


if __name__ == '__main__':
	app.run(debug = True, host="127.0.0.1", port=9566)