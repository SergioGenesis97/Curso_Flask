#Curso #13 Validacion Datos

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import validators


def lengt_honeypot(field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe de estar vacio')


class CommentForm(Form):
    username = StringField('username', [
        validators.Required(message='El username es requerido'),
        validators.length(min=4, max=25, message="Ingresa un usuario valido!")]
                           )
    email = EmailField('Correo electronico'#, [
        #validators.Required(message='Ingresa un mail para poder comenzar'),
        #validators.Email(message='Ingresa un mail valido')]
                       )
    comment = TextField('Comentario')
    honeypot = TextField('', [lengt_honeypot])


class LoginForm(Form):
    username = StringField('Username',
                           [
                               validators.Required(message='El username es requerido'),
                               validators.length(min=4, max=25, message="Ingresa un usuario valido!"),])
    password = PasswordField('Password', [validators.Required(message='El password es requerido')])