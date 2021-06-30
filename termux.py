import socket
from tkinter import *
from tkinter import messagebox
import requests
import os

#client.send(chat.encode('utf-8'))
chot_message = ''


def bulder_windows():
    pass    





#main opchin

def start_button():
    user_name = os.getlogin()

    response = requests.get("http://jsonip.com/").json()

    user_port = user_token.get()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('127.0.0.1', int(user_port)))



    def chat():


        def close_chat():
            chat_user.destroy()

        def send_message_server():

            message_server = chot_message.get()
            
            client.send(message_server.encode('utf-8'))

        global chot_message

        chat_user = Toplevel(port)
        chat_user.geometry('300x150')
        chat_user['bg'] = 'black'
        chat_user.title('chat')

        #frame
        chat_frame = Frame(chat_user, bg='black', width = 300)
        chat_frame.pack(fill="both", side="top", expand=True)

        #input fields
        chot_message = Entry(chat_user, bg='black', fg='green')
        chot_message.place(x=10, y=10, height=30, width=280)

        #chat button
        chat_button = Button(chat_user, bg='black', fg='green', text='send message',command=send_message_server)
        chat_button.place(x=10, y=100, height=40, width=130)

        close_button = Button(chat_user, bg='black', fg='green', text='close chat', command=close_chat)
        close_button.place(x=150, y=100, height=40, width=140)


    while True:
    
        #Connect

        error = 0
        

        #main design
        main_form = Toplevel(port)

        port.withdraw()
        
        main_form['bg'] = 'black'

        main_form.title(f'Ilision.Rat [Buld:beta] [User:{user_name}] [Port:{user_port}]')

        main_form.resizable(False,False)

        main_form.geometry('800x350')


        #mein frame
        main_frame = Frame(main_form, bg='black', width = 800)
        main_frame.pack(fill="both", side="top", expand=True)

        #button main

        button_main = Button(main_frame, bg='black', fg='green', text='[Log]', command=bulder_windows)
        button_main.place(x=3, y=323)


        #function select
        function_select = Toplevel(main_form)
        function_select['bg'] = 'black'
        function_select.geometry('200x350')
        function_select.title('')
        function_select.resizable(False,False)

        function_frame = Frame(function_select, bg='black', width = 200)
        function_frame.pack(fill="both", side="top", expand=True)

        #Function
        chat_button = Button(function_select, bg='black', fg='green', text='Chat', command=chat)
        chat_button.place(x=10, y=10, width=185)



        mainloop()



def exit_button():
    exit()



#design_port_frame

port = Tk()
port['bg'] = 'black'
port.geometry('200x200')
port.resizable(False,False)
port.title('')




#Frame_port_form

port_frame = Frame(port, bg='black')
port_frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

#Button_port_form
button_port = Button(port_frame, bg='black', fg='green', text='Exit', command=exit_button)
button_port.place(width=120, height=35, x=10, y=105)

button_port_start = Button(port_frame, bg='black', fg='green', text='start', command=start_button)
button_port_start.place(width=120, height=35, x=10, y=50)


#text_port form
user_token = Entry(port_frame, bg='black', fg='green')
user_token.pack()


mainloop()

