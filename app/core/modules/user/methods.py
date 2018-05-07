from flask import Blueprint, request, make_response, jsonify
from flask_cors import CORS, cross_origin
from app.core.modules.user.models.auth import Auth
from app.core.modules.user.models.registration import Registration
from http import HTTPStatus


method = Blueprint('user', __name__)
CORS(method)
status = HTTPStatus


@method.route('/account/auth/login', methods=['GET', 'POST'])
@cross_origin()
def auth():
    if request.method == 'POST':
        try:
            req = request.get_json() or request.form
            auth_ = Auth(email=req['email'], password=req['password'])
            return make_response(jsonify(auth_()), status.OK)
        except (ValueError, LookupError, KeyError) as error:
            return make_response(str(error), status.BAD_REQUEST)


@method.route('/account/registration', methods=['POST'])
@cross_origin()
def registration():
    try:
        req = request.args or request.form
        reg = Registration(first_name=req['first_name'], last_name=req['last_name'], email=req['email'], password=req['password'])
        return make_response(jsonify(reg()), status.OK)
    except (ValueError, LookupError, KeyError, TypeError) as error:
        return make_response(str(error), status.BAD_REQUEST)
