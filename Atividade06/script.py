#!/usr/bin/python3
# Import modules for CGI handling
import cgi, cgitb
import json
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
autor = form.getvalue('autor')
mensagem = form.getvalue('mensagem')
data = form.getvalue('data')

dados = {"autor" : autor, "mensagem" : mensagem, "data" : data}

#Salvar no arquivo
with open("db.json", 'w' , encoding='utf-8') as database:
    json.dump(dados, database, indent=4)


print ("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CGI Script</title>")
print("</head>")
print("<body>")
print ("<h2>Mensagem recebida</h2>")
print(f"Nome: {autor}")
print ("</br>")
print(f"Data: {data}")
print ("</br>")
print(f"Text : {mensagem}")
print ("</br>")
print("</body>")
print ("</html>")