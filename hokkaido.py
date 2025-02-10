# seleniumの設定

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException,ElementClickInterceptedException,StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from subprocess import CREATE_NO_WINDOW
import pandas as pd
import sys
import json
import re
import os
from collections import Counter
from csv import writer
import csv
import random
import threading
import gspread
import logging
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
ua = UserAgent()
#ランダム数の作成
randomC = random.uniform(3,15)


##chormeのオプションを指定
options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'normal'
# options.page_load_strategy = 'eager'
# options.add_argument(ua.random)
driver = webdriver.Chrome(options=options)

# options.add_argument("--incognito")
# options.add_argument("--no-startup-window")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1200,1200")
# options.add_argument("--no-sandbox")
# options.add_argument("--enable-javascript")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument("--enable-webgl")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument('--disable-dev-shm-usage')#ディスクのメモリスペースを使う。DockerやGcloudのメモリ対策でよく使われる。
# options.add_argument('blink-settings=imagesEnabled=false')  # 画像の読み込みを無効化
# options.add_argument('--disable-cache')


path = os.getcwd()
CHROMEDRIVER = path + r'\chromedriver.exe'


random_wait_min = 1800
random_wait_max = 1801

url = "https://www.evcharger-network.com/chg_spot_search/"

time.sleep(randomC)
# options.add_argument(ua.random)
# すべてのCookieを削除
driver.implicitly_wait(10)
driver.get(url)
time.sleep(10)
#北海道を指定
area_select = driver.find_element(By.XPATH,'//*[@id="id_state"]/option[2]')
area_select.click()
#市区町村
citys = driver.find_elements(By.ID,'id_city')
city_count = len(citys)

# zoom_out = driver.find_element(By.XPATH,'//*[@id="mapCanvas"]/div/div[3]/div[12]/div/div[2]/div/button[2]')
# for i in range(0,4,1):
#     zoom_out.click()
#     time.sleep(2)

# # 10秒間、要素が表示されるまで待つ
# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="mapCanvas"]/div/div[3]/div[1]/div[2]/div/div[3]/div[5]'))
# )
for c in range(2,city_count,1):
    city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[1]/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
    city_select.click()
    search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
    search_button.click()


#要素数をカウント
    element = driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/div[*]")
    count = len(element)
    print(count)

    driver.get(url)
    time.sleep(2)
    #北海道を指定
    area_select = driver.find_element(By.XPATH,'//*[@id="id_state"]/option[2]')
    area_select.click()
    city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[1]/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
    city_select.click()

    search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
    search_button.click()

    for i in range(1,count,1):
        print(i)
        try:
            element = driver.find_element(By.XPATH,f"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/div[{i}]")
            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()
            print("clicked!!")
            check = element.is_displayed()
            print(check)
            if check is True:
                # element.click()
                time.sleep(2)
            else:
                continue
            name = driver.find_element(By.CLASS_NAME,"info-window-name").text
            address = driver.find_element(By.CLASS_NAME,"info-window-layout").text
            vattery = driver.find_element(By.CLASS_NAME,"info-window-charger.info-window-ttl").text
            vattery_num = driver.find_element(By.CLASS_NAME,"info-window-charger.info-window-ttl").find_element(By.TAG_NAME,'em').text
            available = driver.find_element(By.CLASS_NAME,"info-window-charger-available").text
            in_use = driver.find_element(By.CLASS_NAME,"info-window-charger-using").text
            on_hold = driver.find_element(By.CLASS_NAME,"info-window-charger-stopping").text
            output_list = [name,address,vattery,vattery_num,available,in_use,on_hold]
            print(output_list)
            output_df = pd.DataFrame([output_list])
            print(output_df)
            output_df.to_csv('output.csv' ,mode ='a' ,index=False ,header=None ,encoding='utf-8')
            #閉じる
            close = driver.find_element(By.CLASS_NAME,"gm-ui-hover-effect")
            close.click()
            # center_btn = driver.find_element(By.CLASS_NAME,'btn.white.reload')
            # center_btn.click()

            time.sleep(2)
            # area_select = driver.find_element(By.XPATH,'//*[@id="id_state"]/option[2]')
            # area_select.click()
            # search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
            # search_button.click()

        except:
            # area_select = driver.find_element(By.XPATH,'//*[@id="id_state"]/option[2]')
            # area_select.click()
            # search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
            # search_button.click()
            continue

# for param in element:
#     param.click()
#     close = driver.find_elements(By.XPATH,'//button[@aria-label="閉じる"]')
#     close.click()
#     time.sleep(5)
# element.click()
# time.sleep(30)
  # Get attribute of current active element
# attr = driver.switch_to.active_element.get_attribute("title")
# print(attr)

# /html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/div[5]
