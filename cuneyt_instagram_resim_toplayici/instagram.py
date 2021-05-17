import urllib.request
import re
import os
os.system('cls' if os.name == 'nt' else 'clear')
print ("""
#######################################################
#                                                     #  
# Cüneyt TANRISEVER // instagram resim toplama aracı  #
#                                                     #  
#######################################################

""")
sor=input("İnstagram user adı giriniz. = ")
adres=f"https://www.instagram.com/{sor}/?__a=1"
try:
    url         = urllib.request
    connection  = url.urlopen(adres)
    content = connection.read()
    oku=open('dex.json',"r").readlines()
    dex=re.findall("\"thumbnail_src\"\:\"(.*?)\",",str(content))
    yaz=open("insta.txt","w")
    sira=0
    print ("\n")
    for i in dex:
        urllib.request.urlretrieve(i,sor+str(sira)+".jpeg")
        sira+=1
        yaz.write( str((i))+"\n")
        print (sor+str(sira)+".jpeg adında resim kaydedildi")
    print ("Toplam ",len(dex), "tane resim indirildi")
    yaz.close()
    if dex !="":
        print ("İndirilen resim linkleride insta.txt dosyasına kayıt edilmiştir")
except urllib.error.HTTPError:
    print ("Böyle bir user bulunamadı!")
