from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
#ChromeOptionでヘッドレスモードを指定

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')


driver = webdriver.Chrome(options=chrome_option)

url = 'http://www.webscrapingfordatascience.com/postform2/'

driver.implicitly_wait(10)
driver.get(url)

driver.find_element_by_name('name').send_keys('wadatinpo')
driver.find_element_by_css_selector('input[name="gender"][value="M"]').click()
driver.find_element_by_name('pizza').click()
driver.find_element_by_name('salad').click()
Select(driver.find_element_by_name('haircolor')).select_by_value('black')
driver.find_element_by_name('comments').send_keys(
        ['First line', Keys.ENTER, 'Second line'])

input('Press ENTER to submit the form')


driver.find_element_by_tag_name('form').submit()
input('Press Enter to close the automated browser')
driver.quit()

driver.quit()


