from xml.dom.minidom import parse
from datetime import datetime

start = datetime.now() # Iniciar Contagem do tempo

mapDocument = parse('map.osm')
atributo = ""   # Variavel para auxiliar

print("Starting DOM Parser...")
print("")

for c in mapDocument.getElementsByTagName("node"):	
	tags = c.getElementsByTagName("tag")
	for t in tags:
		atributo = t.getAttribute("k")

		if atributo == "amenity":
			print("tipo", t.getAttribute("v"))   # Mostrar o tipo de estabelecimento
			try:
				if tags[1].getAttribute("k") == "name":
					print("nome", tags[1].getAttribute("v")) # Nome do estabelecimento
					print("latitude", c.getAttribute("lat")) # Mostrar a latitude
					print("longitude", c.getAttribute("lon")) # Mostrar a longitude
					print("=="*20)
					print("")
					break
			except:
				print("latitude", c.getAttribute("lat")) # Mostrar a latitude
				print("longitude", c.getAttribute("lon")) # Mostrar a longitude
				print("=="*20)
				print("")
				break

end = datetime.now() # Fim da contagem do tempo

print("")
print("Tempo de execução DOM: (hh:mm:ss.ms) ", end - start)
print("")