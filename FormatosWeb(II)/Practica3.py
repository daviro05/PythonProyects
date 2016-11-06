#David Rodriguez Marco

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
import urllib
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

arbol = ElementTree.parse("MonumentosZaragoza.xml")
root = arbol.getroot()

i=0

for child in root.findall(".//Feature"):
    propertyValue = child.find("PropertyValue").text
    print i, ":", propertyValue
    i = i+1

terminar = "NO"

while terminar != "n":
    numMonumento = raw_input("Elija el numero de un monumento: ")
    
    
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
    monumento = root[int(numMonumento)][0].text
    url = serviceurl + urllib.urlencode({'address': monumento.encode('utf-8'),'components':'country:ES'}) 
    uh = urllib.urlopen(url)
    data = uh.read()
    doc = ElementTree.fromstring(data)
    
    latitud = doc.find(".//location/lat").text
    longitud = doc.find(".//location/lng").text

    print "Nombre monumento:", monumento
    print "Latitud:", latitud
    print "Longitud:", longitud
    print "Pagina web asociada:", root[int(numMonumento)][1].text

    contenido = urllib.urlopen(root[int(numMonumento)][1].text)
    contenidoLeido = contenido.read()
    
    cod = contenido.headers['content-type'].split('charset=')[-1]

    indiceInicio = contenidoLeido.find("<p>")
    indiceFinal = contenidoLeido.find("</div>", indiceInicio)
    paraImprimir = contenidoLeido[indiceInicio+3 : indiceFinal]
    paraImprimirFinal = cleanhtml(paraImprimir)
    paraImprimirFinal = unicode (paraImprimirFinal, cod)
    print "Descripcion: "
    print paraImprimirFinal.encode('utf-8')

    terminar = raw_input("Quiere buscar informacion sobre otro monumento? (n para terminar, cualquier letra para continuar)")
