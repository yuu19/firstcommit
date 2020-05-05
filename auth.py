#基本認証を使用してリクエストを実行する
import requests
url = 'http://www.webscrapingfordatascience.com/authentication/'

r = requests.get(url, auth=('myusername', 'mypassword'))

print(r.text)
print(r.request.headers)

