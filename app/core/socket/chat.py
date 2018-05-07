from flask_socketio import *


class SocketChat:
    def __init__(self, socket):

        @socket.on('chat')
        def room_message():
            pass
