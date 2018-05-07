from flask_socketio import *


class SocketConnect:
    def __init__(self, socket):

        @socket.on('connect')
        def connect():
            emit('connect', {'message': 'successfully connected!'})
            print('socket connected!')
