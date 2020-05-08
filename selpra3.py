from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#ChromeOptionでヘッドレスモードを指定

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_option)


class at_least_n_elements_found(object):

    def __init__(self, locator, n):
        self.locator = locator
        self.n = n

    def __call__(self, driver):
        #ここで何らかの処理を実行
        #条件の結果自体でFalseかそれ以外の結果を返す
        elements = driver.find_elements(*self.locator) #正規表現に注意
        if len(elements) >= self.n:
            return elements
        else:
            return False

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver.get(url)

#暗黙的待機
driver.implicitly_wait(10)

div_element = driver.find_element_by_class_name('infinite-scroll')
quotes_locator = (By.CSS_SELECTOR, ".quote:not(.decode)")

nr_quotes = 0
while True:
    #一番下までスクロールする
    #execute_script メソッドを使用すると、ロードしたページ上でjavascriptを実行できる
    driver.execute_script(
            #arguments[0]の意味がよくわかってない
            'arguments[0].scrollTop = arguments[0].scrollHeight',
            div_element)
    #少なくともnr_quotes+1個の名言を取得しようとする
    try:
        all_quotes = WebDriverWait(driver, 3).until(  #allquotesには[<selenium.webdriver.remote.webelement.WebElement (session="86d1387f3a33074f875417b3882c4c26", element="774f1266-e179-4222-ad24-972a6aea5474")>のような要素すべてからなるリストが入る(もっとまともな説明がありそう)
            at_least_n_elements_found(quotes_locator, nr_quotes + 1)
        )

    except TimeoutException as ex:
        print("...done")
        break
    
    nr_quotes = len(all_quotes)
    print("...now seeing ", nr_quotes, "quotes" )

print(len(all_quotes), 'quotes found\n')
for quote in all_quotes: #all_quotesは名言の情報?
    print(quote.text)

input('PRESS ENTER TO CLOSE THE AUTOMATED BROWSER')
driver.quit()




