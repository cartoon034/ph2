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

        menu_User = browser.find_element(By.XPATH, '//*[@id="side-menu"]/li[9]/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", menu_User)

        print("[{}] Click Menu Group !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Click_Add = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        Click_Add.click()

        print("[{}] Click Add Group !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Code = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/input')
        Code.send_keys("เทสกลุ่ม")

        Name = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[2]/input')
        Name.send_keys("เทสกลุ่ม")

        Group_Type = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div[1]/select')
        all_option = Group_Type.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        Group_Bank = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div[2]/select')
        all_option = Group_Bank.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        Min_deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/input')
        Min_deposit.send_keys(Keys.BACKSPACE)

        Min_withdraw = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[2]/input')
        Min_withdraw.send_keys(Keys.BACKSPACE)

        Min_withdraw_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[5]/div[1]/input')
        Min_withdraw_without.send_keys(Keys.BACKSPACE)

        Limit_count_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[1]/input')
        Limit_count_without.send_keys(Keys.BACKSPACE)

        Limit_amount_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[2]/input')
        Limit_amount_without.send_keys(Keys.BACKSPACE)

        time.sleep(1)

        Min_deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/input')
        Min_deposit.send_keys('1')

        Min_withdraw = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[2]/input')
        Min_withdraw.send_keys('300')

        Min_withdraw_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[5]/div[1]/input')
        Min_withdraw_without.send_keys('5000')

        Limit_count_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[1]/input')
        Limit_count_without.send_keys('10')

        Limit_amount_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[2]/input')
        Limit_amount_without.send_keys('2000000')

        Bank_Deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[8]/div[1]/select')
        all_option = Bank_Deposit.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        time.sleep(1)

        click_add_Bank = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[8]/div[2]/button')
        click_add_Bank.click()

        time.sleep(1)

        Save = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[10]/div/button[1]')
        Save.click()

        time.sleep(1)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
            Ok.click()

            print('[{}] Add Group successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Add Group false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Search = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div/div[1]/input')
        Search.send_keys('เทสกลุ่ม')

        Click_Search = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div/div[2]/button')
        Click_Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Click_Edit = browser.find_element(By.XPATH, '//*[@id="__BVID__193"]/tbody/tr/td[9]/ul/li[1]/a')
        Click_Edit.click()

        time.sleep(1)

        print('[{}] Click Edit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Code = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/input')
        Code.send_keys(Keys.CONTROL + "A")
        Code.send_keys(Keys.DELETE)

        Name = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[2]/input')
        Name.send_keys(Keys.CONTROL + "A")
        Name.send_keys(Keys.DELETE)

        Min_deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/input')
        Min_deposit.send_keys(Keys.CONTROL + "A")
        Min_deposit.send_keys(Keys.DELETE)

        Min_withdraw = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[2]/input')
        Min_withdraw.send_keys(Keys.CONTROL + "A")
        Min_withdraw.send_keys(Keys.DELETE)

        Min_withdraw_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[5]/div[1]/input')
        Min_withdraw_without.send_keys(Keys.CONTROL + "A")
        Min_withdraw_without.send_keys(Keys.DELETE)

        Limit_count_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[1]/input')
        Limit_count_without.send_keys(Keys.CONTROL + "A")
        Limit_count_without.send_keys(Keys.DELETE)

        Limit_amount_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[2]/input')
        Limit_amount_without.send_keys(Keys.CONTROL + "A")
        Limit_amount_without.send_keys(Keys.DELETE)

        Bank_Deposit_Delete = browser.find_element(By.XPATH, '//*[@id="__BVID__237"]/tbody/tr/td[4]/ul/li/a')
        Bank_Deposit_Delete.click()

        time.sleep(1)

        Code = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[1]/input')
        Code.send_keys("เทสครับ")

        Name = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div[2]/input')
        Name.send_keys("เทสครับ")

        Group_Type = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div[1]/select')
        all_option = Group_Type.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        Group_Bank = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div[2]/select')
        all_option = Group_Bank.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        Min_deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[1]/input')
        Min_deposit.send_keys('2')

        Min_withdraw = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[4]/div[2]/input')
        Min_withdraw.send_keys('200')

        Min_withdraw_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[5]/div[1]/input')
        Min_withdraw_without.send_keys('2000')

        Limit_count_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[1]/input')
        Limit_count_without.send_keys('5')

        Limit_amount_without = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[6]/div[2]/input')
        Limit_amount_without.send_keys('1000000')

        Bank_Deposit = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[8]/div[1]/select')
        all_option = Bank_Deposit.find_elements_by_tag_name("option")
        random.choice(all_option).click()

        time.sleep(1)

        click_add_Bank = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[8]/div[2]/button')
        click_add_Bank.click()

        time.sleep(1)

        Save = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[10]/div/button[1]')
        Save.click()

        time.sleep(2)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
            Ok.click()

            print('[{}] Edit Group successful!'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit Group false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Search = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div/div[1]/input')
        Search.send_keys('เทสครับ')

        Click_Search = browser.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/form/div[2]/div/div[2]/button')
        Click_Search.click()

        print('[{}] Search Group seccessful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Delete = browser.find_element(By.XPATH, '//*[@id="__BVID__278"]/tbody/tr/td[9]/ul/li[2]/a')
        Delete.click()

        time.sleep(1)

        Yes = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
        Yes.click()

        time.sleep(1)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
            Ok.click()

            print('[{}] Delete Group seccessful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Delete Group false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        print('[{}] No error !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.close()

        print('[{}] close browser !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except:
        print("[{}] problem Menu Group & error code !".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
