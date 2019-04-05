# pip install requests
# pip install bs4
# pip install win10toast


import requests #requests module
from bs4 import BeautifulSoup as bs #beautiful soup module
from pprint import pprint as pp #pretty print module
from win10toast import ToastNotifier

def check_recent_articles(url): # https://medium.com
    try:
        response = requests.get(url)
    except:
        raise requests.exceptions.ConnectionError('No internet connection or cannot reach {}'.format(url))
    soup = bs(response.content, 'html.parser')

    title_elements = soup.select('h2.ui-h4')
    pp(soup.find('nav')['role'])
    for element in title_elements:
        print(element.string)

    titles = [element.string for element in title_elements]
    return titles


def notify(article_title, text = 'Nothing yet!'):
    toaster = ToastNotifier()
    for title in article_title:
        toaster.show_toast(text, title, duration = 5)

#popular posts = ol.u-padding32



notify(article_title = check_recent_articles('https://medium.com'), text = 'News!')