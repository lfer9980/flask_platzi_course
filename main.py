from flask import request, make_response, redirect, render_template, session
from flask.helpers import flash, url_for
from flask_bootstrap import Bootstrap
#traemos una funcionalidad de unitest que se encargara de correr todos los tests desde el dir
import unittest
from app import create_app
from app.forms import loginForm

app = create_app()

to_dos = ['to-do 1', 'to-do 2', 'to-do 3']


@app.cli.command()
def test():
    # los tests sera todo lo que encuentre unittest 
    # en la carpeta que estara en la raiz llamada tests
    tests = unittest.TestLoader().discover('tests')
    #corremos los tests con unittests
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    #la respuesta sera redigirlo a /hello y guardamos eso en una var
    response = make_response(redirect('/hello'))
    #guardando la ip en session para que sea seguro
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET'])
def hello():

    #obtenemos la cookie a través del metodo get
    user_ip = session.get('user_ip')
    #si existe ya username en session, lo obtenemos
    username = session.get('username')

    #diccionario para pasar muchas variables al template de una
    context = {
        'user_ip': user_ip,
        'to_dos': to_dos,
        'username': username
    }


    #los dos ** expanden el diccionario 
    # context para acceder mas facil en el html
    return render_template('hello.html', **context)

