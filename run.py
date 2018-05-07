from app import app as application
from app.config.config import HOST, PORT, DEBUG
if __name__ == "__main__":
    # context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # context.load_cert_chain('xxx.crt', 'xxx.key')
    # ssl_context=context
    application.run(host=HOST, port=PORT, threaded=True, debug=DEBUG)
