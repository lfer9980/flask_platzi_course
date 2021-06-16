import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.Certificate('/home/lfer9980/development/platzi/curso_flask/cloud_keys/vivid-willow-317004-3ac2314984b5.json')
firebase_admin.initialize_app(credential)

#nueva instancia de servicio firestore
db = firestore.client()

# implementando los metodos que usaremos en firestore

#con este metodo obtendremos lo que tengamos en la coleccion de usuarios
def get_users():
	return db.collection('users').get()

#
def get_to_dos(user_id):
	return db.collection('users').\
	document(user_id).\
	collection('todos').get()