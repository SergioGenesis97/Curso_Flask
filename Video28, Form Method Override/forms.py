#Curso #28 Form Method Override

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import validators
from models import User
import email_validator


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe de estar vacio')


class CommentForm(Form):
  username = TextField('Username',
    [
      validators.Required(message = 'El username es requerido'),
      validators.length(min=4, max=50, message='Ingrese un username valido')
    ])
  email = EmailField('Email',
    [
      validators.Required(message = 'El email es requerido'),
      validators.Email(message = 'Ingrese un email valido'),
      validators.length(min=4, max=50, message='Ingrese un email valido')
    ])

  comment = TextField('Comment')
  honeypot = TextField('', [length_honeypot])


class LoginForm(Form):
  username = StringField('Username',
    [
      validators.Required(message='El username es requerido'),
      validators.length(min=4, max=25, message="Ingresa un usuario valido!")
    ])
  password = PasswordField('Password', [validators.Required(message='El password es requerido')])


class CreateForm(Form):
  username = TextField('Username',
      [
        validators.Required(message = 'El username es requerido'),
        validators.length(min=4, max=50, message='Ingrese un username valido')
      ])
  email = EmailField('Email',
      [
        validators.Required(message = 'El email es requerido'),
        validators.Email(message = 'Ingrese un email valido'),
        validators.length(min=4, max=50, message='Ingrese un email valido')
      ])
  password = PasswordField('Password',
      [
        validators.Required(message='El password es requerido')
      ])

  def validate_username(form, field):
    username = field.data
    user = User.query.filter_by(username = username).first()

    if user is not None:
      raise validators.ValidationError('El usuario ya existe!')