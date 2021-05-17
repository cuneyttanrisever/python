#coding:utf-8
import hashlib
import sys
import time
import base64
import datetime
import os
reload(sys) 
sys.setdefaultencoding('utf-8')
os.system('cls' if os.name == 'nt' else 'clear')
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
def gecen(baslangic, bitis):
    sonuc = bitis - baslangic
    d= str(sonuc).split(":")
    dd= d[0]+":"+d[1]+":"+d[2][0:2]
    print renkler.sari+"Program islemi   %s' surede bitirmistir."%(dd)+renkler.beyaz
    
class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print renkler.yesil + """
##################################################################
#                          Hacked by DexmoD                      #
#-------------------------_₺₺₺₺₺₺₺₺₺₺₺₺₺₺₺₺_-------------------- #
# Bir islem secin ve kirilacak hash i girin                      #
# Ardindan wordliste ayni klasorde ise sifre.txtolarak giriniz.  #
# Degilse uzantisi ile birlikte giriniz /sdcard/sifre.txt gibi   #
#                                                                #
##################################################################"""+renkler.beyaz
aks=0
def yazi():
    global aks
    aks +=1
    sys.stdout.write("\r")
    sys.stdout.write(renkler.kirmizi+"Denenen sifre sayisi = %s"%(aks)+renkler.beyaz)
    sys.stdout.write("\r")
    sys.stdout.flush()



def kmd5(hashmd5,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.md5(sifre).hexdigest()
                if dene==hashmd5 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def kmd5salt(hashmd5,salt,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.md5(salt+sifre).hexdigest()
                if dene==hashmd5 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s  "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s:%s" %(sifre,dene,salt)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def kmd5salt2(hashmd5,salt,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashmd5)==32 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.md5(sifre+salt).hexdigest()
                if dene==hashmd5 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s :%s" %(sifre,dene,salt)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def ksha224(hashsha224,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashsha224)==56 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.sha224(sifre).hexdigest()
                if dene==hashsha224 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def ksha1(hashsha1,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashsha1)==40 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.sha1(sifre).hexdigest()
                if dene==hashsha1 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def ksha256(hashsha256,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashsha256)==64 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.sha256(sifre).hexdigest()
                if dene==hashsha256 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def ksha384(hashsha384,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashsha384)==96 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.sha384(sifre).hexdigest()
                if dene==hashsha384 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def ksha512(hashsha512,liste):
    global aks
    baslangic=datetime.datetime.now()
    aks =0
    kontrol= []
    try:
        dosya=open(liste,"r").readlines()
    
        if len(hashsha512)==128 and dosya !="":
            for i in dosya:
                sifre=i.replace("\n","")
                dene=hashlib.sha512(sifre).hexdigest()
                if dene==hashsha512 :
                
                    print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
                    print renkler.kirmizi+"KIRILAN SİFRE = "+renkler.yesil+"%s   "%(sifre)+renkler.beyaz
                    print renkler.yesil+"\n%s = %s" %(sifre,dene)+renkler.beyaz
                    bitis=datetime.datetime.now()
                    gecen(baslangic,bitis)
                    kontrol.append("1")
                    break
                    sys.exit()
                else:
                    yazi()
            if kontrol!="":
                sys.exit()
            else:
                print renkler.mavi+"\nBulunamadi :(\n"+renkler.beyaz
                bitis=datetime.datetime.now()
                gecen(baslangic,bitis)
        else:
            print renkler.kirmizi+"Bu hash md5 degildir."+renkler.beyaz
    except IOError:
        print renkler.kirmizi+"Boyle bir dosya yoktur.Lutfen dosya adini ve uzantisini kontrol ediniz."+renkler.beyaz
        sys.exit()
def kbase64(hbase64):
    try:
        baslangic=datetime.datetime.now()
        dene=base64.b64decode(hbase64)
        print renkler.kirmizi+"\n---KIRILDI---"+renkler.beyaz
        print renkler.yesil+"\n%s = %s" %(dene,hbase64)+renkler.beyaz
        bitis=datetime.datetime.now()
        gecen(baslangic,bitis)
        sys.exit()
    except TypeError:
        print renkler.kirmizi+"Bu hash base64 degildir."+renkler.beyaz

print renkler.kirmizi+"""
1 = md5 Decrypter
2 = md5 (salt+md5) Decrypter
3 = md5 (md5+salt) Decrypter
4 = sha1   Decrypter
5 = sha224 Decrypter
6 = sha256 Decrypter
7 = sha384 Decrypter
8 = sha512 Decrypter
9 = base64 Decrypter
"""+renkler.beyaz

sec=raw_input("Lütfen Seçtiğiniz numarayı giriniz = ")
if sec =="1":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak md5'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    kmd5(hashmd5,liste)
if sec == "2":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak md5'i giriniz = \n"+renkler.beyaz)
    salt=raw_input(renkler.kirmizi+"lutfen salt' i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    kmd5salt(hashmd5,salt,liste)

if sec == "3":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak md5'i giriniz = \n"+renkler.beyaz)
    salt=raw_input(renkler.kirmizi+"lutfen salt' i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    kmd5salt2(hashmd5,salt,liste)
if sec == "4":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak sha1'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    ksha1(hashmd5,liste)
if sec == "5":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak sha224'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    ksha224(hashmd5,liste)
if sec == "6":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak sha256'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    ksha256(hashmd5,liste)
if sec == "7":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak sha384'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    ksha384(hashmd5,liste)
if sec == "8":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak sha512'i giriniz = \n"+renkler.beyaz)
    liste=raw_input(renkler.yesil+"lutfen wordlist dosyasini giriniz. ayni klasorde ise wordlist.txt gibi dosya adini yaz degilse; \nuzantisi ile birlikte yaziniz. /sdcard/wordlist.txt gibi giriniz = "+renkler.beyaz)
    ksha512(hashmd5,liste)

if sec == "9":
    hashmd5=raw_input(renkler.sari+"lutfen kirilacak base64'ü giriniz = \n"+renkler.beyaz)
    kbase64(hashmd5)


