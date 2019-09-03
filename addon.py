from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://feeds.buzzsprout.com/284746.rss"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts113/v4/30/1e/26/301e2617-50d6-7e7c-edb3-abb93ccab7be/mza_1744527215859774756.jpg/939x0w.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts113/v4/30/1e/26/301e2617-50d6-7e7c-edb3-abb93ccab7be/mza_1744527215859774756.jpg/939x0w.jpg"},
   ]
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items


if __name__ == '__main__':
    plugin.run()
