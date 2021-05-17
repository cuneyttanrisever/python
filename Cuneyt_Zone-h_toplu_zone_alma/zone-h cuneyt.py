import requests
#coding:utf-8
import sys
print "*"*50
print "* Cuneyt TANRISEVER oto zone alma programı"
print "* Kullanimi = cuneyt.py Dosya listesi rumuz" 
print "* cuneyt.py siteler.txt cuneyt"
print "*"*50
dosya=sys.argv[1]
rumuz=sys.argv[2]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)
oku=open(dosya,"r").readlines()
for i in oku:
    url=i.replace("\n","").replace("\r","")
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
                url = "http://" + url
    
        url1="http://www.zone-h.org/notify/single"
        datas={"defacer":rumuz,"domain1":url,"hackmode":"15","reason":"3"}
        gonder=rq.post(url1,data=datas)
        print url ,"gonderildi"
    except:
        print("urlde hata var tekrar gir.")
