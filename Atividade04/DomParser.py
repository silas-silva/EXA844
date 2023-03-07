from xml.dom.minidom import parse
from datetime import datetime
import json

start = datetime.now() # Iniciar Contagem do tempo

mapDocument = parse('map.osm')
atributo = ""   # Variavel para auxiliar

dados = {}


print("Starting DOM Parser...")
print("")
cont = 0
for c in mapDocument.getElementsByTagName("node"):	
	tags = c.getElementsByTagName("tag")
	dado = {}
	for t in tags:
		atributo = t.getAttribute("k")

		if atributo == "amenity":
			#print("tipo", t.getAttribute("v"))   # Mostrar o tipo de estabelecimento
			dado['tipo'] = t.getAttribute("v") # Tipo do estabelecimetno
			try:
				if tags[1].getAttribute("k") == "name":
					#print("nome", tags[1].getAttribute("v")) # Nome do estabelecimento
					dado['nome'] = tags[1].getAttribute("v") # Nome do estabelecimento

					#print("latitude", c.getAttribute("lat")) # Mostrar a latitude
					dado['latitude'] = c.getAttribute("lat")

					#print("longitude", c.getAttribute("lon")) # Mostrar a longitude
					dado['longitude'] = c.getAttribute("lon")
					cont += 1
					dados[f"{cont}"] = dado
					break
			except:
				#print("latitude", c.getAttribute("lat")) # Mostrar a latitude
				dado['latitude'] = c.getAttribute("lat")

				#print("longitude", c.getAttribute("lon")) # Mostrar a longitude
				dado['longitude'] = c.getAttribute("lon")
				cont += 1
				dados[f"{cont}"] = dado
				break
	

end = datetime.now() # Fim da contagem do tempo

#Json
print(dados)

#Salvar dados no arquivo
with open("Jsons/domJson.json", 'w' , encoding='utf-8') as database:
    json.dump(dados, database, indent=4)   

print("")
print("Tempo de execução DOM: (hh:mm:ss.ms) ", end - start)
print("")
