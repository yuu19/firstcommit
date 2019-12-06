import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=KMZF4gXc8OQ&t=1397s'
r = requests.get(url)
html_contents = r.text

html_soup = BeautifulSoup(html_contents, 'html.parser')
print(html_soup.find('h1'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
