from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
#para importar los fields del form, los traemos directamente de wtforms
from wtforms.fields import StringField, PasswordField
#de aqui nos traemos el boton de submit
from wtforms.fields.simple import SubmitField
#validador de datos de wtf
from wtforms.validators import DataRequired

app = Flask(__name__)
#la instancia de bootstrap recibe una app de flask
bootstrap = Bootstrap(app)

#configurando LLAVE para session
app.config['SECRET_KEY'] = 'SUPER SECRETO'

to_dos = ['to-do 1', 'to-do 2', 'to-do 3']

class loginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

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

    #creamos un objeto/instancia para enviar el form al html en el context
    login_form = loginForm()

    #diccionario para pasar muchas variables al template de una
    context = {
        'user_ip': user_ip,
        'to_dos': to_dos,
        'login_form': login_form,
    }
    #los dos ** expanden el diccionario 
    # context para acceder mas facil en el html
    return render_template('hello.html', **context)

