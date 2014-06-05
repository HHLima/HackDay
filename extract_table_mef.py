#!/bin/bash
#[@antoniocuga] Script para descargar
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar
import csv
import socks
import socket

#Este script esta torificado por lo que es necesario
#tener el tor corriendo, en caso no quieran usarlo comentar
#las dos lineas siguientes.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

#Guardamos una cookie (sirve cuando queremos descargar informacion
#de sitios con login
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#url de descarga del MEF, el ultimo parametro 'y' le pasaremos una variable
#para que descargue por anyos
domain = 'http://apps5.mineco.gob.pe/transparencia/Navegador/Navegar_5.aspx?_tgt=html&_uhc=yes&0=&1=E&2=06&3=006&4=15&30=9002&31=3999999&32=&y=%s'

if __name__ == '__main__':

    start = int(raw_input("Anyo de inicio: "))
    end = int(raw_input("Anyo de fin: ")) + 1
    filename = raw_input("nombre de archivo: ")
    ofile = open('%s.csv' % filename, 'wb')
    writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for year in range(start, end):
        try:
            page = domain % year

            print 'Descargando ...'
            print page

            content = opener.open(page)
            soup = BeautifulSoup(content)

            try:
                table = soup.find("table", class_="Data")
                cells = table.find_all("tr")
                tr = cells
                for td in tr:
                    rows = td.find_all("td")
                    contentrow = []
                    contentrow.append(year)
                    for row in rows:
                        row = ((row.get_text()).encode('utf-8')).strip()
                        contentrow.append(row)
                    writer.writerow(contentrow)
            except ValueError:
                pass

        except ValueError:
            pass
