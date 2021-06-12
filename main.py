from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

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
    #al return le enviamos la variable como segundo parametro
    return render_template('hello.html', user_ip= user_ip)

