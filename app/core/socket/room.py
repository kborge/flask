from flask_socketio import *


class SocketRoom:
    def __init__(self, socket):

        @socket.on('join_company_channel')
        def join_company_channel():
            pass
