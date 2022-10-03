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

    try:

        time.sleep(1)

        print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get('https://s-u-p.zabtech.xyz/')

        time.sleep(1)

        username = browser.find_element(By.NAME, 'username')
        username.send_keys('admin000022')

        password = browser.find_element(By.NAME, 'password')
        password.send_keys('9v~C3V[CEf&HDcY^')
        password.submit()

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Menu_Cash_System = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Menu_Cash_System)

        time.sleep(2)

        Menu_Transfer = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Menu_Transfer)

        time.sleep(2)

        print("[{}] Click Menu Transfer !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Amount_1 = 1

        def Create_Transfer_Bank_1():

            time.sleep(2)

            Withdrawal_Bank1 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div[2]/div/ul/li[1]').click()

            time.sleep(1)

            Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_1)

            Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอททำรายการโอนไปถอน 1')

            try:

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(2)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(1)

                print('[{}] Create Transfer 1 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Transfer 1 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        def Create_Transfer_Bank_2():

            time.sleep(2)

            Withdrawal_Bank1 = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div[2]/div/ul/li[2]').click()

            time.sleep(1)

            Amount = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_1)

            Remark = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอททำรายการโอนไปถอน 2')

            try:

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(2)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(1)

                print('[{}] Create Transfer 2 successful !'.format(
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Transfer 2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        def Create_Transfer_Bank_Deposit_Saving():

            time.sleep(2)

            Transfer_Saving = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[1]/ul/li[2]').click()

            time.sleep(1)

            Withdrawal_Bank1 = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/ul/li').click()

            Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_1)

            Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอททำรายการฝากโอนไปพัก')

            try:

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(2)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(1)

                print('[{}] Create Deposit Saving successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Deposit Saving false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        def Create_Transfer_Bank_Saving():

            time.sleep(2)

            Withdrawal_Bank1 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/button').click()
            Withdrawal_Bank2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/ul/li').click()

            time.sleep(1)

            Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div[2]/input')
            Amount.send_keys(Amount_1)

            Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/input')
            Remark.send_keys('บอททำรายการถอนโอนไปพัก')

            try:

                Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/div/button[1]')
                Save.click()

                time.sleep(1)

                Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(2)

                print('[{}] Create Saving successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Saving false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        bank_1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_1)

        Create_Transfer_Bank_1()

        Amount_1 = Amount_1 + 1

        bank_1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_1)

        Create_Transfer_Bank_2()

        Amount_1 = Amount_1 + 1

        bank_1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_1)

        Create_Transfer_Bank_Deposit_Saving()

        Amount_1 = Amount_1 + 1

        bank_2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_2)

        Create_Transfer_Bank_1()

        Amount_1 = Amount_1 + 1

        bank_2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_2)

        Create_Transfer_Bank_2()

        Amount_1 = Amount_1 + 1

        bank_2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_2)

        Create_Transfer_Bank_Deposit_Saving()

        Amount_1 = Amount_1 + 1

        bank_3 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_3)

        Create_Transfer_Bank_Saving()

        Amount_1 = Amount_1 + 1

        bank_4 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div')
        browser.execute_script("arguments[0].click();", bank_4)

        Create_Transfer_Bank_Saving()

        Amount_1 = Amount_1 + 1

        bank_5 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/div/div')
        browser.execute_script("arguments[0].click();", bank_5)

        Create_Transfer_Bank_1()

        Amount_1 = Amount_1 + 1

        bank_5 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div[2]/div/div/div/div')
        browser.execute_script("arguments[0].click();", bank_5)

        Create_Transfer_Bank_2()

        Amount_1 = Amount_1 + 1


        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)