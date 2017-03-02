#!/usr/bin/python
# -*-coding: utf-8 -*-
#4)Introduce una subcadena , en el caso que coincida con un numero de teléfono muestre de que club se trata.
from lxml import etree

doc = etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")

raiz = doc.getroot()

directorio = raiz.findall("club")

var = raw_input("Subcadena de un numero de telefono: ")
hay=False
for d in directorio:
	telefono= d.findall("telefono")
	
	for c in telefono:
		
		
		if c.text.startswith(var):
			hay=True
			nombre=d.findall("nombre")
			for y in nombre:

				print c.text, y.text
if not hay:
	print "No hay ningún número de telefono que empiece por dicha cadena"