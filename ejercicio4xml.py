#!/usr/bin/python
# -*-coding: utf-8 -*-

from lxml import etree

doc = etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")

raiz = doc.getroot()

directorio = raiz.findall("club")

var = raw_input("Subcadena de un numero de telefono: ")

for d in directorio:
	telefono= d.findall("telefono")
	
	for c in telefono:
		
		
		
