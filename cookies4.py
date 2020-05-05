#複雑な場合に対応する
#ログイン後にセッションIDが変更されている場合

import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

#最初に通常のGETリクエストを実行する
r = requests.get(url)

#この時点でcookieを設定する必要がある
my_cookies = r.cookies
print(my_cookies)

#次にPOSTリクエストを実行する(リダイレクトをされないようにする)
#?p=loginパラメーターを設定する必要がある
#この時点で取得したcookieをリクエストに用いる
r = requests.post(url, params={'p': 'login'},
        data={'username': 'dummy', 'password': '1234'},
        allow_redirects=False, cookies=my_cookies)


#Cookieを再度更新する必要がある
#PHPSESSIDが変更されていることに注意
my_cookies = r.cookies
print(my_cookies)


#Cookieを用いて秘密のページへのGETリクエストを実行する
#Cookieの値が変更されていることに注意する
r = requests.get(url, params={'p': 'protected'}, cookies=my_cookies)

print(r.text)


