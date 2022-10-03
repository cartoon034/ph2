from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    try:

        time.sleep(1)

        print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz')

        username = browser.find_element(By.NAME, 'username')
        username.send_keys('pp100200')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('password')
        password.submit()

        print("[{}] Login !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(1)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Phone_number_2 = 1000000011
        m = 0
        for i in range(1,4):

            browser.get('https://s-u-p.zabbet168.com/th/user/list')

            time.sleep(2)

            Add_user = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[3]/div/div[1]/div/button')
            browser.execute_script("arguments[0].click();", Add_user)

            Phone_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[1]/div[2]/input')
            Phone_number.send_keys(Phone_number_2)

            First_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
            First_name.send_keys('test')

            Last_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
            Last_name.send_keys(i)

            User_group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/div/div[2]').click()

            User_group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/div/div[3]/ul/li[10]').click()

            Affiliate_Group1 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[1]').click()

            Affiliate_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/div/div[3]/ul/li[3]').click()

            Commission_Group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[1]').click()

            Commission_Group2 = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[6]').click()

            Bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/button[2]').click()

            Bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/ul/li[18]').click()


            Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[8]/div[2]/input')
            Account_name.send_keys('test the system')

            Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[9]/div[2]/input')
            Account_number.send_keys(Phone_number_2)

            Password = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[10]/div[2]/input')
            Password.send_keys('password01')

            Remark = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[11]/div[2]/div/textarea')
            Remark.send_keys('test the system')

            time.sleep(2)

            Save = browser.find_element(By.XPATH, '//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[2]/button[1]').click()

            time.sleep(2)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            Phone_number_2 = Phone_number_2 + 1

            m = m + 1
            print('[{}] Click ! => {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), m))

        time.sleep(2)

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
