import requests
from bs4 import BeautifulSoup
url = 'http://abehiroshi.la.coocan.jp/'
r = requests.get(url)
<<<<<<< HEAD
print(r.status_code) #HTTPステータスコード
print(r.reason) #ステータスメッセージ　
print(r.headers) #ヘッダー
print(r.request) #リクエスト情報
print(r.request.headers) #HTTPリクエストヘッダー
print(r.text) #コンテンツ
=======
print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)
print(r.request.url)
print (r.text)
>>>>>>> 37a8aef1cfc22dc68339c78ea2ec4ab49ea685cf



