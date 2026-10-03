import socket


class Server:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        host = socket.gethostname()
        port = 12345

        self.socket.bind((host, port))
        self.socket.listen(1)

        self.client, address = self.socket.accept()

        print("Client connected:", address)

    def send(self, message):
        self.client.send(message.encode("utf-8"))

    def receive(self):
        message = self.client.recv(1024)
        return message.decode("utf-8")