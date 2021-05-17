import phpass
import Queue
import time
import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')
print  """
############################################################################
#                        Cüneyt TANRISEVER                                  #
#                    Phpass sifre kirma araci                              #
#  ilk once $P$BvFUKtbCPkRrPt9OWl/cFxBSYiZd2J/ seklindeki hash giriniz     #
#  sonra wordlist sifre dosyasini giriniz.ayni dizinde ise                 #
#  direk adini yaziniz farkli yerde ise uzantisi ile yaziniz               #
#  hash giriniz = $P$BvFUKtbCPkRrPt9OWl/cFxBSYiZd2J/                       #
#  sifre listesini giriniz = sifreler.txt gibi giriniz.                    #
############################################################################"""
dur= False
abk=0
hash=raw_input("hash giriniz = ")
sifrelistesi=raw_input("sifre listesini giriniz = ")

dex=open(sifrelistesi,"r").readlines()
print "dosyadaki mevcut denecek sifre sayisi = %s"%(len(dex))
print hash 
q=Queue.Queue()
for i in dex:
    b=i.replace("\n","")
    q.put(b)

def kir (sifre,hash):
    if phpass.crypt_private(sifre, hash) == hash:
        print "\nsifre kirildi \nkirilansifre = %s , hashsiniz = %s "%(sifre,hash)
        yaz=open("kirilansifre.txt","a")
        
        si=str(sifre)+"   =   "+str(hash)
        
        yaz.write(str(si))
        yaz.close()
        print  "Bulunan sifre kirilansifre.txt dosyasina yazilmistir\n\n\n\n\n\n\n"
        global dur
        dur = True
        time.sleep(4)
        abk="deneme"
while True:
    if dur :
            sys.exit()
            break
    
    kir(q.get(),hash)
    sys.stdout.write('\r')
    abk+=1
    sys.stdout.write('[+]baglanti normal denenen sifre sayisi = '+ str(abk))
    sys.stdout.flush()
