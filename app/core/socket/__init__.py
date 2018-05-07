from app.core.socket.connect import SocketConnect
from app.core.socket.disconnect import SocketDisconnect
from app.core.socket.chat import SocketChat
from app.core.socket.room import SocketRoom


class Connect:
    def __init__(self, socket):
        SocketConnect(socket)
        SocketDisconnect(socket)
        SocketChat(socket)
        SocketRoom(socket)