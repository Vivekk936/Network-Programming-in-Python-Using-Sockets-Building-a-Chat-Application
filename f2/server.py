import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
port=12345
s.bind((HOST_NAME,port))
s.listen(4)
client,address=s.accept()
while True:
    message=input("server: ")
    client.send(bytes(message,'utf-8'))
    message1=client.recv(50)
    print("Client:"+message1.decode('utf-8'))
 