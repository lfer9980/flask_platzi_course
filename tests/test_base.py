from flask.wrappers import Response
from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest (TestCase):
	#este metodo, debera regresar una app de flask
	def create_app(self):
		# asi sabra flask que esta en ambiente de testing
		app.config['TESTING'] = True
		#no utilizaremos el token para cifrar forms
		#esto es porque no tenemos sesiones de usario activas
		#si queremos probar formas pedira un token que obviamente
		#no tenemos...
		app.config['WTF_CSRF_ENABLED'] = False
		return app

	def test_app_exists(self):
		self.assertIsNotNone(current_app)

	def test_app_in_test_mode(self):
		self.assertTrue(current_app.config['TESTING'])

	def test_index_redirect(self):
		response = self.client.get(url_for('index'))
		self.assertRedirects(response, url_for('hello'))
	
	def test_hello_get(self):
		response = self.client.get(url_for('hello'))
		self.assert200(response)

	def test_hello_post(self):
		fake_form = {
			'username': 'fake',
			'password': 'fake-password'
		}
		response = self.client.post(url_for('hello'), data=fake_form)
		self.assertRedirects(response, url_for('index'))

	def test_auth_blueprint_exists(self):
		self.assertIn('auth', self.app.blueprints)

	def test_auth_login_get(self):
		#para acceder a la ruta, se hace con auth.login en vez de solo login
		response = self.client.get(url_for('auth.login'))
		self.assert200(response)

	def test_auth_login_render_template(self):
		#simplemente con hacer el request es suficiente
		self.client.get(url_for('auth.login'))
		self.assertTemplateUsed('login.html')