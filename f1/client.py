import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT = 12345
s.connect((HOST_NAME,PORT))
while True:
    message=""
    while True:
        msg=s.recv(10)
        if len(msg)<=0:
            break
        message+=msg.decode('utf-8')
    if len(message)>0:
        print(message)
 