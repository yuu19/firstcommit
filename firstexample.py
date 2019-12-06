import requests
url = 'https://www.youtube.com/watch?v=KMZF4gXc8OQ&t=1397s'
r = requests.get(url)
print(r.status_code)
print(r.reason)
print(r.headers)
print(r.request)
print(r.request.headers)
print(r.request.url)


