import socket
client_socket = socket.socket()
client_socket.connect(("192.168.56.1", 8000)) #or enter ip of server
while True:
    client_command = input("command: ")
    client_socket.send(client_command.encode())
