
#!/usr/bin/python
#-*- coding: utf-8 -*--

#1)listar clubs



from lxml import etree

doc = etree.parse("/home/alvarocamargo/Descargas/segundo año/lenguaje de marcas/clubpensionistas.xml")

raiz = doc.getroot()

