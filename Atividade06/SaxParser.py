# encoding=utf8

from html.parser import HTMLParser
import requests

listaSites = ['https://vitat.com.br/alimentacao/busca-de-alimentos/mais-buscados']

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.currentData = ""
    self.nomeAlimento = ""
    self.calorias = ""
    self.carboidratos = ""
    self.proteinas = ""
    self.gorduras = ""
    self.hasCalorias = False
    self.hasCarboidratos = False
    self.hasProteinas = False
    self.hasGorduras = False
    self.hasRankingLinkVitat = False
    self.hasResultLinkVitat = False
    self.hasH1Vitat = False
    self.pularProximoAlimento = False
    self.linksCategoriasVitat = []
    self.linksAlimentosIndividuaisVitat = []
    self.dicDados = {}

  def handle_starttag(self, tag, attrs):
    self.currentData = ""

    if tag =="a":
      for k, v in attrs:
        if k == "class":
          if v == "ranking__link":  #Pagina das categorias de alimentos do site Vitat
            self.hasRankingLinkVitat = True
          if v == "result__link pl-0 pl-lg-3": #Pagina dos alimentos do site vitat
            self.hasResultLinkVitat = True
        elif k == 'href' and self.hasRankingLinkVitat: #Pagina das categorias de alimentos do site Vitat
          self.linksCategoriasVitat.append("https://vitat.com.br" + v)
          self.hasRankingLinkVitat = False
        elif k == 'href' and self.hasResultLinkVitat: #Pagina dos alimentos por categoria do site Vitat
          if v[0] == '/':
            if "/alimentacao/busca-de-alimentos" in v:
              self.linksAlimentosIndividuaisVitat.append("https://vitat.com.br" + v)
          self.hasRankingLinkVitat = False
    elif tag == "td":
      pass
    elif tag == "h1":
      for k, v in attrs:
        if k == "class":
          if "result__title" in v:
            self.hasH1Vitat = True
      pass
        

  def handle_endtag(self, tag):
    if tag == "td":
      if self.currentData == 'Calorias (valor energético)':
        self.hasCalorias = True
      elif self.currentData == 'Carboidratos':
        self.hasCarboidratos = True
      elif self.currentData == 'Proteínas':
        self.hasProteinas = True
      elif self.currentData == 'Gorduras totais':
        self.hasGorduras = True
      
      elif 'kcal' in self.currentData and self.hasCalorias:
        self.hasCalorias = False
        self.calorias = self.currentData
      elif 'g' in self.currentData and self.hasCarboidratos:
        self.hasCarboidratos = False
        self.carboidratos = self.currentData
      elif 'g' in self.currentData and self.hasProteinas:
        self.hasProteinas = False
        self.proteinas = self.currentData
      elif 'g' in self.currentData and self.hasGorduras:
        self.hasGorduras = False
        self.gorduras = self.currentData      
        self.pularProximoAlimento = True
    elif self.pularProximoAlimento == True:
      self.pularProximoAlimento = False
      self.dicDados[self.nomeAlimento] = {
        "Calorias" : self.calorias,
        "Proteinas" : self.proteinas, 
        "Carboidratos" : self.carboidratos, 
        "Gorduras Totais" : self.gorduras
        }
    elif tag == "h1":
      if self.hasH1Vitat:
        self.nomeAlimento = self.currentData
        self.hasH1Vitat = False

  def handle_data(self, data):
      self.currentData += data


page = requests.get(listaSites[0])

# Instanciar
parser = MyHTMLParser()

#Verificar Links da pagina inicial
parser.feed(page.content.decode('utf-8'))

#print("Imagem:", parser.image)

# Verificar link das paginas filhas
#page = requests.get(parser.linksCategoriasVitat[0])
#parser.feed(page.content.decode('utf-8'))

# Verificar alimentos individuais das paginas filhas da filha

#Mapear todos os links de todos os alimentos

#Pegar dados de cada alimentos

cont = 0

for c in parser.linksAlimentosIndividuaisVitat:
  cont += 1
  print(cont)
  page = requests.get(c)
  parser.feed(page.content.decode('utf-8'))

print(parser.dicDados)
