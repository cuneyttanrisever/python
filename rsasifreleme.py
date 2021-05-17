from Crypto.PublicKey import RSA 
print "\n","*" * 30 + "\n"
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
print "\n","*" * 30 + "\n"
sor = raw_input("Sifrelenecek metni giriniz = ")
sifrebit=2048
anahtar = RSA.generate(sifrebit)
privateanahtari = anahtar.exportKey(passphrase=sor, pkcs=8)
publicanahtari = anahtar.publickey().exportKey()
print privateanahtari
print "\n","*" * 50 + "\n"
print publicanahtari