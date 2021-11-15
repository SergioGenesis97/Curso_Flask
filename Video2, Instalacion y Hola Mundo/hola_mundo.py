#Curso #2 Hola mundo e instalacion

from flask import Flask

app = Flask(__name__) #Nuevo obeto

@app.route('/') #Decorador
def index():
	return 'Hola Mundo' #Funcion 

app.run(host="127.0.0.1", port=9566) #Ejecuta el servidor 