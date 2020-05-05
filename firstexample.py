import requests
url = 'https://www.youtube.com/watch?v=KMZF4gXc8OQ&t=1397s'
r = requests.get(url)
print(r.status_code) #HTTPステータスコード
print(r.reason) #ステータスメッセージ　
print(r.headers) #ヘッダー
print(r.request) #リクエスト情報
print(r.request.headers) #HTTPリクエストヘッダー
print(r.text) #コンテンツ



