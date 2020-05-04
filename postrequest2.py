import requests
from bs4 import BeautifulSoup
url = 'http://www.webscrapingfordatascience.com/postform3/'

#まずGETリクエストを実行する
r = requests.get(url)

#protecion(valueのキー)の値を取得
html_soup = BeautifulSoup(r.text, 'html.parser')
p_val = html_soup.find('input', attrs={'name':'protection'}).get('value') #attrsでname=protectionという属性を指定

#取得した値をPOSTリクエストで用いる
formdata = {
        'name': 'aan',
        'gender': 'M',
        'pizza': 'like',
        'haircolor': 'brown',
        'comments': '',
        'protection': p_val
        }

r = requests.post(url, data=formdata)

print(r.text)


