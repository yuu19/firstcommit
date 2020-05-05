<<<<<<< HEAD
import sys
import requests
from bs4 import BeautifulSoup
print(sys.version_info)
=======
import requests
from bs4 import BeautifulSoup
>>>>>>> 37a8aef1cfc22dc68339c78ea2ec4ab49ea685cf
url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

#リストを用いて一覧を保存する
<<<<<<< HEAD
episodes = []

ep_tables = html_soup.find_all('table', class_='wikitable plainrowheaders')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')

    for header in table.find('tr').find('th'):
        headers.append(header.text)

    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th', 'td']):
            values.append(col.text)
        if values:
            episode_dict = {headers[i]: values[i] for i in  range(len(values))}
            eposodes.append(episode_dict)


for episode in episodes:
    print(episode)
    
=======
#episodes = []

#ep_tables = html_soup.find_all('table', class_='wikitable plainrowheaders')

#for table in ep_tables:
#        headers = []
#            rows = table.find_all('tr')
#
#                for header in table.find('tr').find('th'):
#                            headers.append(header.text)
#
 #                               for row in table.find_all('tr')[1:]:
#                                            values = []
#                                                    for col in row.find_all(['th', 'td']):
#                                                                    values.append(col.text)
#                                                                            if values:
#                                                                                            episode_dict = {headers[i]: values[i] for i in  range(len(values))}                                                                                                     eposodes.append(episode_dict)
#
#
 #                                                                                                       for episode in episodes:
  #                                                                                                              print(episode)
                                                                                                                    



>>>>>>> 37a8aef1cfc22dc68339c78ea2ec4ab49ea685cf
