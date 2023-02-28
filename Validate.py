from lxml import etree
parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse(open("Banco.xml", "rb"))
dtd = etree.DTD(open("Banco.dtd", "rb"))
print("Nome: <Coloque seu nome aqui>")
print(dtd.validate(tree))
print(dtd.error_log.filter_from_errors())