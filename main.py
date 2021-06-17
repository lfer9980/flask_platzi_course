from flask import request, make_response, redirect, render_template, session
from flask.helpers import flash, url_for
from flask_bootstrap import Bootstrap
#traemos una funcionalidad de unitest que se encargara de correr todos los tests desde el dir
import unittest

from flask_login import login_required, current_user
from app import create_app
from app.forms import *
from app.firestore_service import *

app = create_app()


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


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():

    #obtenemos la cookie a través del metodo get
    user_ip = session.get('user_ip')
    #si existe ya username en session, lo obtenemos
    username = current_user.id

    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()

    #diccionario para pasar muchas variables al template de una
    context = {
        'user_ip': user_ip,
        'to_dos': get_to_dos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form,
    }

    if todo_form.validate_on_submit():
        put_to_dos(user_id=username, description=todo_form.description.data)
        flash('Todo added successful!')

        return redirect(url_for('hello'))


    #los dos ** expanden el diccionario 
    # context para acceder mas facil en el html
    return render_template('hello.html', **context)


#esto es una ruta dinamica, cambian de acuerdo al id del todo
@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id,todo_id=todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id=user_id,todo_id=todo_id, done=done)

    return redirect(url_for('hello'))