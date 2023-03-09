from html.parser import HTMLParser
import urllib.request

seeds = []

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.currentData = ""
    self.title = ""
    self.image = ""

  def handle_starttag(self, tag, attrs):
    self.currentData = ""
    
    if tag =="img":  
      for k, v in attrs:
        if k == "src":
          self.image = v

  def handle_endtag(self, tag):
    if tag =="title": 
      self.title = self.currentData      

  def handle_data(self, data):
    self.currentData += data    


with open('seeds.txt', 'r', encoding='UTF-8') as arquivo:
    seeds = arquivo.readlines()


for link in seeds:

    page = urllib.request.urlopen(link)

    parser = MyHTMLParser()
    parser.feed(str(page.read().decode('utf-8')))
    print("")
    print("=="*20)
    print("Título:", parser.title)
    print("Imagem:", parser.image)
    print("=="*20)
    

   