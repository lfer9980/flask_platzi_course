from app.models import UserData
from flask_wtf.form import FlaskForm
from app.forms import loginForm
from flask import session, flash, redirect, render_template
from flask.helpers import url_for
#nota: se hace un bug si ponemos app en vez de "."
#teoria: la app no tiene auth, pero la raiz si...
from . import auth
from app.firestore_service import get_user, put_user
from app.models import UserModel, UserData
from flask_login import login_user, login_required, logout_user, current_user
#libreria de seguridad para guardar passwords en signup
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		flash('You already logged')
		return redirect(url_for('index'))
	else:
		login_form = loginForm()
		context = {
			'login_form': login_form
		}

		#validamos la forma si nos hacen un POST
		if login_form.validate_on_submit():
			#como el username es una instancia de un stringField, por lo cual debe agregarse .data
			username = login_form.username.data
			password = login_form.password.data

			user_doc = get_user(username)

			#si hay info en el document snapshot, valida el password 
			if user_doc.to_dict() is not None:
				password_from_db = user_doc.to_dict()['password']

				if check_password_hash or password (user_doc.to_dict()['password'], password):
					# crearemos el userdata y model para mandarlo a una
					#funcion login_user de flask_login
					user_data = UserData(username, password)
					user = UserModel(user_data)
					
					#hacemos el login_user con userModel para que 
					#tenga el mixin de propiedades que necesitamos
					#para hacer login
					login_user(user)
	
					flash('Bienvenido de nuevo')
					redirect(url_for('hello'))
				else:
					flash('La información no coincide')
			else:
				flash('El usuario no existe')	
					
			return redirect( url_for('index') )
	
		return render_template('login.html',**context) 


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	signup_form=loginForm()

	context = {
		'signup_form': signup_form
	}

	if signup_form.validate_on_submit():
		username = signup_form.username.data
		password = signup_form.password.data

		user_doc = get_user(username)

		if user_doc.to_dict() is None:
			password_hash = generate_password_hash(password)
			user_data = UserData(username, password_hash)
			put_user(user_data)

			user = UserModel(user_data)
			#para hacer login en el mismo signup
			login_user(user)

			flash('Bienvenido')
			return redirect(url_for('hello'))
		else:
			flash('El usuario ya existe, logeate para entrar')
			return redirect(url_for('auth.login'))

	return render_template('signup.html', **context)



@auth.route('/logout')
#login required, porque no queremos hacer un logout de un 
#usuario que no existe
@login_required
def logout():
	logout_user()
	flash('regresa pronto')
	
	return redirect(url_for('auth.login'))