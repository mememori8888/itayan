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
#ランダム数の作成
randomC = random.uniform(10,15)


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
driver.implicitly_wait(10)


# #市区町村
# citys = driver.find_elements(By.XPATH,'//*[@id="id_city"]/option[*]')
# city_count = len(citys)
# print(city_count)
# zoom_out = driver.find_element(By.XPATH,'//*[@id="mapCanvas"]/div/div[3]/div[12]/div/div[2]/div/button[2]')
# for i in range(0,4,1):
#     zoom_out.click()
#     time.sleep(2)

# # 10秒間、要素が表示されるまで待つ
# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="mapCanvas"]/div/div[3]/div[1]/div[2]/div/div[3]/div[5]'))
# )

for i in range(2,50,1):
  for c in range(2,50,1):
      print(i)
      print(c)
      store_names = []

      driver.get(url)
      time.sleep(randomC)
      #北海道を指定
      area_select = driver.find_element(By.XPATH,f'//*[@id="id_state"]/option[{i}]')
      area_select_text = area_select.text
      print(area_select_text)
      area_select.click()
      city_select_btn = driver.find_element(By.ID,'id_city')
      city_select_btn.click()
      try:
          city_select = driver.find_element(By.XPATH,f'/html/body/div/div/div[2]/div[2]/div/div/div[1]/div[1]/form/div/div[2]/div/div/div[1]/div[2]/select/option[{c}]')
          city_select.click()
          city_select_text = city_select.text
      except:
          break
      search_button = driver.find_element(By.XPATH,'//*[@id="jsSearchStateArea"]/div/div/div[2]/div')
      search_button.click()

      time.sleep(2)
      # ページのソースコードを取得
      html_source = driver.page_source

      # BeautifulSoupで解析
      soup = BeautifulSoup(html_source, 'html.parser')

      # インデントして整形
      # aria-label属性を持つdiv要素を検索
      div_elements = soup.find_all('div', {'aria-label': True})

      for div in div_elements:
          store_name = div.get('aria-label')
          # print(store_name) 
          store_names = [area_select_text,city_select_text,store_name]
          # 既存のCSVファイルに追記
          df = pd.DataFrame([store_names])
          print(df)
          df.to_csv("output.csv",mode = 'a',index=False,header=None,encoding='utf-8')


          





