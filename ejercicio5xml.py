#!/usr/bin/python
#-*- coding: utf-8 -*--
#5)Introduce un año y muestre el/los clubes que se han creado ese año.
from lxml import etree

doc = etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")

raiz = doc.getroot()

directorio = raiz.findall("club")

fecha = raw_input("fecha contitucion: ")

for d in directorio:
	telefono=d.findall("fconstitucion")
	
	