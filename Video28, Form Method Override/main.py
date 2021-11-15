#Curso #28 Form Method Override

from flask import Flask  # se importa flask para asi poder usare
from flask import render_template  # para poder Ejecutar el templade html
from flask import request
from flask import make_response
from flask import session
from flask import flash
from flask import g

from config import DevelopmentConfig

from models import db
from models import User

from flask import url_for
from flask import redirect

from flask_wtf.csrf import CSRFProtect
import forms
import json


app = Flask(__name__)  # Aqui se puede dar una ruta espesifica si esta en otra carpeta
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    print("Before Request")
    print(request.endpoint)

    '''if 'username' not in session and request.endpoint in ['comment']:
        return redirect( url_for('login') )

    elif 'username' in session and request.endpoint in ['login', 'create']:
        return redirect( url_for('index') )'''


@app.after_request  #decorador para terminar la funcion
def after_request(response):
    return response


@app.route('/', methods=['GET', 'POST'])  # metodos para obtener los datos
def index():
    print("Index")

    title = "Index"
    return render_template('index.html', title=title)


@app.route('/comment', methods=['GET', 'POST'])  # metodos para obtener los datos
def comment():
    print("Comment")

    custome_cookie = request.cookies.get('custome_cookies', 'Undefinido')
    
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

    title = "Comment"
    return render_template('comment.html', title=title, form=comment_form)


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
        password = login_form.password.data


        user = User.query.filter_by(username = username).first()
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] = username
            return redirect( url_for('index') )

        else:
            error_message = 'Usuario o Contraseña incorrectos'
            flash(error_message)

        session['username'] = login_form.username.data
    return render_template('login.html', form=login_form)


@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Peter')
    return response


@app.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():

        user = User( create_form.username.data,
                     create_form.password.data,
                     create_form.email.data )

        db.session.add(user)
        db.session.commit()#Escribe en la db

        success_message = 'Usuario Registrado en la Base de Datos'
        flash(success_message)

    return render_template('create.html', form = create_form)


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8001)