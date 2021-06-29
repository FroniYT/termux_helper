import socket   


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.0.50', 6743))

while True:

    command = input('''
    
    
''')


    if command == '/'[-1]:
        client.send('ура'.encode('utf-8'))

    client.send(command.encode('utf-8'))
