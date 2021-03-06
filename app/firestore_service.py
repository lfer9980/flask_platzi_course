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

def get_user(user_id):
	return db.collection('users').document(user_id).get()

def put_user(user_data):
	user_ref = db.collection('users').document(user_data.username)
	user_ref.set({ 'password': user_data.password })

def get_to_dos(user_id):
	return db.collection('users').\
	document(user_id).\
	collection('todos').get()

def put_to_dos(user_id, description):
	todos_collection_ref = db.collection('users').document(user_id).collection('todos')
	todos_collection_ref.add({'description': description, 'done': False})

def delete_todo(user_id, todo_id):
	todo_ref = get_todo_ref(user_id,todo_id)
	todo_ref.delete()

def update_todo(user_id, todo_id, done):
	todo_done = not bool(done)
	todo_ref = get_todo_ref(user_id, todo_id)
	todo_ref.update({'done': todo_done})

#para no repetir codigo y obtener la referencia rapido al todo
def get_todo_ref(user_id, todo_id):
	return db.document('users/{}/todos/{}'.format(user_id, todo_id))