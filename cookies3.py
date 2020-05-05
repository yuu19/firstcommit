#より複雑なログインのフローに対処する
#
import requests

url = 'http://www.webscrapingfordatascience.com/redirlogin/'

#初めにPOSTリクエストを実行する(リダイレクトがされないようにする)
r = requests.post(url, data={'username':'dummy', 'password':'1234'},
        allow_redirects=False)

#Cookieの値を取得する
print(r.cookies)

my_cookies = r.cookies

#Cookieを用いて秘密のページへのGETリクエストを実行する
r = requests.get(url + 'secret.php', cookies=my_cookies)

print(r.text)


