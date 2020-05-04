import requests
from bs4 import BeautifulSoup
url = 'http://abehiroshi.la.coocan.jp/'
r = requests.get(url)
print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)
print(r.request.url)
print (r.text)



