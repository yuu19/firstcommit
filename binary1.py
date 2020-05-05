#バイナリデータのスクレイピング
import requests

url = 'http://www.webscrapingfordatascience.com/files/kitten.jpg'
r = requests.get(url)

#content属性を使用することに注意する
with open('image.jpg', 'wb') as my_file:
    my_file.write(r.content)


