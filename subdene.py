#coding:utf-8
import requests
import re
import os
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
dosya=open("subdomaincekilen.txt","w")
dosya.close()
domainok=open("liste.txt","r").readlines()
print len(domainok)," site sub domain aramasına girdi"
domainliste=[]

for i in domainok:
	dx=i.replace("\r","").replace("\n","")
	domainliste.append(dx)
    
def proxykontrol():
    global proxyD
    say=0
    proxyoku=open("dexmodprx.txt","r").readlines()
    prxy=[]
    for i in proxyoku:
        dd=i.replace("\n","").replace("\r","") 
        prxy.append(dd)
    len(prxy)
    for i in prxy:
        try:
            dexmod= i
            ht="http://"+dexmod
            htps="https://"+dexmod
            proxyD = {"http"  : ht, 
                    "https" : htps}
            rq= requests.Session()
            r= requests.get("https://dnsdumpster.com",proxies=proxyD,timeout=7)
            if r.status_code == 200:
                dom=domainliste[say]
                DNSdumpster(dom,proxyD)
                say+=1
                print dom,proxyD
            else:
                continue
        except requests.exceptions.Timeout:
            print "7 sn de baglanmadi"
            continue
        except requests.exceptions.ConnectionError:
            print "Kötü Baglanti"
            continue
def DNSdumpster(domain,prox):
    try:
        print domain," sitesi subları cekiliyor"
        url = 'https://dnsdumpster.com'
        uag = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
	
        get_token = requests.get(url,headers={'User-Agent':uag},proxies=prox ,timeout=7)
        token = re.findall("value=\'(.*?)\'",get_token.text)[0]
        post = requests.post(url,data={
        'csrfmiddlewaretoken':token,
        'targetip':domain
        },
        cookies={
        'csrftoken':token
        },
        headers={
        'User-Agent':uag,
        'Referer':url
        }            
        )
        subdo = re.findall('http://(.*?)"',post.text)
        print subdo
        for x in subdo:
            dosya=open("subdomaincekilen.txt","a")
            dosya.write(x+"\n")
            dosya.close()
            print x
    except requests.exceptions.Timeout:
            print "7 sn de baglanmadi"
            pass
    except requests.exceptions.ConnectionError:
            print "Kötü Baglanti"
            pass

proxykontrol()
ekle=[]
def dduz (dexm,yaz):
	kaynak=[]
	karsilastirma=[]
	sonduzen=[]
	dex=dexm
	dex2=open(yaz,"w")
	dex2.close()
	for duzen in dex:
		dzr=duzen.replace("\n","")
		kaynak.append(dzr)
	for i in kaynak:
		karsilastirma.append(i)
	for i in karsilastirma:
		if sonduzen.count(i)==0:
			sonduzen.append(i)
	for i in sonduzen:
			neo=open(yaz,"a")
			neo.write(i+"\n")
			neo.close()
	kaynak=[]
	karsilastirma=[]
	sonduzen=[]

domainok=[]
os.system("del bulunandomainler.txt")
dex1=open("subdomaincekilen.txt","r").readlines()
for i in dex1:
    dx1=i.replace("\r","").replace("\n","")
    ekle.append(dx1)
dduz(ekle,"subdomainlerliste.txt")
