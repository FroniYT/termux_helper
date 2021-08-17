import os 

try:
    import requests

except ImportError:
    os.system('pip install requests')   
    os.system('clear')

print('hello from Froni')