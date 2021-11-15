#Curso #22 Global

from flask import Flask  # se importa flask para asi poder usare
from flask import render_template  # para poder Ejecutar el templade html
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import g

from flask import url_for
from flask import redirect

from flask_wtf.csrf import CSRFProtect
import forms
import json


app = Flask(__name__)  # Aqui se puede dar una ruta espesifica si esta en otra carpeta
app.secret_key = 'my_secret_key'

csrf = CSRFProtect(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    print("Before Request")
    print(request.endpoint)

    g.test = 'test1'

    #if 'username' not in session:
        #print("El usuario necesita login!")


@app.after_request  #decorador para terminar la funcion
def after_request(response):
    print(g.test)
    return response


@app.route('/', methods=['GET', 'POST'])  # metodos para obtener los datos
def index():
    print("Index")
    print(g.test)

    custome_cookie = request.cookies.get('custome_cookies', 'Undefinido')
    print(custome_cookie)
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():  # Busca la lista para asi poder ver las validar
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario")

    if 'username' in session:
        username = session['username']
        print(username)

    title = "Index"
    return render_template('index.html', title=title, form=comment_form)


@app.route('/logout')#se dirige a la funcion
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)

        session['username'] = login_form.username.data
    return render_template('login.html', form=login_form)


@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Peter')
    return response


'''@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)'''


if __name__ == '__main__':  #
    app.run(debug=True, port=8001)