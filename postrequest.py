import requests

url = 'http://www.webscrapingfordatascience.com/postform/'

# まずGETリクエストを実行　
r = requests.get(url)

#次にPOSTリクエストを実行
formdata = {
    'name': 'wadatinpo',
    'gender': 'M',
    'pizza': 'like',
    'haircolor': 'brown',
    'comment': ''
    }


r = requests.post(url,data=formdata)
print(r.text)

