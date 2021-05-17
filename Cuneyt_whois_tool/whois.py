#coding:utf-8
import requests 
from bs4 import BeautifulSoup
print ("""
###################################
#       Cüneyt TANRISEVER         #
#       Who is sorgu araci        #
###################################""")

while True:
    sor=raw_input("site adresini gir = ")
    kl=str(sor).replace("http://","").replace("https://","").replace("/","")
    url="https://www.whois.com/whois/%s"%(kl)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    res=rq.get(url)
    rm=res.content
    soup = BeautifulSoup(rm,'html.parser')
    sonuc= soup.findAll('pre', attrs={'class':'df-raw'})
    dd=str(sonuc).replace("<pre class=\"df-raw\" id=\"registrarData\">","")
    bol= dd.replace("\\n","\n").split("URL of the")
    print bol[0]
