#coding:utf-8
from passlib.hash import bcrypt
import sys
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
hash=sys.argv[1]
dosya=sys.argv[2]

sifreler=open(dosya, "r")

dex=sifreler.read().splitlines()

print "basladi"
for i in dex:
	dex1=bcrypt.verify(i, hash)
	if dex1:
		print "Kirilan hash = ", i
		break
