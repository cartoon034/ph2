from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import random
import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    time.sleep(1)

    print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    username_tiktok    = ('sdsadsa@fdsfsd.com')
    password_tiktok    = ('dsad13213')

    web_tiktok_login        = ('https://www.tiktok.com/login/phone-or-email/email')
    web_tiktok_live         = ('')

    def login_tiktok():

        time.sleep(1)

        browser.get(web_tiktok_login)

        time.sleep(3)

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.NAME, 'username')
        username.send_keys(username_tiktok)

        password = browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input')
        password.send_keys(password_tiktok)
        password.submit()

        try:

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


    login_tiktok()