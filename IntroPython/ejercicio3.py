# David Rodriguez Marco

#!/usr/bin/env python
# -*- coding utf-8 -*-
import sys

outputFile = "output.txt"

def generateDictionary(lines):
    dic={}
    for line in lines:
        palabras = line.split(' ')
        for palabra in palabras:
            palabra = palabra.strip()
            if dic.has_key(palabra):
                dic[palabra] += 1
            else:
                dic[palabra] = 1
    
    f = open(outputFile, 'w')
    for k, v in dic.items():
        f.write(k + ": " + str(v) + '\n')
    f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            f = open(sys.argv[1], 'r')
            lines = f.readlines()
            f.close()
            generateDictionary(lines)
        except:
            print "El fichero no existe"
    else:
        print "Uso: python " + sys.argv[0] + " [Fichero_entrada]"
