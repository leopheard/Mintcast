import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
get_soup("https://feeds.buzzsprout.com/284746.rss")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts113/v4/30/1e/26/301e2617-50d6-7e7c-edb3-abb93ccab7be/mza_1744527215859774756.jpg/939x0w.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=10):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts113/v4/30/1e/26/301e2617-50d6-7e7c-edb3-abb93ccab7be/mza_1744527215859774756.jpg/939x0w.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
