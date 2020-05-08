import requests
import records
from bs4 import BeautifulSoup 
from urllib.parse import urljoin
from sqlalchemy.exc import IntegrityError

#CREATE TABLE [IF NOT EXISTS] tbl_name
   # (col_name data_type, ...)

db = records.Database('sqlite:///crawler_database.db')

db.query('''CREATE TABLE IF NOT EXISTS links (
            url text PRIMARY_KEY,
            created_at datetime,
            visited_at datetime NULL)''')
db.query('''CREATE TABLE IF NOT EXISTS numbers (url text, number integer, PRIMARY KEY (url, number))''')

def store_link(url):
    try:
        db.query('''INSERT INTO links (url, created_at)
                    VALUES (:url, CURRENT_TIMESTAMP)''', url=url)

    except IntegrityError as ie:
        #この数字は存在するので何もしない
        pass

def store_number(url, number):
    try:
        db.query('''INDERT INFO numbers (url, number)
                    VALUES (:url, :number)''', url=url, number=number)

    except IntegrityError as ie:
        #この数字は存在するので何もしない
        pass

def mark_visited(url):
    db.query('''UPDATE links SET visited_at=CURRENT_TIMESTAMP
                WHERE url=:url''', url=url)


def get_random_unvisited_link():
    link = db.query('''SELECT * FROM links
                       WHERE visited_at IS NULL
                       ORDER BY RANDOM() LIMIT 1''').first() #テーブルからランダムに１件取得するクエリ
    return None if link is None else link.url

def visit(url):
    html = requests.get(url).text
    html_soup = BeautifulSoup(html, 'html.parser')
    new_links = []
    for td in html_soup.find_all("a"):
        store_number(url, int(td.text.strip()))
    for link in html_soup.find_all("a"):
        link_url = link.get('href')
        if link_url is None:
            continue
        full_url = urljoin(url, link_url)
        new_links.append(full_url)
    return new_links

store_link('http://www.webscrapingfordatascience.com/crawler/')
url_to_visit = get_random_unvisited_link()
while url_to_visit is not None:
    print('Now visiting:', url_to_visit)
    new_links = visit(url_to_visit)
    print(len(new_links), 'new link(s) found')
    for link in new_links:
        store_link(link)
    mark_visited(url_to_visit)
    url_to_visit = get_random_unvisited_link()


