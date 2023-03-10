import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('file:///Users/joaob.rocha-junior/Dropbox/Courses/EXA844/Aulas/Aula03/code/html/Basic.html')

html = str(page.read().decode('utf-8'))

soup = BeautifulSoup(html, 'lxml')

print("Título:", soup.title.string)
for img in soup.find_all('img'):
  print("src: ", img.attrs.get("src"))
  break
