import xml.sax
from datetime import datetime
import json

dados = {}

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.tipo = ""
    self.nome = ""
    self.latitude = ""
    self.longitude = ""
    self.hasAmenity = False

  def startElement(self, tag, attributes):    
    
    if tag == "node":
      self.latitude = attributes["lat"]
      self.longitude = attributes["lon"]
    if tag =="tag":  
      if attributes.get("k") == "amenity":
        self.tipo = attributes.get("v")
        self.hasAmenity = True
      if attributes.get("k") == "name":
        self.nome = attributes.get("v")

  def endElement(self, tag):    
    if tag =="node" and self.hasAmenity:	
      #print("=="*20)
      dado = {}
      #print("tipo: ", self.tipo)
      #dado["tipo"] = self.tipo
      #print("nome: ", self.nome)
      dado["nome"] = self.nome
      #print("latitude: ", self.latitude)
      dado["latitude"] = self.latitude
      #print("longitude: ", self.longitude)
      dado["longitude"] = self.longitude
      
      dados[self.tipo] = dado

      # Limpar variaveis
      dado = {}
      
      self.hasAmenity = False
      self.tipo = ""
      self.nome = ""
      self.latitude = ""
      self.longitude = ""


  def characters(self, content):	
    pass


start = datetime.now() # Iniciar Contagem do tempo


parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")


end = datetime.now() # Fim da contagem do tempo
print("")
print(dados)

#Salvar dados no arquivo
with open("Jsons/saxJson.json", 'w' , encoding='utf-8') as database:
    json.dump(dados, database, indent=4)   

    
print("")
print("Tempo de execução SAX: (hh:mm:ss.ms) ", end - start)
print("")