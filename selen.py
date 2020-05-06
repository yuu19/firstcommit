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

driver.get('https://ja.wikipedia.org/wiki/%E4%BB%A3%E6%95%B0%E5%B9%BE%E4%BD%95%E5%AD%A6')
time.sleep(3)

#ブラウザのスクリーンショットを撮る

driver.save_screenshot('/home/vagrant/workspace/algebra1.png')

#検索ボックスのname="q"を属性として指定して文字入力

search_box = driver.find_element_by_role("navigation")




driver.save_screenshot('/home/vagrant/workspace/takousiki.png')

#検索文字を送信

search_box.submit()
time.sleep(2)

#検索結果のスクショを撮る
serch_ref = driver.find_element_by_ref("nofollow")
driver.save_screenshot('/home/vagrant/workspace/ref.jpg')

#終了する

driver.quit()

