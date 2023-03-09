import urllib.request
from bs4 import BeautifulSoup

seeds = []


with open('seeds.txt', 'r', encoding='UTF-8') as arquivo:
    seeds = arquivo.readlines()


for link in seeds:

    page = urllib.request.urlopen(link)

    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'lxml')
    print("")
    print("=="*20)
    print("Título:", soup.title.string)
    for img in soup.find_all('img'):
        print("src: ", img.attrs.get("src"))
        break
    print("=="*20)
    print("")