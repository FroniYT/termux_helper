import os

#настройки программы
versino_helpers = '1'
error = 0
apdate_log = '0'
logs = 0
get_log = ''

#bruteforce
passworld = ''


def main():
    import os
    global error


    #утсновка библиотек
    def download():
        os.system('apt update')
        os.system('apt upgrade -y')
        os.system('pip install requests')
        os.system('pip install colorama')
        os.system('clear')

    download()
        

    def caston_design():
        import colorama
        import time
        
        os.system('clear')
        print('------------------        -----')
        print('|                |        |   |')
        print('------------------        |   |')
        print('      |    |              |   |')
        print('      |    |              |   |')
        print('      |    |              |   |')
        print('      |    |              |   |-----------')
        print('      |    |              |   |      |   |')
        print('      |    |              |   |      |   |')
        print('      |    |              |   |      |   |')
        print('      |    |              |   |      |   |')
        print('      |    |              |   |      |   |')
        print('      |____|              |___|      |___|')
    #Страшная чать кода
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

    #это для бета юзеров
    def bruteforce():
        global passworld


        print('bruteforce BETA')
        count = int(input('Количество подборов >>> '))
        lenght = int(input('Длина пороля >>> '))
        age = input('age >>> ')
        name = input('name >>> ')
        love_number = int(input('Любимое цисло >>> '))
        Type = input(' 1.Type \n 2.Type \n >>> ')

        if Type == '1':
            for coun in range(0, count):
                passworld = ''
                for lengh in range(0, lenght):

                    passworld += name + age

                print('\n' + passworld)

        input()


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
                    bomber = input(' 1.b0mb3r \n 2.bomber 3000 \n 3.FSbomber \n >>> ')

                    #Crinny B0mb3r
                    if bomber == '1':
                        os.system('pip install db0mb3r -U')
                        os.system('b0mb3r')
                        os.system('clear')

                    #nn bomber
                    if bomber == '2':
                        os.system('echo bomber to update')
                        time.sleep(5)
                        os.system('clear')

                    #Fsystem88 big zalypa
                    if bomber == '3':
                        os.system('git clone https://github.com/FSystem88/spymer')
                        os.system('sh ~/spymer/install.sh')
                        os.system('spymer')
                        os.system('1')

                if termux_helper == '2':
                    DDos = input(' 1.Xerxes \n 2.hakddos ')

                    if DDos == '1':
                        os.system('echo soon')

                    if DDos == '2':
                        os.system('git clone https://github.com/white-hackers/hakddos​')
                        os.system('cd hakddos')
                        os.system('chmod +x hakddos.py')
                        os.system('python hakddos.py')
                
                if termux_helper == 'admin':
                    bruteforce()


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