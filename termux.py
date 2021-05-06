import os
versino_helpers = '1'
error = 0
apdate_log = '0'
logs = 0
get_log = ''


def main():
    import os
    global error



    def download():
        os.system('pip install requests')
        os.system('pip install colorama')
        os.system('clear')
        

    def caston_design():
        import colorama

        #ужас на это нельзя смотреть(на этот код)
        print('''
+=======================+
|                       |
| coder: Froni#1540     |
|                       |
| version:1[beta]       |
|                       |                       
+=======================+          
''')

    
    def check():
        global logs
        global apdate_log
        global versino_helpers
        global error
        global get_log
 
        import requests
        get_log = requests.get('https://pastebin.com/raw/yYRiw4dm').text
        logs = requests.get('https://raw.githubusercontent.com/FroniYT/termux_helper/main/appdate.txt').text
        version = requests.get('https://pastebin.com/raw/Gwme01s2').text

        #получения версия
        if versino_helpers == version:
            error = '0'
        
        elif versino_helpers != version:
            error = '1'

        if get_log == '1':
            logs == '1'

        if get_log == '0':
            logs == '0'



    check()

    if error == '0':

        def helper():
            import os 
            global logs
            global log
            global get_log
            

            
            connect = True
            
            #вывод обновления
            if get_log == '1':
                print(logs)

            while connect:
                caston_design()


                termux_helper = input(' 1.Sms-Bomber \n 2.DDos attack Internet \n 3.Metosplite[beta] \n >>> ')

                if termux_helper == '1':
                    os.system('pip install db0mb3r -U')
                    os.system('b0mb3r')
                    os.system('clear')

                if termux_helper == '2':
                    DDos = input(' 1.Xerxes \n 2.hakddos ')

                    if DDos == '1':
                        os.system('echo soon')

                    if DDos == '2':
                        os.system('git clone https://github.com/white-hackers/hakddos​')
                        os.system('cd hakddos')
                        os.system('chmod +x hakddos.py')
                        os.system('python hakddos.py')


                if termux_helper == 'Stop':
                    connect = False

        
        helper()

        
        


    #Авто обновы
    elif error == '1':
        import time
        os.system('rm -rf dir termux_helper')
        os.system('git clone https://github.com/FroniYT/termux_helper')
        time.sleep(5)
        os.system('echo Обновления скаченно успешно перезапустите скрипт :)')







main()