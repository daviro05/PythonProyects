# David Rodriguez Marco

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cifrar(texto,desp,desp2):
    muestra = ""
    texto = convertir(texto,desp2)
    palabras = texto.split(' ')
    copia = palabras[:]
    indices = []
    for i in range(0,len(palabras)):
        indices.append((i + int(desp)) % len(palabras))
        copia[indices[i]] = palabras[i]
    for j in range(0,len(copia)):
        muestra += "".join(copia[j])+" "
    print "\nTexto cifrado: "+ muestra
    
def convertir(text,desp2):
    resul = ""
    for car in text:
        if car.isalpha():
           if car.islower():
               resul += chr((ord(car) - 97 + int(desp2)) % 26 + 97)
           if car.isupper():
               resul += chr((ord(car) - 65 + int(desp2)) % 26 + 65)      
        else:
            resul += car
    return resul    
    
if __name__ == "__main__":
   texto = raw_input("Texo a cifrar: ")
   desp2 = raw_input("Desplazamiento letra: ")
   desp = raw_input("Desplazamiento palabra: ")  
   if desp.isdigit() and desp2.isdigit():
       cifrar(texto,desp,desp2)
   else:
       print "El desplazamiento ha de ser un digito"