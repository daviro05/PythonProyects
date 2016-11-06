# David Rodriguez Marco

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv,operator

#Contaminacion,Empresa
archivoCsv=open("agua_eprtr_2008_030412.csv")
lector=csv.reader(archivoCsv,delimiter=';')
listaDatos = list(lector)
listaDatos.pop(0)
listaDatos.pop(0)
listaord = sorted(listaDatos, key=operator.itemgetter(8), reverse=False)

csvRows = []
for row in listaord:
    csvRows.append(row)
archivoCsv.close()

archivoCsv = open('AguaAgrupada.csv','w')
guardarCsv = csv.writer(archivoCsv)
guardarCsv.writerow(["Contaminacion, Empresa"])
for row in csvRows:
     guardarCsv.writerow([row[8]+","+row[2]])
archivoCsv.close()