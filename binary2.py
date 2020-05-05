#ファイルの内容全体がメモリに一度に格納されると容量が圧迫されるためストリーミング処理を行う
import requests

url = 'http://www.webscrapingfordatascience.com/files/kitten.jpg'

#レスポンス内でストリーミング処理を実行
r = requests.get(url, stream=True)
#r.raw r.iter_lines, r.iter_contentが使えるようになる


#r.iter_contentを使うことでバイナリデータに対してコンテンツ全体を業ごとに反復処理
with open('image.jpg', 'wb') as my_file:
    for byte_chunk in r.iter_content(chunk_size=4096):
        my_file.write(byte_chunk)



