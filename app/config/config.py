import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

__PROTOCOL = "http"
HOST = "127.0.0.1"
PORT = 5000
DOMAIN = "%s://codegearsolutions.com" % __PROTOCOL
BASE_URL = DOMAIN
MEDIA_URL = "/var/www/html/media"

SECRET_KEY = 'SecretKeyForSessionSigning'

DATABASE_NAME = 'flask-database'
DATABASE_PORT = 27017
JWT_SECRET_KEY = 'takestwototango'
JWT_HASH = 'HS256'
