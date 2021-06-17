from flask_wtf import FlaskForm
#para importar los fields del form, los traemos directamente de wtforms
from wtforms.fields import StringField, PasswordField
#de aqui nos traemos el boton de submit
from wtforms.fields.simple import SubmitField
#validador de datos de wtf
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
	username = StringField('Nombre de usuario', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Enviar')


class TodoForm(FlaskForm):
	description = StringField('Descripción', validators=[DataRequired()])
	submit = SubmitField('Crear')