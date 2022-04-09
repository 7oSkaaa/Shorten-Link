from os import link
from requests import api
from Services.link_shorten import shortenLink
from Helpers.colors import bcolors
from Services.API import get_api_key
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def saveToFile(fileName, mode, data):
    with open(f'{fileName}', mode) as file:
        file.write(data + '\n')


def main():
    # Get URL that we want to shorten
    url = input(f'{bcolors.OKYELLOW}Enter Your URL: ')
    
    # Get API Key of the user
    Api_Key = get_api_key()
    
    # Make Shorten Link
    shorten_url = shortenLink(url, Api_Key)
    
    # Save the links to the file
    saveToFile('URLs.txt','w', shorten_url)
    saveToFile('URLs.txt','a', url)
    
    
if __name__ == "__main__":
    main()