#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
import json
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()
dados = ""

#Salvar no arquivo
with open("db.json", 'r' , encoding='utf-8') as database:
    dados = json.load(database)

print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
listaTeste = []
for c in dados:
    aux = f"<p> Autor: {c}, Mensagem: {dados[c]['mensagem']}, Data: {dados[c]['data']} </p>"
    listaTeste.insert(0,aux)

for c in listaTeste:
    print(c)

print ("</br>")
print("</body>")
