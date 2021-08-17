import os
import time

try:
    import requests

except ImportError:
    os.system('pip install requests')   
    os.system('clear')

banners = 0

while True:
    banner = [
        '____________________       _____       _____        ',
        '|                  |       |   |\      |   |        ',
        '|__________________|       |   | \     |   |        ',
        '       |   |               |   |  \    |   |        ',
        '       |   |               |   |   \   |   |        ',
        '       |   |               |   |    \  |   |        ',
        '       |   |               |   |     \ |   |       ',
        '       |   |               |   |      \|   |        ',
        '       |___|               |___|       |___|       ',
    ]

    for q in range(9):
        print(banner[q])

        if banners == 0:
            time.sleep(0.5)

        banners += 1

    menu = input('[1] Sms-Bomber \n[0] Exit \n>>> ')

    os.system('clear')

    if menu == '0':
        exit()
    
    elif menu == '1':
        os.system('clear')

        bomber_menu = input()

    

input()