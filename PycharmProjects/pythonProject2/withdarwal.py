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

    #รหัสผ่านแอดมิน
    usernameadmin    = ('admin000033')
    passwordadmin    = ('pp100200')

    #รหัสผ่านผู้ใช้
    telephone_number = ["0825169264", "0943725983", "0000078000"]
    pass_word        = ('pp100200')
    Bank_Account_number = ('')

    #ใส่จำนวนเงิน
    user_keys_money  = 500

    web_admin        = ('https://s-u-p.zabtech.xyz/')
    web_user         = ('https://zabtech.xyz/')

    def login_admin():

        time.sleep(1)

        browser.get(web_admin)

        time.sleep(2)

        print("[{}] Login Web Admin !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.NAME, 'username')
        username.send_keys(usernameadmin)

        password = browser.find_element(By.NAME, 'password')
        password.send_keys(passwordadmin)

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button').click()

            print('[{}] login user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def logout_admin():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] logout admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        profileadmin = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button/i')
        browser.execute_script("arguments[0].click();", profileadmin)

        time.sleep(2)

        logoutadmin = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/ul/a[2]')
        browser.execute_script("arguments[0].click();", logoutadmin)

        try:
            time.sleep(2)

            username = browser.find_element(By.NAME, 'username')
            username.send_keys('admin000033')

            print('[{}] logout admin successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] logout admin false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def Create_Withdrawal():

        for x in telephone_number:

            browser.get(web_admin)

            time.sleep(3)

            menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
            browser.execute_script("arguments[0].click();", menu_user)

            time.sleep(2)

            menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
            browser.execute_script("arguments[0].click();", menu_user2)

            print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            time.sleep(3)

            Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
            Search.send_keys(x)
            Search.submit()

            time.sleep(2)

            Edit_user = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/button')
            browser.execute_script("arguments[0].click();", Edit_user)

            time.sleep(2)

            print('[{}] Create Withdrawal !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            Deposit = browser.find_element(By.XPATH, '//*[@id="dropdown-right"]/ul/li[6]/a')
            Deposit.click()

            time.sleep(2)

            Withdrawal = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[1]/ul/li[2]')
            Withdrawal.click()

            time.sleep(1)

            Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
            Amount1.send_keys(Keys.CONTROL + 'a')

            Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
            Amount2.send_keys(user_keys_money)

            Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[5]/input')
            Remark_Deposit.send_keys('ทดสอบถอน')

            time.sleep(1)

            Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/button[1]')
            Save_Deposit.click()

            time.sleep(1)

            try:

                time.sleep(1)

                Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
                browser.execute_script("arguments[0].click();", Close)

                time.sleep(2)

                print('[{}] Create Withdrawal successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except:
                print('[{}] Create Withdrawal false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


    try:

        login_admin()

        Create_Withdrawal()

        # browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format(
            (datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)