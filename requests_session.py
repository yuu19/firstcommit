#requests.Sessionを用いることでCookieの自動処理を行い、簡潔にコードを書くことができる
import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

my_session = requests.Session()

r = my_session.get(url)
r = my_session.post(url, params={'p':'login'}, data={'username': 'wadatinpo', 'password': 'osetinko'})
r = my_session.get(url, params={'p': 'protected'})

print(r.text)


