import socket
import random
import errno
import sys
import time
import os
import socks
from threading import Thread
from Queue import Queue
os.system('cls' if os.name == 'nt' else 'clear')
print """
#######################################
# Cüneyt Tanrısever proxy test pro v1 #
# 1sn veya daha az surede baglanan    #
# super proxy listesini olusturur     #
# proxyler sonuc.txt ye yazilacaktir  #
#######################################"""
dexk=open("sonuc.txt","w")
dexk.close()
dexkontrol="Teklike Yok devam"
q=Queue()
kaynak=[]
sor=input("heyecan yok no panik \nthread degeri gir bence 100 yeter :) = ")
def threadsorgu():
	global sor
	#sor=input("heyecan yok no panik \nthread degeri gir bence 200 yeter :) = ")
	proxykontrol()
def proxykontrol():
	global prxdex
	cdosya = raw_input("Proxy dosya adini giriniz. = ")
	prxdex = open(cdosya).readlines()
	calistir()
def quen():
	
    global kaynak
    global q
    for i in kaynak:
        q.put(i)
q.join()
        
def proxyoku():
    for i in prxdex:
        x=i.replace("\n","")
        kaynak.append(x)
    
    quen()
def basladex():
    global dexkontrol
    
    while True:
        try:
                proxy=q.get().strip().split(":")
                v= q.empty()
                if v==True:
                    print "---------+-+--liste bitti---++-+---\n+++++PROGRAMI KAPAT+-++\nsaglan proxyler d.txt yazdirildi"
                    dexkontrol="Kapat"
                    dexknt()
                    sys.exit()
                    sys.exit(0)
                    break
                q.task_done()
                print proxy
                socket.setdefaulttimeout(1)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy[0]), int(proxy[1])))
                print "baglandi"
                print str(proxy[0]), int(proxy[1])
                print "gonderiliyor"
                print ("Request sent from " + str(proxy[0]+":"+proxy[1]) ) 
                print "gonderdi"
                dexk=open("sonuc.txt","a")
                dexk.write(str(proxy[0])+":"+str(proxy[1])+"\n")
                dexk.close()
                s.close()
                
        except socket.timeout:
            v= q.empty()
            if v==True:
                    
                    sys.exit()
                    sys.exit(0)
            print "zaman asimi hata"
            continue
        except EnvironmentError as exc: 
                v= q.empty()
                if v==True:
                   
                    sys.exit()
                    sys.exit(0)
                if exc.errno == errno.ECONNREFUSED:
                    if v==True:
                        q.join()
                        sys.exit()
                        sys.exit(0)
                    print "bag hata"
                    continue
        except :
            v= q.empty()
            if v==True:
                    
                    sys.exit()
                    sys.exit(0)
                    break
            print "cuneyt hata"
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("saglam proxyler sonuc.txt yazdirildi")
            sys.exit()
def dexknt():
    c=os.getppid()
 #   print " program 5 sn sonra kapanacak.\nSonuclar sonuc.txt yazildi"
    #time.sleep(1)
    os.system("kill -9 %s"%(c))
    sys.exit()
    while True:
    	sys.exit()
def calistir():
    proxyoku()
    d()
    basladex()
 
def d():    
    for i in range(sor):
            worker = Thread(target=basladex)
            worker.setDaemon(True)
            worker.start()
            v= q.empty()
            if v==True:
                    
                    sys.exit()
                    sys.exit(0)
                    break
threadsorgu()
sys.exit()
