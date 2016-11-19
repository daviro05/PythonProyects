# David Rodríguez Marco
#!/usr/bin/env python
import os
import re
import urllib
from BeautifulSoup import *

url = 'https://trenesytiempos.blogspot.com.es/'

def findLinks():
    html = urllib.urlopen(url).read()
    links = re.findall("href='(https://trenesytiempos.blogspot.com.es/\d.+?)'", html)
    return links

def urlSearch(search, link):
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)
    res = soup.findAll('span', text = re.compile(search))
    return len(res) != 0

if __name__ == "__main__":
    links = ()
    search = raw_input("Introduce el conjunto de palabras clave: ")
    links = findLinks()

    for link in links:
        if urlSearch(search, link) == True:
            print link
