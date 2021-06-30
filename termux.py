import socket
#from tkinter import *

#client.send(chat.encode('utf-8'))


#Connect
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('10.80.68.86', 4783))

client.send(input().encode('utf-8'))
