import socket

    
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',123))
server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode('UTF-8').lower()

        print(data)
