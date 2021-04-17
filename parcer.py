import urllib.request
from bs4 import BeautifulSoup

def ria_news_politics(rows):
    url = 'https://ria.ru/politics/'
    html = urllib.request.urlopen(url) 
    soup = BeautifulSoup(html,'lxml')
    titles_collector = soup.find_all('a', class_ = "list-item__title color-font-hover-only")
    urls_collector = soup.find_all('div', class_='list-item__content')
    
    titles = []
    #titles_string = ''
    urls = []
    #urls_string = ''
    merged_string = ''

    for i in titles_collector:
        titles.append(i.text)

    for i in urls_collector:
        urls.append(i.find_all('a', href = True)[0]['href'])

    for i in range(rows, rows + 5):
        merged_string = merged_string + '#' + str(i + 1) + ' ' + str(titles[i]) + ' ' + '\n' + str(urls[i]) + '\n' + '\n'

    return (merged_string)


def ria_news_world(rows):
    url = 'https://ria.ru/world/'
    html = urllib.request.urlopen(url) 
    soup = BeautifulSoup(html,'lxml')
    titles_collector = soup.find_all('a', class_ = "list-item__title color-font-hover-only")
    urls_collector = soup.find_all('div', class_='list-item__content')
    img_collector = soup.find_all('img', class_ = 'responsive_img m-list-img')
    
    titles = []
    #titles_string = ''
    urls = []
    #urls_string = ''
    images = []
    merged_string = ''

    for i in titles_collector:
        titles.append(i.text)

    for i in urls_collector:
        urls.append(i.find_all('a', href = True)[0]['href'])

    for i in img_collector:
        images.append(i.text)

    for i in range(rows, rows + 5):
        merged_string = merged_string + '#' + str(i + 1) + ' ' + str(titles[i]) + ' ' + '\n' + str(urls[i]) + '\n' + images[i]+ '\n'

    return (merged_string)