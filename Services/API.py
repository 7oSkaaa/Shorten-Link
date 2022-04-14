import time
import os
from Helpers.colors import bcolors
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

load_dotenv()

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def find_element(driver, by, value, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)), f'\n{bcolors.FAIL}Timeout while trying to find element...{bcolors.ENDC}\n')


def get_api_key():
    # Get the information of the user
    client_email = os.getenv('EMAIL')
    client_password = os.getenv('PASSWORD')
    driver = create_driver()
    print(f'{bcolors.HEADER}\nLogging in to get your API Key...{bcolors.ENDC}')
    driver.get('https://cutt.ly/login')
    find_element(driver, By.CSS_SELECTOR, '#email').send_keys(client_email)
    find_element(driver, By.CSS_SELECTOR, '#password').send_keys(client_password)
    find_element(driver, By.CSS_SELECTOR, '.g-recaptcha').click()
    time.sleep(2)
    if driver.current_url == 'https://cutt.ly/login':
        print(f'{bcolors.FAIL}\nlogging in failed\n{bcolors.ENDC}')
        driver.close()
        return 'Invalid API Key'
    driver.get('https://cutt.ly/edit')
    find_element(driver, By.XPATH, '/html/body/div[3]/main/section/div/div/div[3]/ul/li[1]/a').click()
    time.sleep(2)
    find_element(driver, By.XPATH, '/html/body/div[3]/main/section/div/div/div[3]/ul/div[1]/div/div/form/input[2]').click()
    time.sleep(2)
    Alert(driver).accept()
    time.sleep(8)
    api_key = find_element(driver, By.XPATH, '/html/body/div[3]/main/section/div/div/div[3]/ul/li[1]/p/span').text
    driver.close()
    print(f'\n{bcolors.OKGREEN}API Key successfuly parsing ✅\n{bcolors.ENDC}')
    return api_key.split(' ')[2]