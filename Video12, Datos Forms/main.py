#Curso #12 Datos Forms

from flask import Flask  # se importa flask para asi poder usare
from flask import render_template  # para poder Ejecutar el templade html
from flask import request

import forms

app = Flask(__name__)  # Aqui se puede dar una ruta espesifica si esta en otra carpeta


@app.route('/', methods=['GET', 'POST'])  # metodos para obtener los datos
def index():
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST':
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)

    title = "Curso Flask"
    return render_template('index.html', title=title, form=comment_form)


if __name__ == '__main__':  #
    app.run(debug=False, port=8003)