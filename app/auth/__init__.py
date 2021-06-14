from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

#importamos despues de crear el blueprint
from . import views
