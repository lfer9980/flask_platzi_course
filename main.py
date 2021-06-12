from flask import Flask, request

#creamos una var app que construya un objeto desde la clase
#flask y que tenga como nombre main.py o mejor dicho __name__
app = Flask(__name__)

#crearemos un decorador de python
#la app tiene una funcion llamada route
#recibe la ruta de donde buscara el archivo que correra la funcion
@app.route('/')
#creamos la primer ruta donde desplegaremos el hello world
#se hara con una funcion que retorne el hello world
#se ligara con la app para que Flask sepa a la ruta donde 
#debe ir y que tiene que desplegar....
def hello():
    user_ip = request.remote_addr
    return f'your IP address is {user_ip}'

