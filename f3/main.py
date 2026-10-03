from client import Client
from server import Server
from layout import Layout


def main():

    choice = input("Enter 1 for Server or 2 for Client: ")

    if choice == "1":

        server = Server()
        server.start()

        layout = Layout(server, "Server")
        layout.start()

    elif choice == "2":

        client = Client()
        client.connect()

        layout = Layout(client, "Client")
        layout.start()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()