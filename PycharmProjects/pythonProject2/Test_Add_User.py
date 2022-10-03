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
from random import randint

import random
import datetime
import time
import sys


if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    # รหัสผ่านแอดมิน
    usernameadmin       = ('admin000033')
    passwordadmin       = ('pp100200')

    # username
    user_name           = ('na100200')

    # เบอร์โทรศัพท์
    telephone_number_1  = ('0000091111')
    telephone_number_2  = ('0000092222')

    # รหัสผ่าน
    pass_word_1         = ('nazza246')
    pass_word_2         = ('password999')
    # เลขที่บัญชี
    Bank_Account_number_1 = ('0000092222')
    Bank_Account_number_2 = ('0000091111')

    # ใส่จำนวนเงิน
    user_keys_money     = 100
    keys_reduce_credit  = -999999999

    # URL เว็บที่จะเทส
    web_admin           = ('https://s-u-p.zagent.dev/th')
    web_user            = ('https://lobby.zcompany.dev/login')

    # เข้าเว็บหลังบ้าน
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

    # ออกเว็บหลังบ้าน
    def logout_admin():

        time.sleep(1)

        browser.get(web_admin)

        print('[{}] logout admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        profileadmin = browser.find_element(By.XPATH,
                                            '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/button/i')
        browser.execute_script("arguments[0].click();", profileadmin)

        time.sleep(2)

        logoutadmin = browser.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div/header/div/div[2]/div[6]/ul/a[2]')
        browser.execute_script("arguments[0].click();", logoutadmin)

        try:
            time.sleep(2)

            username = browser.find_element(By.NAME, 'username')
            username.send_keys('admin000033')

            print('[{}] logout admin successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] logout admin false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # สร้างลูกค้าใหม่
    def create_user():

        time.sleep(2)

        browser.get(web_admin)

        time.sleep(2)

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Add_user = browser.find_element(By.XPATH,'//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/button')
        browser.execute_script("arguments[0].click();", Add_user)

        print('[{}] create user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[1]/div[2]/input')
        username.send_keys(user_name)

        Phone_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        Phone_number.send_keys(telephone_number_1)

        Gender = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/fieldset/div/div/div[3]').click()

        First_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[4]/div[2]/input')
        First_name.send_keys('test the')

        Last_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[5]/div[2]/input')
        Last_name.send_keys('system')

        User_group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[1]').click()

        Affiliate_Group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[7]/div[2]/div/div[1]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[7]/div[2]/div/div[3]/ul/li[1]').click()

        Commission_Group1 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[8]/div[2]/div/div[1]').click()

        Commission_Group2 = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[8]/div[2]/div/div[3]/ul/li[1]').click()
        # time.sleep(2)
        Bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[9]/div[2]/div/button[2]').click()
        Bank2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[9]/div[2]/div/ul')
        all_option = Bank2.find_elements_by_tag_name("li")
        random.choice(all_option).click()

        Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[10]/div[2]/input')
        Account_name.send_keys('test the system')

        Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[11]/div[2]/input')
        Account_number.send_keys(Bank_Account_number_1)

        Password = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[12]/div[2]/input')
        Password.send_keys(pass_word_1)

        Remark = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[1]/div[14]/div[2]/div/textarea')
        Remark.send_keys('test the system')

        time.sleep(2)

        Save = browser.find_element(By.XPATH,'//*[@id="modal-UsersInfo___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(5)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] create user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] create user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เข้าเว็บหน้าบ้าน ก่อนเปลี่ยนรหัส
    def login_user_1():

        time.sleep(1)

        print('[{}] web user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_user)

        time.sleep(3)

        login = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login user1 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys(telephone_number_1)

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys(pass_word_1)

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user1 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user1 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # ออกเว็บหน้าบ้าน
    def logout_user():

        time.sleep(1)

        browser.get(web_user)

        print('[{}] logout user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        profile1 = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

        time.sleep(1)

        logout = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[3]/div/div[2]/div[2]/button[2]/span').click()

        try:

            time.sleep(2)

            click_login = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

            print('[{}] logout user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] logout user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # สร้างรายการฝากหน้าบ้านแล้วยกเลิก
    def user_create_cancel_deposit():

        time.sleep(2)

        print('[{}] web user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_user)

        time.sleep(3)

        print('[{}] try User create deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        deposit = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/button/span').click()

        time.sleep(3)

        NoPro = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/button[2]').click()

        try:

            time.sleep(3)

            money = browser.find_element(By.ID, 'deposit-amount')
            money.send_keys(randint(1, 10000))
            money.submit()

            time.sleep(5)

            cancel = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[3]/div/div/div[3]/div/div[7]/button').click()

            print('[{}] User cancel deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] User cancel deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # แก้ไขชื่อลูกค้า
    def Edit_user():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_1)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        Edit_user2 = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Edit_user2)

        print('[{}] Edit user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Phone_number_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div[2]/input')
        Phone_number_clear.send_keys(Keys.CONTROL + "a")

        Phone_number = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div[2]/input')
        Phone_number.send_keys(telephone_number_2)

        Gender = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/fieldset/div/div/div[2]')
        Gender.click()

        First_name_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        First_name_clear.send_keys(Keys.CONTROL + "a")

        First_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        First_name.send_keys('ชื่อทดสอบ')

        # time.sleep(1)

        Last_name_clear = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/input')
        Last_name_clear.send_keys(Keys.CONTROL + "a")

        Last_name = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[5]/div[2]/input')
        Last_name.send_keys('นามสกุนทดสอบ')

        User_group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[2]').click()

        User_group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[6]/div[2]/div/div[3]/ul/li[2]').click()

        Affiliate_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[2]').click()

        Affiliate_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[7]/div[2]/div/div[3]/ul/li[2]').click()

        Commission_Group = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/div[2]').click()

        Commission_Group2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[8]/div[2]/div/div[3]/ul/li[2]').click()

        Remark1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[9]/div[2]/div/textarea')
        Remark1.send_keys(Keys.CONTROL + "a")

        Remark2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[9]/div[2]/div/textarea')
        Remark2.send_keys('ทดสอบแก้ไขผู้ใช้และเบอร์โทรศํพท์')

        Save = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]').click()

        time.sleep(2)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] Edit user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # แก้ไขชื่อลูกค้า
    def edit_password_user():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        edit_password = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", edit_password)

        time.sleep(3)

        print('[{}] Edit password !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        password1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div[2]/input')
        password1.send_keys(pass_word_2)

        confirm_password = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div/div[4]/input')
        confirm_password.send_keys(pass_word_2)

        Save2 = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button[1]').click()

        time.sleep(1)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] Edit password successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Edit password false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เข้าเว็บหน้าบ้าน หลังเปลี่ยนรหัส
    def login_user_2():

        time.sleep(1)

        print('[{}] web user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_user)

        time.sleep(3)

        login = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[1]').click()

        print('[{}] login user2 !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        username = browser.find_element(By.ID, 'login-phone')
        username.send_keys(telephone_number_2)

        password = browser.find_element(By.ID, 'login-password')
        password.send_keys(pass_word_2)

        try:

            password.submit()

            time.sleep(3)

            profile1 = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            time.sleep(1)

            profile2 = browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[7]/button').click()

            print('[{}] login user2 successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:

            print('[{}] login user2 false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เปลี่ยธนาคารแบบอนุมัติทันที
    def edit_bank_approve_now():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        edit_bank = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", edit_bank)

        time.sleep(3)

        print('[{}] edit bank approve now !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Account_name1 = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        Account_name1.send_keys(Keys.CONTROL + 'a')

        time.sleep(1)

        Account_name2 = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        Account_name2.send_keys('ทดสอบ เปลี่ยนชื่อบัญชี')

        time.sleep(1)

        Account_number1 = browser.find_element(By.XPATH, '//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
        Account_number1.send_keys(Keys.CONTROL + 'a')

        time.sleep(1)

        Account_number2 = browser.find_element(By.XPATH, '//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
        Account_number2.send_keys(Bank_Account_number_2)

        time.sleep(1)

        approve_now = browser.find_element(By.XPATH, '//*[@id="modal-UserBank___BV_modal_body_"]/form/div[2]/div/div[1]/button').click()

        time.sleep(2)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] edit bank approve now successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] edit bank approve now false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เปลี่ยนธนาคารโดยให้ api ตรวจสอบ
    def edit_bank_validate():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        edit_bank = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", edit_bank)

        time.sleep(3)

        print('[{}] edit bank validate !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Account_name = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        Account_name.send_keys('ใส่ชื่อ มั่วๆ')

        Account_number = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div[1]/div[3]/div[2]/input')
        Account_number.send_keys(Bank_Account_number_2)

        validate = browser.find_element(By.XPATH,'//*[@id="modal-UserBank___BV_modal_body_"]/form/div[2]/div/div[2]/button[1]').click()
        save = browser.find_element(By.XPATH, '//*[@id="modal-UserBank___BV_modal_body_"]/form/div[2]/div/div[2]/button[2]').click()

        time.sleep(5)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] edit bank validate successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] edit bank validate false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เพิ่มพันธมิตร
    def edit_partner():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        edit_partner = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[4]/a')
        browser.execute_script("arguments[0].click();", edit_partner)

        time.sleep(3)

        print('[{}] edit partner !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Partner1 = browser.find_element(By.XPATH,'//*[@id="modal-UserPartners___BV_modal_body_"]/form/div[1]/div[1]/div[2]/div/div[1]').click()
        Partner2 = browser.find_element(By.XPATH,'//*[@id="modal-UserPartners___BV_modal_body_"]/form/div[1]/div[1]/div[2]/div/div[3]/ul/li[2]').click()

        Remark = browser.find_element(By.XPATH,'//*[@id="modal-UserPartners___BV_modal_body_"]/form/div[1]/div[2]/div[2]/input')
        Remark.send_keys('ทดสอบผูกพันธมิตร')

        Save = browser.find_element(By.XPATH,'//*[@id="modal-UserPartners___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(5)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] edit partner successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] edit partner false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # เพิ่มเครดิต
    def Adjust_credit():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        Adjust_credit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[5]/a')
        browser.execute_script("arguments[0].click();", Adjust_credit)

        time.sleep(3)

        print('[{}] Adjust credit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        creedit = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/input')
        creedit.send_keys(user_keys_money)

        choose_file_image = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/div/input')
        choose_file_image.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\dodo.jpg')

        Remark = browser.find_element(By.XPATH,'//*[@id="modal-UserCredit___BV_modal_body_"]/form/div[1]/div[4]/div[2]/input')
        Remark.send_keys('ทดสอบเพิ่มเครดิต')

        Reviewing = browser.find_element(By.XPATH,'//*[@id="modal-UserCredit___BV_modal_body_"]/form/div[1]/div[5]/div/div/input').click()
        Save = browser.find_element(By.XPATH,'//*[@id="modal-UserCredit___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(5)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] Adjust credit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Adjust credit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # สร้างรายการฝาก
    def admin_Create_Deposit():

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        time.sleep(2)

        Edit_user = browser.find_element(By.ID, 'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.ID,'deposit-withdrawal')
        Deposit.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/input')
        Amount2.send_keys(user_keys_money)

        # time.sleep(1)

        Edit_bank1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/button').click()
        Edit_bank2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/ul/li[2]').click()

        # time.sleep(1)

        Date = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Date)
        Date.send_keys('{}'.format(datetime.datetime.now().strftime("%Y-%m-%d")))

        # time.sleep(1)

        Time = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[1]/div/div[9]/input')
        browser.execute_script("arguments[0].removeAttribute('readonly')", Time)
        Time.send_keys('{}'.format(datetime.datetime.now().strftime("%I%M%p")))
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

            print('[{}] Create Deposit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Create Deposit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # อนุมัติทันรายการฝาก
    def Deposit_reject():

        time.sleep(1)

        browser.get(web_admin)

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Withdraw = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", Withdraw)

        Search1 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/input')
        Search1.send_keys(telephone_number_2)

        time.sleep(2)

        Search2 = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[8]/button[1]')
        Search2.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        reject = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li/a[1]')
        browser.execute_script("arguments[0].click();", reject)

        print('[{}] Deposit reject !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Remark = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div[2]/input')
        Remark.send_keys('บอททดสอบยกเลิกรายการฝาก')

        time.sleep(1)

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            ok = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[1]')
            browser.execute_script("arguments[0].click();", ok)

            time.sleep(2)

            print('[{}] Deposit reject successful !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Deposit reject false !'.format(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # สร้างรายการถอน
    def admin_Create_Withdrawal():

        browser.get(web_admin)

        time.sleep(3)

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        time.sleep(2)

        Edit_user = browser.find_element(By.ID, 'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] Create Withdrawal !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Deposit = browser.find_element(By.ID,'deposit-withdrawal')
        Deposit.click()

        time.sleep(2)

        Withdrawal = browser.find_element(By.ID, 'withdrawal___BV_tab_button__')
        Withdrawal.click()

        time.sleep(1)

        Amount1 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        Amount1.send_keys(Keys.CONTROL + 'a')

        Amount2 = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
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

    # ยกเลิกรายการถอน
    def Withdraw_reject():

        time.sleep(1)

        browser.get(web_admin)

        time.sleep(2)

        Cash_System = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a')
        browser.execute_script("arguments[0].click();", Cash_System)

        time.sleep(2)

        print('[{}] Click Menu Deposit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Withdraw = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", Withdraw)

        Search1 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/input')
        Search1.send_keys(telephone_number_2)

        time.sleep(2)

        Search2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[9]/button[1]')
        Search2.click()

        print('[{}] Click Search !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        reject = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[10]/ul/li[2]/a')
        browser.execute_script("arguments[0].click();", reject)

        print('[{}] Withdraw reject !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(2)

        Remark = browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div/div/form/div/div[1]/div/div/div[2]/input')
        Remark.send_keys('บอททดสอบยกเลิกรายการถอน')

        time.sleep(1)

        Save = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/div/form/div/div[2]/button[1]')
        Save.click()

        try:

            time.sleep(2)

            ok = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
            browser.execute_script("arguments[0].click();", ok)

            time.sleep(2)

            print('[{}] Withdraw reject successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] Withdraw reject false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # แบนลูกค้า
    def status_ban():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        status_ban = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[8]/a')
        browser.execute_script("arguments[0].click();", status_ban)

        print('[{}] status ban !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Confirm_Ban = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[6]/button[1]')
        browser.execute_script("arguments[0].click();", Confirm_Ban)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] status ban successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] status ban false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # อับโหลดรูปภาพ
    def upload_image():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] upload image !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        upload_image = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[10]/a')
        upload_image.click()

        time.sleep(2)

        upload_image_file = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div[1]/div/input')
        upload_image_file.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\mumu.jfif')

        upload_image_save = browser.find_element(By.XPATH,'//*[@id="modal-UserImage___BV_modal_body_"]/form/div[1]/div[1]/div[2]/button')
        upload_image_save.click()

        time.sleep(1)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
            Ok.click()

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button')
            Close.click()

            print('[{}] upload image successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] upload image false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # ลบรูป
    def delete_image():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.XPATH, '//*[@id="filter-input"]')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID, 'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(2)

        print('[{}] upload image !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        upload_image = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[10]/a')
        upload_image.click()

        time.sleep(2)

        delete_image = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div/div/div/h4/a')
        delete_image.click()

        time.sleep(1)

        confirm_delete = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
        confirm_delete.click()

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[6]/button[1]')
            Ok.click()

            time.sleep(1)

            Close = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[2]/button')
            Close.click()

            print('[{}] upload image successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] upload image false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # ลดเครดิต
    def reduce_credit():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Search User !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        reduce_credit = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[11]/div/ul/li[5]/a')
        browser.execute_script("arguments[0].click();", reduce_credit)

        time.sleep(3)

        print('[{}] reduce credit !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        creedit = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/input')
        creedit.send_keys(Keys.CONTROL + 'a')

        time.sleep(1)

        creedit = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div[2]/input')
        creedit.send_keys(keys_reduce_credit)

        choose_file_image = browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[3]/div[2]/div/input')
        choose_file_image.send_keys('C:\\Users\\NeneAnime\\Desktop\\Windows 11\\dodo.jpg')

        Remark = browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/form/div[1]/div[4]/div[2]/input')
        Remark.send_keys('ทดสอบเพิ่มเครดิต')

        time.sleep(1)

        Reviewing = browser.find_element(By.XPATH,'//*[@id="modal-UserCredit___BV_modal_body_"]/form/div[1]/div[5]/div/div/input').click()

        time.sleep(1)
        Save = browser.find_element(By.XPATH,'//*[@id="modal-UserCredit___BV_modal_body_"]/form/div[2]/button[1]').click()

        time.sleep(5)

        try:

            time.sleep(1)

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] reduce credit successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] reduce credit false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # ลบลูกค้า
    def Delete_user():

        time.sleep(1)

        print('[{}] Web Admin !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        browser.get(web_admin)

        time.sleep(3)

        print("[{}] Click Menu Users !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        menu_user = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/a/span')
        browser.execute_script("arguments[0].click();", menu_user)

        time.sleep(2)

        menu_user2 = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a')
        browser.execute_script("arguments[0].click();", menu_user2)

        time.sleep(3)

        Search = browser.find_element(By.ID, 'filter-input')
        Search.send_keys(telephone_number_2)
        Search.submit()

        print("[{}] Delete user !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        time.sleep(1)

        Edit_user = browser.find_element(By.ID,'dropdown-right__BV_toggle_')
        browser.execute_script("arguments[0].click();", Edit_user)

        time.sleep(1)

        Delete_user_na = browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[11]/div/ul/li[9]/a')
        browser.execute_script("arguments[0].click();", Delete_user_na)

        time.sleep(1)

        print('[{}] Confirm delete user !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        Confirm_Delete_remark = browser.find_element(By.XPATH, '/html/body/div[2]/div/input[1]')
        Confirm_Delete_remark.send_keys('ทดสอบลบผู้ใช้')

        Confirm_Delete = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
        browser.execute_script("arguments[0].click();", Confirm_Delete)

        time.sleep(1)

        try:

            Ok = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]')
            Ok.click()

            print('[{}] delete user successful !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        except:
            print('[{}] delete user false !'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))



    try:

        login_admin()

        create_user()

        # login_user_1()
        #
        # user_create_cancel_deposit()
        #
        # logout_user()

        Edit_user()

        edit_password_user()

        # login_user_2()
        #
        # user_create_cancel_deposit()
        #
        # logout_user()

        edit_bank_approve_now()

        edit_partner()

        Adjust_credit()

        admin_Create_Deposit()

        Deposit_reject()

        admin_Create_Withdrawal()

        Withdraw_reject()

        status_ban()

        status_ban()

        upload_image()

        delete_image()

        reduce_credit()

        Delete_user()

        # login_user_2()

        # time.sleep(10000)

        browser.close()

        print("[{}] browser close !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    except KeyboardInterrupt:
        print("[{}] Process exit !".format((datetime.datetime.now() - datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")))
        browser.close()
        sys.exit(0)
