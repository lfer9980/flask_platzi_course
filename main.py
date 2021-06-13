from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

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
    #creando la cookie como metodo de response
    #                    nombre    valor
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    #obtenemos la cookie a través del metodo get
    user_ip = request.cookies.get('user_ip')

    #diccionario para pasar muchas variables al template de una
    context = {
        'user_ip': user_ip,
        'to_dos': to_dos,
    }
    #los dos ** expanden el diccionario 
    # context para acceder mas facil en el html
    return render_template('hello.html', **context)

