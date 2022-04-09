import time
from Helpers.colors import bcolors
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
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def find_element(driver, by, value, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))


def get_api_key():
    # Get the information of the user
    client_email = input(f'{bcolors.OKBLUE}Enter your Cuttly Email: ')
    client_password = getpass(f'{bcolors.OKBLUE}Enter Your Password: ')
    driver = webdriver.Chrome()
    driver.get('https://cutt.ly/login')
    email = driver.find_element_by_xpath('//*[@id="email"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    email.send_keys(client_email)
    password.send_keys(client_password)
    login_button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/button')
    login_button.click()
    time.sleep(5)
    driver.get('https://cutt.ly/edit')
    manage_api_button = driver.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div[3]/ul/li[1]/a')
    manage_api_button.click()
    time.sleep(5)
    change_api_key_button = driver.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div[3]/ul/div[1]/div/div/form/input[2]')
    change_api_key_button.click()
    time.sleep(5)
    Alert(driver).accept()
    time.sleep(15)
    api_key = driver.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div[3]/ul/li[1]/p/span').text
    words = api_key.split(' ')
    return words[2] 