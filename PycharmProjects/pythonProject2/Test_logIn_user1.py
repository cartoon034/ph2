from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from random import randint

import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    try:

        print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://zabtech.xyz/')

        LogIn = browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div/div[2]/div/button[1]').click()

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys('0825169264')

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys('pp100200')
        password.submit()

        print("[{}] logIn !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/button/span').click()

        time.sleep(2)

        NoPro = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/button[2]').click()

        time.sleep(3)

        money = browser.find_element(By.ID, 'deposit-amount')
        money.send_keys(randint(1,100))
        money.submit()

        print("[{}] deposit NoPro !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(30)

        cancel = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/div/div[4]/button').click()

        print("[{}] cancel deposit !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        user_profile = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[7]/button').click()

        time.sleep(1)

        Logout = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]').click()

        print("[{}] Logout !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(10)

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
