from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_number import random_number_num_generator
from random_username.generate import generate_username
from random_phone import random_phone_num_generator
from selenium.webdriver.support.select import Select



import random
import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/iamCarTooN/Downloads/chromedriver.exe")
    browser.maximize_window()

    try:
        print("[{}] Process start!".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://oca.staging.rcmkt.dev/#/login')

        time.sleep(1)

        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'username')))
        txt_username = browser.find_element(By.NAME, 'username')
        txt_username.clear()


        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'username')))
        txt_username = browser.find_element(By.NAME, 'username')
        txt_username.send_keys('test00005')


        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'password')))
        txt_password = browser.find_element(By.NAME, 'password')
        txt_password.clear()


        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'password')))
        txt_password = browser.find_element(By.NAME, 'password')
        txt_password.send_keys('password')



        # WebDriverWait(browser,60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[4]/button')))
        # login = browser.execute_script(By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[4]/button')
        # login.click()

        browser.find_element_by_class_name("BTN_SIGN_IN").click()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)

