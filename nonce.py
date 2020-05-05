import requests

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

my_session = requests.Session()

my_cookies = {
        'nonce': '1402',
        'PHPSESSID': '3q9r4ipsa7sndcotqifvn9co86'
        }

r = requests.get(url + 'quotes.php', params={'p': '0'})

print(r.text)

