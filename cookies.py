#Cookieを設定する
import requests

url = 'http://www.webscrapingfordatascience.com/cookielogin/secret.php'

my_cookies = {'PHPSESSID': 'vts9ngu6vsisullgtdsbpr0vv2'}

r = requests.get(url, cookies=my_cookies)

print(r.text)




