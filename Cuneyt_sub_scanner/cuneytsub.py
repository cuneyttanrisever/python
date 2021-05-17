#Coding:Utf-8
from urlparse import urlparse
import sys
import argparse
import re
import os
import sys
import argparse
import requests
os.system('cls' if os.name == 'nt' else 'clear')
print """
##############################################################################
# Cüneyt Tanrısever bing sub domain tarayicisi                               #
# Kullanimi = cuneytsub.py site adi ve cekilecek sayfa sayisi                #
# cuneytsub.py justice.gov 5 gibi calistirabilirsiniz ana domain yazin tamam #
##############################################################################"""

dsyz=open("sonuc.txt","w")
dsyz.close()
cekilen=[]
son=[]
site=sys.argv[1]
ssayisi=sys.argv[2]
def calistir():
	global cekilen
	global son
	cekilen=[]
	son=[]
	for i in range(int(ssayisi)):
		syfa=i*10+1
		ac = requests.get("http://www.bing.com/search?q=domain%3a"+site+"&first="+str(syfa))
		oku = ac.content
		ayikla = re.compile("""<h2><a href="(.*?)" h="ID=SERP,""") 
		topla = ayikla.findall(oku)
		
		for url in topla:
			urlp = urlparse(url)
			dex = urlp.netloc
			#print dex
			cekilen.append(dex)
	cuneyt()
def  cuneyt():
    global karsilastirma
    global sonduzen
    karsilastirma=[]
    sonduzen=[]
    for i in cekilen:
        karsilastirma.append(i)
    for i in karsilastirma:
        if sonduzen.count(i)==0:
            sonduzen.append(i)
    for i in sonduzen:
        print i
        dsyz=open("sonuc.txt","a")
        dsyz.write(i+"\n")
        dsyz.close()
    karsilastirma=[]
    sonduzen=[]
    print "sonuclar  sonuc.txt adli klasore yazildi"
calistir()
