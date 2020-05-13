import requests 
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import dataset
base_url = 'http://alg-d.com/math/'

list = []
lists = []
title_list = []
lili = []
deb = []
def scrape_math(base_url):
    r = requests.get(base_url)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    for li_tag in html_soup.select('body > ul > li'):
        li_a = li_tag.find('a')
        url = li_a.get('href')
        list.append(url)

def scrape_pdf(url):
    url = urljoin(base_url, url)
    lists.append(url)
    r = requests.get(url)
    html_soup = BeautifulSoup(r.text, 'html.parser')
    for li_tag_pdf in html_soup.select('body > ul > li'):
        li_a_pdf = li_tag_pdf.select_one('a[href$= ".pdf"]')
        deb.append(li_a_pdf)
        if not li_a_pdf:
            continue
        title = li_a_pdf.get_text(strip=True) 
        title_list.append(title)
        pdf_url = urljoin(url, li_a_pdf.get('href'))
        lili.append(pdf_url)
        filename = 'books' + title + '.pdf'
        r = requests.get(pdf_url)
        with open(filename, 'w') as f:
                f.write(r.text)
                
inp = input('Do you want to start download pdf (y/n)?')
if inp == 'y':
    scrape_math(base_url)
for url_pdf in list:
    url = urljoin(base_url, url_pdf)
    scrape_pdf(url)

print(list)
print(lists)
print(title_list)
print(lili)
print(deb)

print('sucsess!')

