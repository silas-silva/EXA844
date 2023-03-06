import xml.sax
from datetime import datetime

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.tipo = ""
    self.nome = ""
    self.latitude = ""
    self.longitude = ""

  def startElement(self, tag, attributes):    
    self.tipo = ""
    self.nome = ""
    self.latitude = ""
    self.longitude = ""
    
    if tag == "node":
      self.latitude = attributes["lat"]
      self.longitude = attributes["lon"]
    if tag =="tag":  
      if attributes.get("k") == "amenity":
        self.tipo = attributes.get("v")
      if attributes.get("k") == "name":
        self.nome = attributes.get("v")

  def endElement(self, tag):    
    if tag =="node":	
      print("tipo: ", self.tipo)
      print("nome: ", self.nome)
      print("Latitude: ", self.latitude)
      print("Longitude: ", self.longitude)


  def characters(self, content):	
    pass


start = datetime.now() # Iniciar Contagem do tempo


parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")


end = datetime.now() # Fim da contagem do tempo

print("Tempo de execução: (hh:mm:ss.ms) ", end - start)