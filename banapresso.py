from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://banapresso.com/store"
driver.get(url)
target_store = """//*[@id="contents"]/article/div/section[1]/div/div[1]/div[1]/div[2]/ul/li[2]/a"""
driver.find_element(By.XPATH, target_store).click()
store_dict = {}

for x in range(1,11):
    x = x % 6
    try:
        driver.find_element(By.XPATH, f"""//*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/ul/li[{x}]""").click()
        time.sleep(1)
        for y in range(1,11):
            store = driver.find_element(By.XPATH, f"""//*[@id="contents"]/article/div/section[1]/div/div[1]/div[2]/ul/li[{y}]/a/span[2]""").text
            store_dict[store.split('\n')[1]] = store.split('\n')[2]
           
    except Exception as e:
        driver.find_element(By.XPATH, f"""//*[@id="contents"]/article/div/section[1]/div/div[1]/div[3]/span/a""").click()
        
pd.DataFrame(store_dict.items(), columns=['점포명', '주소'])