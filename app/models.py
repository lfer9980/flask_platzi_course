#userMixin implementa todos los def que necesitamos para los
#modelos de nuestros usuarios que necesita flask_login 
from flask_login import UserMixin
from .firestore_service import get_user


#la funcion que nos asegura siempre tener user y password
class UserData():
	def __init__(self, username, password):
		self.username = username
		self.password = password


class UserModel(UserMixin):
	#constructor que hara que siempre que se cree un usuario
	#se necesite un nombre de usuario y password
	def __init__(self, user_data):
		""" 
		:param user_data: userData
		"""
		#recordemos que usaremos el username como id
		self.id = user_data.username
		self.password = user_data.password

	#el decorador indica que es un method static
	#con esto, hacemos que no reciba "self"
	@staticmethod
	def query(user_id):
		user_doc = get_user(user_id)
		user_data = UserData(
			username=user_doc.id,
			password=user_doc.to_dict()['password'])

		return UserModel(user_data)
