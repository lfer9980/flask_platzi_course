from app.forms import loginForm
#nota: se hace un bug si ponemos app en vez de "."
#teoria: la app no tiene auth, pero la raiz si...
from . import auth

from flask import render_template

@auth.route('/login')
def login():

	context = {
		'login_form': loginForm(),
	}

	return render_template('login.html',**context)

