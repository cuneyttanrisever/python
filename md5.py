import hashlib
dexmod = hashlib.md5()
print "Cuneyt TANRISEVER md5 olusturucu tool"
while True:
    sor=raw_input("md5 lenecek sifreyi giriniz = ")
    dexmod.update(sor)
    print "      "+dexmod.hexdigest()+"\n"