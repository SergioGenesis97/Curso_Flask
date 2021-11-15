#Curso #17 Session

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import validators


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe de estar vacio')


class CommentForm(Form):
    username = StringField('UserName', [
        validators.Required(message='El username es requerido'),
        validators.length(min=4, max=25, message="Ingresa un usuario valido!")]
                           )
    email = EmailField('Correo electronico'#, [
        #validators.Required(message='Ingresa un mail para poder comenzar'),
        #validators.Email(message='Ingresa un mail valido')]
                       )
    comment = TextField('Comentario')
    honeypot = TextField('', [length_honeypot])


class LoginForm(Form):
    username = StringField('Username',
                           [
                               validators.Required(message='El username es requerido'),
                               validators.length(min=4, max=25, message="Ingresa un usuario valido!"),])
    password = PasswordField('Password', [validators.Required(message='El password es requerido')])