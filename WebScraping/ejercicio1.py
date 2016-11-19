# David Rodríguez Marco
import os
import re
import urllib
from BeautifulSoup import *

url = 'https://trenesytiempos.blogspot.com.es/'

def createDirectory(url):
    dirname = url[39:49]
    try:
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        os.chdir(dirname)
    except OSError:
        print "Error al crear el directorio ", dirname

def getImages(url):
    dir_project = os.getcwd()
    createDirectory(url)

    html = urllib.urlopen(url).read()
    sopa = BeautifulSoup(html)

    etiquetas=sopa('a',{"imageanchor":"1"})
    j=0
    for i in etiquetas:
        url_img = i.get('href', None)
        if not (url_img).startswith('http'):
            url_img = "https:" + url_img 

        archivo=open("foto"+str(j)+".jpg","wb")

        imagen=urllib.urlopen(url_img)
        while True:
            info = imagen.read(100000)
            if len(info) < 1 : break
            archivo.write(info)

        archivo.close()
        j=j+1 

    os.chdir(dir_project)

def getLinks():
    dic = {}
    html = urllib.urlopen(url).read()
    links = re.findall("href='(https://trenesytiempos.blogspot.com.es/2016_.+?)'", html)
    
    for link in links:
        getImages(link)

if __name__ == '__main__':
   getLinks()

