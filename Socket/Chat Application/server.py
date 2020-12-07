import socket
import select

HEADER = 10
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((SERVER, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}
