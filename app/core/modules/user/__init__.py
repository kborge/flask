from flask import Flask
from app.core.modules.user.methods import method as user

config = Flask(__name__)
config.register_blueprint(user)
