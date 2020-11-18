import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_fish_of_the_Mediterranean_Sea#Cyclostomata'

response = requests.get(url)

with open('fishnames.csv', 'w') as file:
    file.write('Fish Name\n')

    if response.ok:
        titles = []
        soup = BeautifulSoup(response.text, 'lxml')
        rows = soup.findAll('i')
        for row in rows:
            a = row.find('a')
            if a is not None :
                title = a['title']
                titles.append(title)
                file.write(title.replace('(page does not exist)', '') + '\n')
