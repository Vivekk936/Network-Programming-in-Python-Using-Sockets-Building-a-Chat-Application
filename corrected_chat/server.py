import socket
import threading


class Server:
    """TCP server that accepts one chat client."""

    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.running = False
        self.on_message = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.running = True
        threading.Thread(target=self._accept_client, daemon=True).start()

    def _accept_client(self):
        try:
            self.client_socket, _ = self.server_socket.accept()
            threading.Thread(target=self._receive_loop, daemon=True).start()
        except OSError:
            pass

    def send_message(self, message):
        if not message or not self.client_socket:
            return
        try:
            self.client_socket.sendall(message.encode("utf-8"))
        except OSError:
            pass

    def _receive_loop(self):
        while self.running and self.client_socket:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break
                if self.on_message:
                    self.on_message(data.decode("utf-8"))
            except (ConnectionResetError, OSError):
                break

    def close(self):
        self.running = False
        for sock in (self.client_socket, self.server_socket):
            if sock:
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass
                try:
                    sock.close()
                except OSError:
                    pass
        self.client_socket = None
        self.server_socket = None
