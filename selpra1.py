#ブラウザがJavaScriptを実行して名言の取得と表示をするにはわずかに時間がかかるので待機をしなければならないことに注意
from selenium import webdriver

#ChromeOptionでヘッドレスモードを指定    
chrome_option = webdriver.ChromeOptions() 
chrome_option.add_argument('--headless')                             
chrome_option.add_argument('--disable-gpu')            


#WebDriverをオプションを設定して起動         
driver = webdriver.Chrome(options=chrome_option)    

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'


#暗黙的待機の設定
driver.implicitly_wait(10)

driver.get(url)

for quote in driver.find_elements_by_class_name('quote'):
    print(quote.text)

input('PRESS ENTER TO CLOSE THIS SESSION')
driver.quit()


