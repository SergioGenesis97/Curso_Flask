#Curso #11 Formularios

from flask import Flask  # se importa flask para asi poder usare
from flask import render_template  # para poder Ejecutar el templade html

import forms

app = Flask(__name__)  # Aqui se puede dar una ruta espesifica si esta en otra carpeta


@app.route('/')  # queremos obetener el name
def index():
    comment_form = forms.CommentForm()
    title = "Curso Flask"
    return render_template('index.html', title=title, form=comment_form)


if __name__ == '__main__':  #
    app.run(debug=False, port=8002)