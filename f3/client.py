import socket


class Client:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        host = socket.gethostname()
        port = 12345
        self.socket.connect((host, port))

    def send(self, message):
        self.socket.send(message.encode("utf-8"))

    def receive(self):
        message = self.socket.recv(1024)
        return message.decode("utf-8")
