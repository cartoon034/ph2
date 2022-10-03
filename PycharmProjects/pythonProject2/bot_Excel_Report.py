from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from random import randint

import datetime
import time
import pandas
import json

if __name__ == '__main__':
    browser = Chrome(executable_path="C:/Users/NeneAnime/Downloads/chromedriver.exe")
    browser.maximize_window()

    print("[{}] Process Start !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    browser.get('https://admin.wmbet444.com/')

    username = browser.find_element(By.NAME, '_username')
    username.send_keys('singtonumchok')

    password = browser.find_element(By.NAME, '_password')
    password.send_keys('singtonumchok')
    password.submit()

    print("[{}] Login !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    browser.get('https://admin.wmbet444.com/report/member/bet')

    Search_Date = browser.find_element(By.XPATH, '//*[@id="multiCollapseExample1"]/div/div/form/div/ul/li[6]/div/div/label')
    Search_Date.click()

    time.sleep(1)

    Search_Date = browser.find_element(By.XPATH, '//*[@id="criteria_date_dateRange"]')
    browser.execute_script("arguments[0].removeAttribute('readonly')", Search_Date)
    Search_Date.send_keys('2022-08-24 to 2022-08-25')

    time.sleep(1)

    ClickSearch = browser.find_element(By.XPATH, '//*[@id="multiCollapseExample1"]/div/div/form/div/ul/li[7]/button')
    ClickSearch.click()

    time.sleep(2)

    print("[{}] Copy !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    data = []
    m = 0
    count = browser.find_element(By.XPATH, '//*[@id="main__content"]/div[2]/div[2]/div[4]/div/div[2]/div/ul/li[6]/a').text
    for x in range(int(count)):
        Copy = browser.find_elements(By.XPATH, '//*[@id="main__content"]/div[2]/div[2]/div[3]/table/tbody/tr')
        for row in Copy:

            time.sleep(randint(1 , 2))

            q = row.find_element(By.XPATH, 'td[1]').text
            w = row.find_element(By.XPATH, 'td[2]').text
            e = row.find_element(By.XPATH, 'td[3]').text
            r = row.find_element(By.XPATH, 'td[4]').text
            t = row.find_element(By.XPATH, 'td[5]').text
            y = row.find_element(By.XPATH, 'td[6]').text
            u = row.find_element(By.XPATH, 'td[7]').text
            i = row.find_element(By.XPATH, 'td[8]').text


            data.append({"1"          :       q,
                         "2"          :       w,
                         "3"          :       e,
                         "4"          :       r,
                         "5"          :       t,
                         "6"          :       y,
                         "7"          :       u,
                         "8"          :       i})


        m = m + 1
        print('[{}] Click ! => {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), m))
        # time.sleep(1)

        browser.find_element(By.CLASS_NAME, 'next').click()

    data = json.dumps(data)
    excel = pandas.read_json(data)
    excel.to_excel('report.xlsx')
    print("[{}] ok !".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

