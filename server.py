import socket
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8000))
server_socket.listen(1)
(client_socket, client_address) = server_socket.accept()
while True:
    print ("client_connected [" + client_address[0] + "]")
    client_command = client_socket.recv(1024).decode()
    print(client_command)