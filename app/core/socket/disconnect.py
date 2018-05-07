from flask_socketio import *


class SocketDisconnect:
    def __init__(self, socket):

        @socket.on('disconnect')
        def socket_disconnect():
            print('socket disconnected!')
