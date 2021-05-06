import os
versino_helpers = '1'
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

        version = requests.get('https://pastebin.com/raw/Gwme01s2').text

        if versino_helpers == version:
            error = '0'
        
        elif versino_helpers != version:
            error = '1'
    check()

    if error == '0':

        def helper():
            import os 
            termux_helper = input(' 1.Sms-Bomber \n 2.DDos attack Internet \n 3.Metosplite[beta] \n >>> ')

            if termux_helper == '1':
                os.system('pip install db0mb3r -U')
                os.system('b0mb3r')

            if termux_helper == '2':
                os.system('')


        helper()



    elif error == '1':
        os.system('rm -r dir termux_helper')
        os.system('git clone https://github.com/FroniYT/termux_helper')
        os.system('')







main()