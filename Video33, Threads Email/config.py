import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_SSL = False
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'sergio_cod_8@gmail.com' #aquí va el correo a 
											 #donde se enviará el 
											 #mensje de registro
	MAIL_PASSWORD = ' ' #Aquí va la password de tu correo

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False