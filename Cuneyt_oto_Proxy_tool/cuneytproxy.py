import requests
import re
import os
import time
import sys
import urllib2
import base64
import random
import ssl
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf-8')
os.system('cls' if os.name == 'nt' else 'clear')
print"""
##################################################
#             Cüneyt TANRISEVER                  #
# Proxy listesi olusturma araci v.1              #
# 5 ayri proxy sitesine baglanip proxyleri ceker #
##################################################"""
#time.sleep(5)
def agents():
    useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
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
    dexx1=random.choice(useragents)
    return dexx1
def idcloak():
    global sontoplu
    print "-----------------------------www.idcloak.com cekiliyor ------------------------------"
    url="http://www.idcloak.com/proxylist/proxy-list.html\#sort"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    res=rq.get(url)
    rm=res.content
    soup = BeautifulSoup(rm,'html.parser') 
    #print soup
    ad=re.compile("""<tr><td>(.*?)</td></tr>""")
    topla = ad.findall(str(soup))
    ads=re.compile("""<td>.*</td>.*""")
    ne=ads.findall(str(topla))
    ka=[]
    ka1=[]
    ka2=[]
    ka3=[]
    sontoplu=[]
    for i in topla:
        ne=ads.findall(str(i))
        ka.append(str(ne))

    for i in ka:
        kas= i.split("td")
        dex= kas[-1],kas[-3]
        ka1.append(str(dex))
    #print ka1
    kal="\']\", \'>"

    for i in ka1:
        ff=i.replace(kal, ":")
        ka2.append(ff)
    for i in ka2:
        kac=i.replace("</')","")
        ka3.append(kac)
    for i in ka3:
        kac=i.replace("(\">","")
        sontoplu.append(kac)
        print kac
    freeprx()
def freeprx():
    global sontoplu
    print "-----------------------------free-proxy-list.net cekiliyor ------------------------------"
    url="https://free-proxy-list.net"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    res=rq.get(url)
    rm=res.content
    soup = BeautifulSoup(rm,'html.parser') 
    #print soup
    ads=re.compile("""<tr><td>.*?</td><td>.*?</td>""")
    ne=ads.findall(str(soup))
    kar=[]
    kar1=[]
    for i in ne[:-3]:
        dex=i.replace("</td><td>",":")
        kar.append(str(dex))
    for i in kar:
        dex=i.replace("<tr><td>","")
        kar1.append(str(dex))
    for i in kar1:
        dex=i.replace("</td>","")
        sontoplu.append(dex)
        print dex
    usprx()
def usprx():
    global sontoplu
    print "-----------------------------www.us-proxy.org cekiliyor ------------------------------"
    url="https://www.us-proxy.org"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    res=rq.get(url)
    rm=res.content
    soup = BeautifulSoup(rm,'html.parser') 
    #print soup
    ads=re.compile("""<tr><td>.*?</td><td>.*?</td>""")
    ne=ads.findall(str(soup))
    #print ne[:-3]
    kar=[]
    kar1=[]
    for i in ne[:-3]:
        dex=i.replace("</td><td>",":")
        kar.append(str(dex))
    for i in kar:
        dex=i.replace("<tr><td>","")
        kar1.append(str(dex))
    for i in kar1:
        dex=i.replace("</td>","")
        sontoplu.append(dex)
        print dex
    sockss()
def sockss():
    global sontoplu
    print "-----------------------------www.socks-proxy.net cekiliyor ------------------------------"
    url="https://www.socks-proxy.net"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    res=rq.get(url)
    rm=res.content
    soup = BeautifulSoup(rm,'html.parser') 
    #print soup
    ads=re.compile("""<tr><td>.*?</td><td>.*?</td>""")
    ne=ads.findall(str(soup))
    kar=[]
    kar1=[]
    for i in ne[:-3]:
        dex=i.replace("</td><td>",":")
        kar.append(str(dex))
    for i in kar:
        dex=i.replace("<tr><td>","")
        kar1.append(str(dex))
    for i in kar1:
        dex=i.replace("</td>","")
        sontoplu.append(dex)
        print dex
    dexdex=[]
    karsilastirma=[]
    sonduzen=[]
    for i in sontoplu:
        karsilastirma.append(i)
    for i in karsilastirma:
        if sonduzen.count(i)==0:
            sonduzen.append(i)
    cuneyt=open("cuneytprx.txt","w")
    cuneyt.close()
    for i in sonduzen:
        cuneyt=open("cuneytprx.txt","a")
        cuneyt.write(str(i)+"\n")
        cuneyt.close()
    print "tekrar eden proxyler silinip\nTam olarak %s tane proxy cuneytprx.txt dosyasina yazilmistir..."%(len(sonduzen))

def proxydb():
    print "-----------------------------proxydb.net cekiliyor ------------------------------"
    for saydir in range(20):
        global sontoplu
        saydir*=15
        url="http://proxydb.net/?protocol=http&protocol=https&country=&offset=%s"%(saydir)
        headers = {'User-Agent': agents() }
        rq=requests.session()
        rq.headers.update(headers)
        res=rq.get(url)
        rm=res.content
        #print repr(rm)
        soup = BeautifulSoup(rm,'html.parser') 
        print soup
        ads=re.compile("\'.*?\'\.split")
        ads1=re.compile("atob\(\'.*?\'\.replace")
        ads2=re.compile("var pp = .*?;")
        ne=ads.findall(str(soup))
        ne1=ads1.findall(str(soup))
        ne2=ads2.findall(str(soup))
        #print ne
        kar=[]
        kar1=[]
        kar2=[]
        kar3=[]
        ipek=[]
        birles=[]
        por=[]
        por1=[]
        por2=[]
        por3=[]
        for i in ne:
            dex=i.replace("'.split","")
           # print dex
            kar.append(str(dex))
        for i in kar:
            dex=i.replace("\'","")
            kar1.append(dex[::-1])
        for i in ne1:
            dex=i.replace("\'.replace","")
            kar2.append(dex)
        for i in kar2:
            dex=i.replace("atob(\'","")
            kar3.append(dex)
    
        for i in kar3:
            dex=("".join(base64.b64decode("".join([chr(int(y, 16)) for y in x.split("\\x") if len(y) > 0])).decode() for x in i.split()))
            ipek.append(dex)
        for i in range(len(kar1)):
            bir=kar1[i]+ipek[i]
            birles.append(bir)
        for i in ne2:
            dex=i.replace("var pp =","")
            por.append(dex)
        for i in por:
            dex=i.replace(" -1;","")
            por1.append(dex)
        for i in por1:
            dex=i.replace(" ","")
            por2.append(dex)
        for i in por2:
            dex=i.split("+")
            print dex
            topla=int(dex[0])+int(dex[1])
            por3.append(topla)
        for i in range(len(birles)):
            dex=str(birles[i])+":"+str(por3[i])
            print dex
            sontoplu.append(dex)
       # print sontoplu
        #print len(sontoplu)        
    dexdex=[]
    karsilastirma=[]
    sonduzen=[]
    for i in sontoplu:
        karsilastirma.append(i)
    for i in karsilastirma:
        if sonduzen.count(i)==0:
            sonduzen.append(i)
    cuneyt=open("cuneytprx.txt","w")
    cuneyt.close()
    for i in sonduzen:
        cuneyt=open("cuneytprx.txt","a")
        cuneyt.write(str(i)+"\n")
        cuneyt.close()
    print "tekrar eden proxyler silinip\nTam olarak %s tane proxy cuneytprx.txt dosyasina yazilmistir..."%(len(sonduzen))

idcloak()
