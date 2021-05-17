from bs4 import BeautifulSoup
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
# c1.tar çalıştırdıktan sonra çekilen c1 sayfasının kaynak kodunu alıp sayfa.html diye kaydedip programı çalıştırın
sayfa=open("sayfa.html","r").read()

soup = BeautifulSoup(sayfa,'html.parser')
dex= soup.find_all('a')
for i in dex:
    l=i.find_all('a')
    print i
sokup=BeautifulSoup(sayfa,"html.parser")
vc=[]
for i in sokup.find_all("a"):
    p= i.get('href')
    print p
    sayfa=open("/sdcard/d.txt","a")
    sayfa.write(str(p)+"\n")
    sayfa.close()
