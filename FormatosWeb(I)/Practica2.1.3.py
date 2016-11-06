# David Rodriguez Marco

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import operator

aire = open("aire_eprtr_2008_030412.csv")
archivoSalida = open("Contaminantes.csv", "w")
salidaEscritor = csv.writer(archivoSalida, delimiter=";")
lectura = csv.reader(aire, delimiter=";")
listaDatos = list(lectura)
listaDatos.pop(0)
listaDatos.pop(0)
listaord = sorted(listaDatos, key=operator.itemgetter(2), reverse=False)
auxiliar = listaord[0][2]
listaAuxiliar = [listaord[0][0], listaord[0][1], listaord[0][2], listaord[0][3], listaord[0][4], listaord[0][5], listaord[0][6], ""]
listaFinal = []
contadorSumaTotal = 0.00

for empresa in listaord:
    if auxiliar == empresa[2]:
        kgAno = empresa[10].replace(",", ".")
        contadorSumaTotal += float(kgAno)
    else:
        listaAuxiliar[7] = contadorSumaTotal
        listaFinal.append(listaAuxiliar)
        listaAuxiliar = [empresa[0], empresa[1], empresa[2], empresa[3], empresa[4], empresa[5], empresa[6], ""]
        auxiliar = empresa[2]
        kgAno = empresa[10].replace(",", ".")
        contadorSumaTotal = float(kgAno)
listaFinalOrdenada = sorted(listaFinal, key=operator.itemgetter(7), reverse=True)
listaMasContaminantes = listaFinalOrdenada[0:9]

for rowContaminante in listaMasContaminantes:
    salidaEscritor.writerow(rowContaminante)
archivoSalida.close()