import selenium.webdriver

driver = selenium.webdriver.PhantomJS()
driver.get('https://techacademy.jp/')
elems = driver.find_elements_by_tag_name('img')
for e in elems:
        print(e.get_attribute('src'))
