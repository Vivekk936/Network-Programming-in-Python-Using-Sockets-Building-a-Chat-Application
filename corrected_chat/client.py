import socket
import threading


class Client:
    """TCP client for the chat application."""

    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.on_message = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.running = True
        threading.Thread(target=self._receive_loop, daemon=True).start()

    def send_message(self, message):
        if not message or not self.socket:
            return
        self.socket.sendall(message.encode("utf-8"))

    def _receive_loop(self):
        while self.running:
            try:
                data = self.socket.recv(4096)
                if not data:
                    break
                if self.on_message:
                    self.on_message(data.decode("utf-8"))
            except (ConnectionResetError, OSError):
                break
        self.running = False

    def close(self):
        self.running = False
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            self.socket.close()
            self.socket = None
