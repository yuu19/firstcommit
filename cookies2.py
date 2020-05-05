#より確実性のある方法
import requests
url = 'http://www.webscrapingfordatascience.com/cookielogin/'

#最初にpostリクエストを実行する
r = requests.post(url, data={'username': 'wadaakiko', 'password': 'osetinko'})

#Cookieの値を取得する
my_cookies = r.cookies

#秘密のページへのGETリクエストを実行する
r = requests.get(url + 'secret.php' , cookies=my_cookies)

print(r.text)

