from flask import Flask
from flask_bootstrap import Bootstrap
#traemos de __init__ la clase Config
from app.config import Config 
#para registrar los blueprints
from .auth import auth
from flask_login import LoginManager
from .models import UserModel


login_handler = LoginManager()
#definimos la ruta donde presentaremos el login
login_handler.login_view = 'auth.login'

@login_handler.user_loader
def load_user(username):
	return UserModel.query(username)



def create_app():
	app = Flask(__name__)
	#la instancia de bootstrap recibe una app de flask
	bootstrap = Bootstrap(app)
	#configurando LLAVE para session
	app.config.from_object(Config)
	#cargando el login manager
	login_handler.init_app(app)
	#registrando el blueprint
	app.register_blueprint(auth)
	return app 