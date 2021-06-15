from flask_wtf.form import FlaskForm
from app.forms import loginForm
from flask import session, flash, redirect, render_template
from flask.helpers import url_for
#nota: se hace un bug si ponemos app en vez de "."
#teoria: la app no tiene auth, pero la raiz si...
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
	login_form = loginForm()
	context = {
		'login_form': login_form
	}

	#validamos la forma si nos hacen un POST
	if login_form.validate_on_submit():
		#como el username es una instancia de un stringField, por lo cual debe agregarse .data
		username = login_form.username.data
		session['username'] = username
		flash('nombre de usuario registrado con exito!')
		return redirect( url_for('index') )

	return render_template('login.html',**context) 

