
from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
import models

from api.users import user
from api.restaurant import restaurant

DEBUG = True
PORT = 8000

login_manager = LoginManager()

app = Flask(__name__, static_url_path="")

app.secret_key = 'AROEAING KHATEI'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
CORS(restaurant, origins=['http//localhost:3000'], supports_credentials=True)

app.register_blueprint(user)
app.register_blueprint(restaurant)

@app.before_request
def before_request():
	'''Connect to database before each request'''
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	###Close the database connection after each request###
	g.db.close()
	return response

app.route('/')

def index():
	return 'Heeello'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port= PORT)

