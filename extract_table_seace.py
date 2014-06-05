from bs4 import BeautifulSoup
import urllib2
import urllib
from cookielib import CookieJar
from webscraping import xpath
import csv
import re
import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
domain = 'http://www2.seace.gob.pe/?scriptdo=PKU_PROVEEDORESBUENAPRO.doviewTOP100&fldanho=%s&pfldtop100=1-2014&_CALIFICADOR_=PORTLET.1.117.0.21.81&_REGIONID_=1&_PORTLETID_=117&_ORDERID_=0&_PAGEID_=21&_CONTENTID_=81'


if __name__ == '__main__':

    start = int(raw_input("Anio de inicio: "))
    end = int(raw_input("Anio de fin: "))
    filename = raw_input("nombre de archivo: ")
    ofile = open('%s.csv' % filename, 'wb')
    writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for year in range(start, end):
        response2 = opener.open(domain % year)
        html = BeautifulSoup(response2)
        container = html.find("table", id="117")
        table = container.find_all("tr")
        table = table[2].find_all("tr")

        for tr in table:
            rows = tr.find_all("td")
            contentrow = []
            contentrow.append(year)
            for row in rows:
                row = ((row.get_text()).encode('utf-8')).strip()
                contentrow.append(row)
            writer.writerow(contentrow)
