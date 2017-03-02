#!/usr/bin/python
# -*-coding: utf-8 -*-

#2)Contar numeros de clubes.

from lxml import etree
arbol=etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")

raiz=arbol.getroot()
datos=raiz.findall("club")


for a in datos:
	nombre=a.findall("nombre")
	for b in nombre:
		
		
