import os
from requests import api
from Services.link_shorten import shortenLink
from Helpers.colors import bcolors
from Services.API import get_api_key
from dotenv import load_dotenv

load_dotenv()

def saveToFile(fileName, mode, data):
    with open(f'{fileName}', mode) as file:
        file.write(data + '\n')


def main():
    
    if 'URL' not in os.environ or 'EMAIL' not in os.environ or 'PASSWORD' not in os.environ:
        print(f'{bcolors.OKRED}Missing Environment vairables{bcolors.ENDC}')
    
    # Get API Key of the user
    Api_Key = get_api_key()
    
    # Make Shorten Link
    shorten_url = shortenLink(Api_Key)
    
    # Save the links to the file
    saveToFile('URLs.txt','w', shorten_url)
    saveToFile('URLs.txt','a', os.getenv('URL'))
    
    
if __name__ == "__main__":
    main()