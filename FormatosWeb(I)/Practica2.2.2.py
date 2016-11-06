# David Rodriguez Marco

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usar python 3
# Para usar el parseador html se uso BeautifulSoup, para instalarlo:
# pip install beautifulsoup4

import json
from bs4 import BeautifulSoup

file_in = "semaforos.txt"
file_out = "10_semaforos_mas_frecuentes.txt"

if __name__ == "__main__":
	f = open(file_in, 'r')
	datos = f.read()
	datos_js = json.loads(datos)
	f.close()
	dic={}
	num_datos = len(datos_js["features"])
	for i in range(0, num_datos):
		html = datos_js["features"][i]["properties"]["Description"]
		parse = BeautifulSoup(html, "html.parser")
		datos_semaforos = parse.text.split('\n')
		cont_semaforo = datos_semaforos[3].split(':')[1]
		ubicacion = datos_semaforos[2].split(':')[1]
		dic[ubicacion] = 0

		try:
			cont_semaforo = int(cont_semaforo)
			dic[ubicacion] += cont_semaforo
		except Exception as ex:
			pass

	for k,v in dic.items():
		dic[k] = v/num_datos

	f_out = open(file_out, 'w')
	for clave in sorted(dic, key=lambda x: dic[x], reverse=True)[:10]:
		texto = "Calle: " + clave.ljust(50, " ") + " Frecuencia semaforos: " + str(dic[clave])
		print(texto)
		f_out.write(texto + '\n')
	f_out.close()
