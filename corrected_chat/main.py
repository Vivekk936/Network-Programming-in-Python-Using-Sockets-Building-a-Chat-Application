import argparse

from client import Client
from server import Server
from layout import Layout


HOST = "127.0.0.1"
PORT = 12345


def run_server():
    server = Server(HOST, PORT)
    server.start()

    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for a client...")

    layout = Layout(server, "Chat Server")
    layout.start()


def run_client():
    client = Client(HOST, PORT)

    try:
        client.connect()
    except ConnectionRefusedError:
        print("Could not connect to the server.")
        print("Start the server first with: python main.py server")
        return

    print(f"Connected to server at {HOST}:{PORT}")

    layout = Layout(client, "Chat Client")
    layout.start()


def main():
    parser = argparse.ArgumentParser(description="TCP Client-Server Chat")
    parser.add_argument(
        "role",
        choices=("server", "client"),
        help="Start the application as a server or client",
    )

    args = parser.parse_args()

    if args.role == "server":
        run_server()
    else:
        run_client()


if __name__ == "__main__":
    main()
