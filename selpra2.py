import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#ChromeOptionでヘッドレスモードを指定

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')


driver = webdriver.Chrome(options=chrome_option)

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver.get(url)

quote_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".quote:not(.decode)") #ページの要素を選択するメソッドを第一引数、実際の値を第二引数に取る
            )
        )

for quote in quote_elements:
    print(quote.text)


