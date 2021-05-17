#coding:utf-8
import os
import sys
import requests
from bs4 import BeautifulSoup
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
reload(sys) 
sys.setdefaultencoding('utf-8')
os.system('cls' if os.name == 'nt' else 'clear')
print "ne yapcan :)"
siteler=[]
ST=[]
url=raw_input("site urlsini gir")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)
res=rq.get(url).content
soup= BeautifulSoup(res, "html.parser")
yazi= soup.find_all("a")
for i in yazi[5:]:
    cc=i.get('href')
    dd= cc.encode("utf-8")
    ST.append(dd)
yaz=open("siteler.txt","w")
yaz.close()
yaz=open("siteler.txt","a")
for i in ST:
    yaz.write(url+str(i)+"\n")
yaz.close()
print "siteler.txt dosyasina urller eklenmistir."





