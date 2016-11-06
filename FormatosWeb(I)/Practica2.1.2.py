# David Rodriguez Marco

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import operator

aire = open("residuos_peligrosos_eprtr_2008_040412.csv")
archivoSalida = open("FrecuenciaResiduos.csv", "w")
salidaEscritor = csv.writer(archivoSalida, delimiter=";")
lectura = csv.reader(aire, delimiter=";")
listaDatos = list(lectura)
listaDatos.pop(0)
listaDatos.pop(0)
listaord = sorted(listaDatos, key=operator.itemgetter(2), reverse=False)
auxiliar = listaord[0][2]
listaAuxiliar = [listaord[0][2], ""]
listaFinal = []
contadorSumaTotal = 0

for empresa in listaord:
    if auxiliar == empresa[2]:
        contadorSumaTotal += 1
    else:
        listaAuxiliar[1] = contadorSumaTotal
        listaFinal.append(listaAuxiliar)
        listaAuxiliar = [empresa[2], ""]
        auxiliar = empresa[2]
        contadorSumaTotal = 1

for linea in listaFinal:
    salidaEscritor.writerow(linea)
archivoSalida.close()
