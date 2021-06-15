from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.buzzsprout.com/205226.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://storage.buzzsprout.com/variants/5gbunm7tbw3ofsrd269ll09338mk/8d66eb17bb7d02ca4856ab443a78f2148cafbb129f58a3c81282007c6fe24ff2.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://storage.buzzsprout.com/variants/5gbunm7tbw3ofsrd269ll09338mk/8d66eb17bb7d02ca4856ab443a78f2148cafbb129f58a3c81282007c6fe24ff2.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
if __name__ == '__main__':
    plugin.run()
