from os import link
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
    # Get URL that we want to shorten
    url = os.getenv('URL')
    
    # Get API Key of the user
    Api_Key = get_api_key()
    
    # Make Shorten Link
    shorten_url = shortenLink(url, Api_Key)
    
    # Save the links to the file
    saveToFile('URLs.txt','w', shorten_url)
    saveToFile('URLs.txt','a', url)
    
    
if __name__ == "__main__":
    main()