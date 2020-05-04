import requests  
from bs4 import BeautifulSoup
url = 'http://abehiroshi.la.coocan.jp/'
r = requests.get(url)
html_contents = r.text
#print(r.text)

html_soup = BeautifulSoup(html_contents, 'html.parser')

print(html_soup)

print(html_soup.find('meta').name)
print(html_soup.find('meta').contents)



#link = html_soup.find('a')

#print(link)

#print(link.get('href'))

#print(str(first_title))

#print(first_h1.text)

#print(first_h1.attrs)

#print('----------CITATIONS--------------')

#cites = html_soup.find_all('cite', class_ = 'citation', limit=5)
#for citation in cites:
 #   print(citation.get_text())
    
  #  link = citation.find('a')

   # print(link.get('href'))
   # print()


 
