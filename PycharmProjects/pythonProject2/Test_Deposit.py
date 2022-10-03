from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import datetime
import time
import sys

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # รหัสผ่านแอดมิน
    usernameadmin       = ('admin000033')
    passwordadmin       = ('pp100200')

    # รหัสผ่านผู้ใช้
    telephone_number    = ('0834980291')
    pass_word           = ('pp100200')
    Bank_Account_number = ('021101012021')

    # ใส่จำนวนเงิน
    user_keys_money     = 100

    web_admin           = ('https://s-u-p.zagent.dev/th')
    web_user            = ('https://zabtech.xyz/')


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

    # สร้างรายการฝาก
    def user_Create_Deposit_1():

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number)
        Search.submit()

        time.sleep(2)

        Edit_user = browser.find_element(By.ID, 'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit bank 3 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(user_keys_money)

        # time.sleep(1)

        Edit_bank1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
        Edit_bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[2]').click()

        # time.sleep(1)

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        # time.sleep(1)

        Time = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%I%M%p")))
        # Time.send_keys('121212')

        # time.sleep(1)

        Remark_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[13]/input')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        # time.sleep(1)

        Save_Deposit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        time.sleep(2)

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # อนุมัติทันที
    def Approve_Deposit_Bill_Numbe():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] Approve Deposit Bill Numbe !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[8]/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li[1]/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        print('[{}] Approve Deposit Bill Number !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Approve2 = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[1]/div/button')
        Approve2.click()

        Date = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%I%M%p")))
        # Time.send_keys('121212')

        time.sleep(1)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[5]/div[2]/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\koko.jpg')

        time.sleep(1)

        Note = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div/div[4]/div[2]/input')
        Note.send_keys('บอททดสอบอนุมัติทันที')

        time.sleep(1)

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(5)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
            Close.click()

            time.sleep(2)

            print('[{}] Approve Deposit Bill Number successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Bill Number false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # อัปโหลดรูปภาพ
    def Approve_Deposit_Upload_Slip():

        time.sleep(1)

        browser.get(web_admin)

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/form/div/div[8]/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Approve = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[2]')
        browser.execute_script("arguments[0].click();", Approve)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div[2]/div/div/input')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\momo.jpg')

        print('[{}] Click Approve Upload Slip !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Approve Deposit Upload Slip successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Approve Deposit Upload Slip false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # สร้างบิลโน๊ต
    def Adjust_Expense_1():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] Adjust Expense 3 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div')
        Deposit_popup.click()

        print('[{}] Adjust/Expense !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Adjust_Expense = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[1]/div/div/div[2]/button[2]')
        browser.execute_script("arguments[0].click();", Adjust_Expense)

        time.sleep(2)

        Date = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[1]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[1]/div[4]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%I%M%p")))
        # Time.send_keys('121212')

        Amount = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[2]/div[2]/input')
        Amount.send_keys(user_keys_money)

        Note = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[2]/div[4]/input')
        Note.send_keys('บอททดสอบสร้างบิลโน๊ต')

        Customer_account_no = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[3]/div[2]/input')
        Customer_account_no.send_keys(Bank_Account_number)

        Upload_Slip = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[3]/div[4]/input')
        Upload_Slip.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\jojo.jpg')

        time.sleep(1)

        credits = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[3]/div/div/form/div[4]/div/button')
        browser.execute_script("arguments[0].click();", credits)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(1)

            Adjust_Expense_Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/div/form/div[1]/div/div/div[2]/button[2]')
            browser.execute_script("arguments[0].click();", Adjust_Expense_Close)

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(1)

            print('[{}] Create Adjust/Expense successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Adjust/Expense false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # ผูกบิล
    def Bill_Match_1():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] Bill Match 3 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        Cash_System.click()

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[8]/button[1]')
        Search.click()


        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        click_Bill_Number = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[1]/div[1]').text

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div')
        browser.execute_script("arguments[0].click();", Deposit_popup)

        Search_Bank_Account = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[2]/div/form/div[1]/div[4]/input')
        Search_Bank_Account.send_keys(Bank_Account_number)

        Search_Amount = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[2]/div/form/div[2]/div[2]/input')
        Search_Amount.send_keys(user_keys_money)

        click_search = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[2]/div/form/div[4]/div[4]')
        click_search.click()

        Bill_Match = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/ul/li[2]/button')
        Bill_Match.click()

        print('[{}] Click Bill Match !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Bill_Number = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[1]')
        Bill_Number.send_keys(click_Bill_Number)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[2]')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\popo.jpg')

        Remark = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[3]')
        Remark.send_keys('บอททดสอบผูกบิล')

        Save = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/div/button[1]')
        Save.click()

        try:

            time.sleep(5)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[6]/button[1]')
            Close.click()

            time.sleep(3)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            Close.click()

            time.sleep(3)

            print('[{}] Bill Match successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Bill Match false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def user_Create_Deposit_2():

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number)
        Search.submit()

        time.sleep(2)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit bank 2 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[10]/div/ul/li[6]')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(user_keys_money)

        # time.sleep(1)

        Edit_bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
        Edit_bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[3]/a').click()

        # time.sleep(1)

        Date = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        # time.sleep(1)

        Time = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%H%M%p")))
        # Time.send_keys('121212')

        # time.sleep(1)

        Remark_Deposit = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[13]/input')
        Remark_Deposit.send_keys('ทดสอบฝากไม่มีโปรโมชั่น')

        # time.sleep(1)

        Save_Deposit = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[2]/button[1]')
        Save_Deposit.click()

        time.sleep(1)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(2)

            print('[{}] Create Deposit bank 2 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit bank 2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def Adjust_Expense_2():

        time.sleep(1)

        browser.get(web_admin)

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[2]/div')
        Deposit_popup.click()

        print('[{}] Adjust/Expense bank 2 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Adjust_Expense = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[1]/div/div/div[2]/button[2]')
        browser.execute_script("arguments[0].click();", Adjust_Expense)

        time.sleep(2)

        Date = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[1]/div[2]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        Time = browser.find_element(By.XPATH,
                                    '/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[1]/div[4]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%I%M%p")))
        # Time.send_keys('121212')

        Amount = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[2]/div[2]/input')
        Amount.send_keys(user_keys_money)

        Note = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[2]/div[4]/input')
        Note.send_keys('บอททดสอบสร้างบิลโน๊ต')

        # Customer_account_no = browser.find_element(By,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[3]/div[2]/input')
        # Customer_account_no.send_keys()

        Upload_Slip = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[3]/div[4]/input')
        Upload_Slip.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\jojo.jpg')

        time.sleep(1)

        credits = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[3]/div/div/form/div[4]/div/button')
        browser.execute_script("arguments[0].click();", credits)

        try:

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[6]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(1)

            Adjust_Expense_Close = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[1]/div/div/div[2]/button[2]')
            browser.execute_script("arguments[0].click();", Adjust_Expense_Close)

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/button')
            browser.execute_script("arguments[0].click();", Close)

            time.sleep(1)

            print('[{}] Create Adjust/Expense bank 2 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Adjust/Expense bank 2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def Bill_Match_2():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] Bill Match 2 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        Cash_System.click()

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Deposit)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[1]/div[2]/input')
        Search.send_keys(telephone_number)

        time.sleep(2)

        Search = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div/div/form/div[2]/div/button[1]')
        Search.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        click_Bill_Number = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/table/tbody/tr[1]/td[1]/div[1]').text

        time.sleep(2)

        Deposit_popup = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div')
        browser.execute_script("arguments[0].click();", Deposit_popup)

        Search_Amount = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[2]/div[2]/input')
        Search_Amount.send_keys(user_keys_money)

        click_search = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[2]/div/form/div[3]/div[4]/button')
        click_search.click()

        Bill_Match = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/ul/li[2]')
        Bill_Match.click()

        print('[{}] Click Bill Match bank 2 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Bill_Number = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[1]')
        Bill_Number.send_keys(click_Bill_Number)

        upload = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[2]')
        upload.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\popo.jpg')

        Remark = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/input[3]')
        Remark.send_keys('บอททดสอบผูกบิล')

        Save = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div[4]/div/div/div/div/table/tbody/tr[1]/td[8]/div/form/div/div/button[1]')
        Save.click()

        try:

            time.sleep(2)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Close.click()

            time.sleep(2)

            print('[{}] Bill Match bank 2 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Bill Match bank 2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    try:

        login_admin()

        user_Create_Deposit_1()

        Approve_Deposit_Upload_Slip()

        Approve_Deposit_Bill_Numbe()

        user_keys_money = user_keys_money + 100

        user_Create_Deposit_1()

        Adjust_Expense_1()

        Bill_Match_1()

        user_keys_money = user_keys_money + 100

        # user_Create_Deposit_2()
        #
        # Approve_Deposit_Upload_Slip()
        #
        # Approve_Deposit_Bill_Numbe()

        time.sleep(100000)

        # user_keys_money = user_keys_money + 100
        #
        # user_Create_Deposit_2()
        #
        # Adjust_Expense_2()
        #
        # Bill_Match_2()

        time.sleep(10000)

        logout_admin()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.close()

    except KeyboardInterrupt:
        print("[{}] Process exit!".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
