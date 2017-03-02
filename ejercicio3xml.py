#!/usr/bin/python
#-*- coding: utf-8 -*--
# 3) Introducir el nombre de un club y mostrar su dirección
from lxml import etree
from pprint import pprint 
arbol=etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")
doc=arbol.findall("club")
nombre2=raw_input("Introduce el nombre de un club:")
for x in doc:
	doc=x.find("nombre")
	if doc.text==nombre2:
		nombre=x.findall("direccion")
		for y in nombre:
				print "La direccion del club introducido es la siguiente:", y.text
