from flask import Flask
from flask_bootstrap import Bootstrap

#traemos de __init__ la clase Config
from app.config import Config 

def create_app():
	app = Flask(__name__)
	#la instancia de bootstrap recibe una app de flask
	bootstrap = Bootstrap(app)
	#configurando LLAVE para session
	app.config.from_object(Config)

	return app 