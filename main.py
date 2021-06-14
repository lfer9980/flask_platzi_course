from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#la instancia de bootstrap recibe una app de flask
bootstrap = Bootstrap(app)

#configurando LLAVE para session
app.config['SECRET_KEY'] = 'SUPER SECRETO'

to_dos = ['to-do 1', 'to-do 2', 'to-do 3']

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


@app.route('/hello')
def hello():
    #obtenemos la cookie a través del metodo get
    user_ip = session.get('user_ip')

    #diccionario para pasar muchas variables al template de una
    context = {
        'user_ip': user_ip,
        'to_dos': to_dos,
    }
    #los dos ** expanden el diccionario 
    # context para acceder mas facil en el html
    return render_template('hello.html', **context)

