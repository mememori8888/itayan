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
import logging
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
import datetime
#ランダム数の作成
randomC = random.uniform(15,16)


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



url = "https://www.evcharger-network.com/chg_spot_search/"

# time.sleep(randomC)
# options.add_argument(ua.random)
# すべてのCookieを削除
driver.implicitly_wait(3)

wait_text = "An error occurred."
#request数をカウント
req_count = 0

for area in range(2,50,1):
    for c in range(2,50,1):
        req_count += 1
        print(f"req数は{req_count}")
        driver.get(url)
        time.sleep(2)
        page_source = driver.page_source
        if wait_text not in driver.page_source:
            print("アクセスに成功しました。後の処理を続行します。")
        else:
            time.sleep(6)
            driver.quit()
            driver = webdriver.Chrome(options=options)
            continue
        #北海道を指定
        try:
            area_select_btn = driver.find_element(By.ID,'id_state')
            area_select_btn.click()
            # area_select = driver.find_element(By.XPATH,f'//*[@id="id_state"]/option[{area}]')
            area_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='id_state']/option[{area}]")))
            area_select.click()
            area_select_text = area_select.text

            city_select_btn = driver.find_element(By.ID,'id_city')
            city_select_btn.click()
            time.sleep(1)
            # city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
            city_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]")))
            city_select.click()
            city_select_text = city_select.text
            time.sleep(1)

            search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
            search_button.click()
            full_screen = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[7]/button')  
            full_screen.click()  
        except:
            time.sleep(3)
            area_select_btn = driver.find_element(By.ID,'id_state')
            area_select_btn.click()
            # area_select = driver.find_element(By.XPATH,f'//*[@id="id_state"]/option[{area}]')
            area_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='id_state']/option[{area}]")))
            area_select.click()
            time.sleep(1)

            area_select_text = area_select.text

            city_select_btn = driver.find_element(By.ID,'id_city')
            city_select_btn.click()
            # city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
            time.sleep(1)

            city_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]")))
            city_select.click()
            city_select_text = city_select.text
            search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
            search_button.click()
            full_screen = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[7]/button')  
            full_screen.click()  


    #要素数をカウント
        element = driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/div[*]")
        count = len(element)
        print(count)


        for i in range(1,count,1):
            print(i)
            page_source = driver.page_source
            if wait_text not in driver.page_source:
                print("アクセスに成功しました。後の処理を続行します。")
            else:
                #アクセス制限時ブラウザを再起動
                time.sleep(6)
                driver.quit()
                driver = webdriver.Chrome(options=options)
                continue
            try:
                element = driver.find_element(By.XPATH,f"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[3]/div[{i}]")
                # ここでテキスト化して、重複を避ける
                store = element.get_attribute("title")
                print(store)
                dup_df = pd.read_csv('data.csv')
                # 2番目のカラム（インデックスは1から始まる）に"北海道日産　白石店"が含まれる行を抽出
                result = dup_df[dup_df.iloc[:, 1].str.contains(store)]
                print(result)
                print(len(result))
                
                if len(result) > 0:
                    print("重複してます。")
                    continue
                else:
                    pass

                actions = ActionChains(driver)
                actions.click(element).perform()                # driver.excute_script("arguments[0].click();",element)
                print("clicked!!")
                check = element.is_displayed()
                print(check)
                if check is True:
                    pass
                else:
                    continue
            
                        # 現在の日時を取得
                now = datetime.datetime.now()
                # 指定した形式でフォーマット
                formatted_datetime = now.strftime("%m/%d/%y %H:%M")
                name = driver.find_element(By.CLASS_NAME,"info-window-name").text
                if name  == "":
                    name = "取得ミス"
                else:
                    pass
                address = driver.find_element(By.CLASS_NAME,"info-window-layout").text
                address = address.replace("\n充電場所HPはこちら（外部リンク）","")
                page_url = driver.current_url
                link_url = driver.find_element(By.CLASS_NAME,"info-window-url").get_attribute("href")
                vattery = driver.find_element(By.CLASS_NAME,"info-window-charger.info-window-ttl").text
                vattery_num = driver.find_element(By.CLASS_NAME,"info-window-charger.info-window-ttl").find_element(By.TAG_NAME,'em').text
                vattery = vattery.replace(vattery_num,"").replace("台","")
                available_time = driver.find_element(By.CLASS_NAME,"info-window-facilities-detail").text
                vattery_type = driver.find_element(By.CLASS_NAME,"info-window-charger-type-detail").text
                vattery_types = vattery_type.split('/')
                vattery_type = vattery_types[0]
                maximum_output = vattery_types[1]
                price = driver.find_element(By.CLASS_NAME,"info-window-usage-fee-detail").text
                try:
                    other = driver.find_element(By.CLASS_NAME,"info-window-other-detail").text
                except:
                    other = ""
                available = driver.find_element(By.CLASS_NAME,"info-window-charger-available").text
                in_use = driver.find_element(By.CLASS_NAME,"info-window-charger-using").text
                on_hold = driver.find_element(By.CLASS_NAME,"info-window-charger-stopping").text
                output_list = [formatted_datetime,name,address,page_url,link_url,vattery,available_time,vattery_type,maximum_output,price,other,vattery_num,available,in_use,on_hold,area_select_text,city_select_text]
                print(output_list)
                output_df = pd.DataFrame([output_list])
                print(output_df)
                output_df.to_csv('data.csv' ,mode ='a' ,index=False ,header=None ,encoding='utf-8')
                print("書き込み完了")
                #閉じる
                close = driver.find_element(By.CLASS_NAME,"gm-ui-hover-effect")
                close.click()
                # center_btn = driver.find_element(By.CLASS_NAME,'btn.white.reload')
                # center_btn.click()

                time.sleep(2)
                driver.get(url)
                area_select_btn = driver.find_element(By.ID,'id_state')
                area_select_btn.click()

                # area_select = driver.find_element(By.XPATH,f'//*[@id="id_state"]/option[{area}]')
                area_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[@id='id_state']/option[{area}]")))
                area_select.click()
                time.sleep(1)

                city_select_btn = driver.find_element(By.ID,'id_city')
                city_select_btn.click()
       
                # city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
                city_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]")))
                city_select.click()
                time.sleep(1)

                search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
                search_button.click()
                            #全画面
                full_screen = driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div[2]/div[2]/div/div[3]/div[7]/button')  
                full_screen.click()  
                req_count += 1



            except:
                # time.sleep(2)
                # driver.get(url)
                # area_select = driver.find_element(By.XPATH,f'//*[@id="id_state"]/option[{area}]')
                # area_select.click()
                # city_select_btn = driver.find_element(By.ID,'id_city')
                # city_select_btn.click()

                # city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
                # city_select.click()

                # search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
                # search_button.click()
                continue

