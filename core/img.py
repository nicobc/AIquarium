from selenium import webdriver
import os
import urllib.request
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.google.com/search?tbm=isch&q='
SAVE_FOLDER = 'images'

def fishnames():
    URL = 'https://en.wikipedia.org/wiki/List_of_fish_of_the_Mediterranean_Sea'
    response = requests.get(URL)
    if response.ok:
        titles = []
        soup = BeautifulSoup(response.text, features='lxml')
        rows = soup.findAll('i')
        for row in rows:
            a = row.find('a')
            if a is not None :
                title = a['title']
                titles.append(title.replace(' (page does not exist)', ''))
    return titles

for fishname in fishnames():

    DATA_DIR = fishname.replace(' ', '_')

    if not os.path.exists(os.path.join(SAVE_FOLDER, DATA_DIR)):
        os.makedirs(os.path.join(SAVE_FOLDER, DATA_DIR))

    driver = webdriver.Firefox()

    url = BASE_URL + fishname.replace(' ', '+')
    driver.get(url)

    imgs = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')[:10]
    for i, img in enumerate(imgs):
        src = img.get_attribute('src')
        urllib.request.urlretrieve(src, os.path.join(SAVE_FOLDER, DATA_DIR, f'img{i}.jpg'))

    driver.close()
