#!/usr/bin/python
#-*- coding: utf-8 -*--
#5)Introduce un año y muestre el/los clubes que se han creado ese año.
from lxml import etree

doc = etree.parse("clubpensionistas.xml")

raiz = doc.getroot()

directorio = raiz.findall("club")


fecha = raw_input("fecha contitucion: ")
encontrado=False
for d in directorio:
	telefono=d.findall("fconstitucion")
	
	for t in telefono:
		
			
		if t.text.startswith(fecha):
			encontrado=True
			nombre=d.findall("nombre")
			for n in nombre:

				print t.text, n.text
if not encontrado:
	print "No hay clubs con esa fecha de constitución"		