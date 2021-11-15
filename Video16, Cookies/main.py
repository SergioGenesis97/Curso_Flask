#Curso #16 Galletas

from flask import Flask  # se importa flask para asi poder usare
from flask import render_template  # para poder Ejecutar el templade html
from flask import request
from flask import make_response
from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__)  # Aqui se puede dar una ruta espesifica si esta en otra carpeta
app.secret_key = 'my_secret_key'

csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])  # metodos para obtener los datos
def index():
    custome_cookie = request.cookies.get('custome_cookies', 'Undefinido')
    print(custome_cookie)
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():  # Busca la lista para asi poder ver las validar
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario")

    title = "Curso Flask"
    return render_template('index.html', title=title, form=comment_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm()
    return render_template('login.html', form=login_form)


@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Serch')
    return response

if __name__ == '__main__':  #
    app.run(debug=True, port=8001)