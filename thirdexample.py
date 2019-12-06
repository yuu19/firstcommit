import requests  
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/watch?v=KMZF4gXc8OQ&t=1397s'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')
#最初の<h1>タグを検索
first_h1 = html_soup.find('h1')

print(first_h1.name)
print(first_h1.contents)

print(str(first_h1))

print(first_h1.text)

print(first_h1.attrs)

print('----------CITATIONS--------------')

cites = html_soup.find_all('cite', class_ = 'citation', limit=5)
for citation in cites:
    print(citation.get_text())
    
    link = citation.find('a')

    print(link.get('href'))
    print()


 
