import requests
from bs4 import BeautifulSoup

def fishnames():
    URL = 'https://en.wikipedia.org/wiki/List_of_fish_of_the_Mediterranean_Sea'
    response = requests.get(URL)
    if response.ok:
        titles = []
        soup = BeautifulSoup(response.text, 'lxml')
        rows = soup.findAll('i')
        for row in rows:
            a = row.find('a')
            if a is not None :
                title = a['title']
                titles.append(title.replace(' (page does not exist)', ''))
    return titles
