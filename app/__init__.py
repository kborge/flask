from flask import Flask, make_response, jsonify
from app.core import Modules
from app.core.socket import Connect
from flask_socketio import SocketIO
import app.config.config as configuration

app = Flask(__name__)
app.config.from_object(configuration)
Modules(app)
socket = SocketIO(app)
Connect(socket)


@app.errorhandler(404)
def not_found_error(data_404):
    return make_response(jsonify({"message": "Route %s" % data_404}), 404)


@app.errorhandler(403)
def forbidden_error(data_403):
    return make_response(jsonify({"message": "Route %s" % data_403}), 403)


@app.errorhandler(410)
def gone_error(data_410):
    return make_response(jsonify({"message": "Route %s" % data_410}), 410)


@app.errorhandler(500)
def internal_server_error(data_500):
    return make_response(jsonify({"message": "Route %s" % data_500}), 500)
