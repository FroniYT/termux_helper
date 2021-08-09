import socket
server_socket = socket.socket()
server_socket.bind(("192.168.56.1", 8000))
server_socket.listen(1)
(client_socket, client_address) = server_socket.accept()
while True:
    client_command = client_socket.recv(1024).decode()
    print(client_command)
