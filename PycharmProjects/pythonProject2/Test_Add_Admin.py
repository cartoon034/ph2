from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import random
import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/iamCarTooN/Downloads/chromedriver.exe")
    browser.maximize_window()

    try:

        # time.sleep(15)

        print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://admin.zabtech.xyz/')

        username = browser.find_element(By.NAME, 'username')
        username.send_keys('admin000010')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('password')
        password.submit()

        print("[{}] Login !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        menu_admin = browser.find_element(By.XPATH, '//*[@id="side-menu"]/li[12]/a/span')
        browser.execute_script("arguments[0].click();", menu_admin)

        print("[{}] Click Menu User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)


    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
