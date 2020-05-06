import time

#SeleniumWebDriverのインポート
from selenium import webdriver

#ChromeOptionでヘッドレスモードを指定

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

#WebDriverをオプションを設定して起動

driver = webdriver.Chrome(options=chrome_option)

#googleのサイトを開く
url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.get(url)

input('Press Enter to close the automated browser') 
driver.quit()

