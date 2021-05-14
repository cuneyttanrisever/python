import os
os.system('cls' if os.name == 'nt' else 'clear')
print("""
#####################################
#      Mesai Ücreti Hesaplama       #
#      Coder: Cüneyt TANRISEVER     #
#####################################

NOT: Haftalık 45 saatten fazla çalışmayı devlet mesaiden sayıyor.
Örnek = 1 haftada 60 saat çalışılmış 60 - 45= 15 saat fazla mesai yapılmış.
Bunu 4 le çarpıp aylık olarakta yazabilirsiniz 15*4= 60 saat  
Mesai aylık olarakta yazabilirsiniz.
Asgari ücretliden yıl sonuna doğru gelir  24.000Tl yi aşığı için  gelir vergisi oranı %20 ye çıkıyor ve kademe kademe artıyor yuzdelik
İşverene destek verildiği için net ücretten kesinti olmuyor eğer asgari ücretten fazla maaş alıyorsanız
Gelir Vergisi Kesinti olacaktır.
\n\n""")

def ilksoru ():
    try:
        global sorular
        sorular=int(input("Asgari ücret maaşından hesaplamak için \"1\" yazıp enter a basınız. \nAsgari ücretten Yüksek bir maaş ise \"2\" yazıp enter a basınız. = "))
        if sorular ==1:
            ikinci_soru(1)
        elif sorular ==2:
            ikinci_soru(2)
        else:
            ##print("Sadece 1 veya 2 rakamlarını kullanabilirsiniz")
            ilksoru ()
    except ValueError:
        ##print("Sadece 1 veya 2 rakamlarını kullanabilirsiniz")
        ilksoru ()
    finally:
        pass
def ikinci_soru(a):
    global brutmaas
    if a==1:
        brutmaas=3577.50
        ucuncu_soru()
    elif a==2:
        try:
            brutmaas=float(input("Brüt Maaşınızı Giriniz.= "))
            ucuncu_soru()
        except ValueError:
            ##print("UYARI:Maaşı yazarken ornek= 5423.55 şeklinde yazınız \",\" yerine \".\" kullanınız")
            try:
                def ikinci_soru_1():
                    sor=int(input("Çıkmak için 0 , brüt mass yeniden girmek için 1 yazıp enterlayınız =  "))
                    if sor ==0:
                        ##print("Program kapatılıyor!.")
                        os.system("exit 1")
                       
                    elif sor ==1:
                        ikinci_soru(2)
                    else:
                       ##print("Sadece 0 veya 1 rakamlarını kullanabilirsiniz")
                       ikinci_soru_1()
                ikinci_soru_1()
            except ValueError:
                ##print("Çok sayıda hatalı giriş yapıldı çıkılıyor!.")
                os.system("exit 1")
            finally:
                pass
        finally:
            pass
def ucuncu_soru():

    global mesai_suresi
    try:
        mesai_suresi=float(input("Mesai Süresini Giriniz.= "))
        dorduncu_soru()
        
    except ValueError:
            ##print("UYARI:Saati yazarken sayıdan başka bir şey yazmayınız.\nOrnek= 10 veya 10.5  şeklinde yazınız \",\" yerine \".\" kullanınız")
            try:
                def ucuncu_soru_1():
                    sor=int(input("Çıkmak için 0 , Mesai Süresini yeniden girmek için 1 yazıp enterlayınız =  "))
                    if sor ==0:
                        ##print("Program kapatılıyor!.")
                        os.system("exit 1")
                       
                    elif sor ==1:
                        ucuncu_soru()
                    else:
                       ##print("Sadece 0 veya 1 rakamlarını kullanabilirsiniz")
                       ucuncu_soru_1()
                ucuncu_soru_1()
            except ValueError:
                ##print("Çok sayıda hatalı giriş yapıldı çıkılıyor!.")
                os.system("exit 1")
def dorduncu_soru():
    print ("\nAsgari Geçim İndirimi (AGİ) SEÇ ")
    print("""Medeni Durumunu SEÇ Örnek bekarsanız 1 yazıp entera basınız.:
1 - Bekar iseniz
2 - Evli eşi çalışmayan çocuksuz iseniz
3 - Evli eşi çalışmayan 1 çocuklu iseniz
4 - Evli eşi çalışmayan 2 çocuklu iseniz
5 - Evli eşi çalışmayan 3 çocuklu iseniz
6 - Evli eşi çalışmayan 4 çocuklu iseniz
7 - Evli eşi çalışmayan 5 ve daha faza çocuklu iseniz
8 - Evli eşi çalışan iseniz
9 - Evli eşi çalışan 1 çocuklu iseniz
10 - Evli eşi çalışan 2 çocuklu iseniz
11 - Evli eşi çalışan 3 çocuklu iseniz
12 - Evli eşi çalışan 4 çocuklu iseniz
13 - Evli eşi çalışan 5 ve daha faza çocuklu iseniz
14 - Boşanmış çocuksuz iseniz
15 - Boşanmış 1 çocuklu iseniz
16 - Boşanmış 2 çocuklu iseniz
17 - Boşanmış 3 çocuklu iseniz
18 - Boşanmış 4 çocuklu iseniz
19 - Boşanmış 5 ve daha faza çocuklu iseniz 
""")
    try:
        
        agisor=int(input("Medeni durumunuza karşılık gelen sayıyı seçiniz. = "))
        
        if agisor >=1 and agisor <=19:
                yillik_sor()
                agi_ekle(agisor)
                
        else:
                ##print("1HATALI GİRİŞ \n---------------Lütfen 1 ila 19 arası bir sayı yazınız-----------\n")
                dorduncu_soru()
    except ValueError:
        ##print("2HATALI GİRİŞ \n---------------Lütfen sadece sayı giriniz-----------\n")
        try:
            def dorduncu_soru_1():
                sor=int(input("Çıkmak için 0 ,  yeniden AGİ seçmek için 1 yazıp enterlayınız =  "))
                if sor ==0:
                    ##print("Program kapatılıyor!.")
                    os.system("exit 1")
                           
                elif sor ==1:
                        dorduncu_soru()
                else:
                    ##print("Sadece 0 veya 1 rakamlarını kullanabilirsiniz")
                    dorduncu_soru_1()
            dorduncu_soru_1()
        except ValueError:
            ##print("Çok sayıda hatalı giriş yapıldı çıkılıyor!.")
            os.system("exit 1")
    finally:
        pass
def agi_ekle(agi):
    #agiler
    global gagi
    if agi ==1:
        gagi=268.31
    elif agi ==2:
        gagi=321.98
    elif agi ==3:
        gagi=362.22
    elif agi ==4:
        gagi=402.47
    elif agi ==5:
        gagi=456.13
    elif agi ==6:
        gagi=456.13
    elif agi ==7:
        gagi=456.13
    elif agi ==8:
        gagi=268.31
    elif agi ==9:
        gagi=308.56
    elif agi ==10:
        gagi=348.81
    elif agi ==11:
        gagi=402.47
    elif agi ==12:
        gagi=429.30
    elif agi ==13:
        gagi=456.13
    elif agi ==14:
        gagi=268.31
    elif agi ==15:
        gagi=308.56
    elif agi ==16:
        gagi=348.81
    elif agi ==17:
        gagi=402.47
    elif agi ==18:
        gagi=429.30
    elif agi ==19:
        gagi=456.13
    saatlik_brut_ucret(sorular)
    return(gagi)
def saatlik_brut_ucret(a):
    global brutlu_maas
    saatlik_ucret_brut=brutmaas/255
    brut_mesaili_ucret=((saatlik_ucret_brut*50)/100)+saatlik_ucret_brut
    brut_mesaisuresi_toplam=brut_mesaili_ucret*mesai_suresi
    brutlu_maas=brut_mesaisuresi_toplam+brutmaas
    asgari_brut_mesai_maas_hesaplama(brutlu_maas)  
def yillik_sor():
    
    try:
        global saydir 
        saydir=int(input("Aynı Mesaiyi 12 ay boyunca hesaplatmak için 1 değilse 0 yazınız.= "))
        if saydir >=0 and saydir <=1:
            saydir
        else:
                ##print("HATALI GİRİŞ \n---------------Lütfen 0 yada 1  yazınız-----------\n")
                yillik_sor()
    except:
        ##print("HATALI GİRİŞ \n---------------Lütfen sadece sayı giriniz-----------\n")
        try:
            def dorduncu_soru_1():
                sor=int(input("Çıkmak için 0 ,  yllık sorusu için 1 yazıp enterlayınız =  "))
                if sor ==0:
                    ##print("Program kapatılıyor!.")
                    os.system("exit 1")
                           
                elif sor ==1:
                        yillik_sor()
                else:
                    ##print("Sadece 0 veya 1 rakamlarını kullanabilirsiniz")
                    dorduncu_soru_1()
            dorduncu_soru_1()
        except ValueError:
            ##print("Çok sayıda hatalı giriş yapıldı çıkılıyor!.")
            os.system("exit 1")
    finally:
        pass
def asgari_brut_mesai_maas_hesaplama(brutlu_maass):
    global gelir_vergisi_matrahi
    global brutlu_maass1
    brutlu_maass1=brutlu_maass
    sgk_prim_payi=brutlu_maass*14/100
    issizliksigortasiprimiscipayi=brutlu_maass*1/100
    gelir_vergisi_matrahi=brutlu_maass-(sgk_prim_payi+issizliksigortasiprimiscipayi)
    kamuflatis(saydir)
def asgari_brut_mesai_maas_hesaplama1(brutlu_maass,ay,saydir,gelir_vergisi_matrahi1):
    #global gelir_vergisi_matrahi
    
    if saydir==1:
        sgk_prim_payi=brutlu_maass*14/100
        #print ("sqk prim payı = ",sgk_prim_payi)
        issizliksigortasiprimiscipayi=brutlu_maass*1/100
        ##print ("issizli sigortası payı = ",issizliksigortasiprimiscipayi)
        gelir_vergisi_matrahi=brutlu_maass-(sgk_prim_payi+issizliksigortasiprimiscipayi)
        ##print ("gelir vergisi matrahı = ",gelir_vergisi_matrahi)
        gelir_vergisi_miktari=gelir_vergisi_matrahi1
        ##print ("gelir vergisi miktarı = ",gelir_vergisi_miktari)
        damgavergisi=brutlu_maass*0.00759
        ##print ("damga vergisi = ",damgavergisi)
        kesintiler_toplami=sgk_prim_payi+issizliksigortasiprimiscipayi+gelir_vergisi_miktari+damgavergisi
        ##print ("kesintiler toplamı = ",kesintiler_toplami)
        Net_ucret=(brutlu_maass-kesintiler_toplami)+gagi
        toparla=round((Net_ucret),2)
        print(ay,"Ayı Net Mesaili Maaşınız. = ", round((Net_ucret),2))
        ##print ("---------------------------------------------")
    elif saydir==0:
        sgk_prim_payi=brutlu_maass*14/100
        issizliksigortasiprimiscipayi=brutlu_maass*1/100
        gelir_vergisi_matrahi=brutlu_maass-(sgk_prim_payi+issizliksigortasiprimiscipayi)
        gelir_vergisi_miktari=gelir_vergisi_matrahi1
        damgavergisi=brutlu_maass*0.00759
        kesintiler_toplami=sgk_prim_payi+issizliksigortasiprimiscipayi+gelir_vergisi_miktari+damgavergisi
        Net_ucret=(brutlu_maass-kesintiler_toplami)+gagi
        toparla=round((Net_ucret),2)
        print(ay,"Net Mesaili Maaşınız. = ", round((Net_ucret),2))

def kamuflatis(saydir):
    aylar=["Ocak ","Şubat ","Mart ","Nisan ","Mayıs ","Haziran ","Temmuz ","Ağustos ","Eylül ","Ekim ","Kasım ","Aralık"]
    kamuflatifgelirvergisimatrahi=gelir_vergisi_matrahi
    say1=0
    global gelir_vergisi_matrahi1
    #os.system('cls' if os.name == 'nt' else 'clear')
    if saydir ==0: 
        kamuflatifgelirvergisimatrahi+=gelir_vergisi_matrahi
        if kamuflatifgelirvergisimatrahi <= 24000:
            gelir_vergisi_matrahi1=gelir_vergisi_matrahi*15/100
            asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,"Bu ay ",saydir,gelir_vergisi_matrahi1)
    elif saydir==1:
        kmufaylar=[]
        for i in aylar:
            
            print ("Artan gelir vergisi matrahı =",kamuflatifgelirvergisimatrahi)
            if kamuflatifgelirvergisimatrahi < 24000:
                gelir_vergisi_matrahi1=gelir_vergisi_matrahi*15/100
                asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                ###print("-------------------\ngelir vergisi matrahı =%s--------"%(gelir_vergisi_matrahi1))
                kmufaylar.append(kamuflatifgelirvergisimatrahi)
            elif kamuflatifgelirvergisimatrahi> 24000 and kamuflatifgelirvergisimatrahi<=53000:
                #print(kamuflatifgelirvergisimatrahi)
                #print(kmufaylar[-1])
                if int(kmufaylar[-1]) < 24000:
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    print ("24k dan yeni degeri cıkartıyoruz")
                    eski=(kamuflatifgelirvergisimatrahi-kmufaylar[-1])
                    ##print("eski kalan vergi = ",eski)
                    yeni_kalan=kamuflatifgelirvergisimatrahi-24000
                    yenikalan=((yeni_kalan)*20)/100
                    eskivergi=((eski-yeni_kalan)*15)/100
                    ##print("yeni kalan vergi = ",yeni_kalan)
                    gelir_vergisi_matrahi1=eskivergi+yenikalan
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
                else:
                    gelir_vergisi_matrahi1=gelir_vergisi_matrahi*20/100
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("son değer 24k dan %20 cıkartıyoruz")
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
# --------------------------------------------------------------------------
            elif kamuflatifgelirvergisimatrahi> 53000 and kamuflatifgelirvergisimatrahi<=190000:
                #print(kamuflatifgelirvergisimatrahi)
                #print(kmufaylar[-1])
                if int(kmufaylar[-1]) < 53000:
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("24k dan yeni degeri cıkartıyoruz")
                    eski=(kamuflatifgelirvergisimatrahi-kmufaylar[-1])
                    ##print("eski kalan vergi = ",eski)
                    yeni_kalan=kamuflatifgelirvergisimatrahi-24000
                    yenikalan=((yeni_kalan)*20)/100
                    eskivergi=((eski-yeni_kalan)*15)/100
                    ##print("yeni kalan vergi = ",yeni_kalan)
                    gelir_vergisi_matrahi1=eskivergi+yenikalan
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
                else:
                    gelir_vergisi_matrahi1=gelir_vergisi_matrahi*20/100
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("son değer 24k dan %20 cıkartıyoruz")
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
# --------------------------------------------------------------------------
            elif kamuflatifgelirvergisimatrahi> 190000 and kamuflatifgelirvergisimatrahi<=650000:
                #print(kamuflatifgelirvergisimatrahi)
                #print(kmufaylar[-1])
                if int(kmufaylar[-1]) < 190000:
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("24k dan yeni degeri cıkartıyoruz")
                    eski=(kamuflatifgelirvergisimatrahi-kmufaylar[-1])
                    ##print("eski kalan vergi = ",eski)
                    yeni_kalan=kamuflatifgelirvergisimatrahi-24000
                    yenikalan=((yeni_kalan)*20)/100
                    eskivergi=((eski-yeni_kalan)*15)/100
                    ##print("yeni kalan vergi = ",yeni_kalan)
                    gelir_vergisi_matrahi1=eskivergi+yenikalan
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
                else:
                    gelir_vergisi_matrahi1=gelir_vergisi_matrahi*20/100
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("son değer 24k dan %20 cıkartıyoruz")
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
# --------------------------------------------------------------------------
            elif kamuflatifgelirvergisimatrahi> 650000:
                #print(kamuflatifgelirvergisimatrahi)
                #print(kmufaylar[-1])
                if int(kmufaylar[-1]) < 650000:
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("24k dan yeni degeri cıkartıyoruz")
                    eski=(kamuflatifgelirvergisimatrahi-kmufaylar[-1])
                    ##print("eski kalan vergi = ",eski)
                    yeni_kalan=kamuflatifgelirvergisimatrahi-24000
                    yenikalan=((yeni_kalan)*20)/100
                    eskivergi=((eski-yeni_kalan)*15)/100
                    ##print("yeni kalan vergi = ",yeni_kalan)
                    gelir_vergisi_matrahi1=eskivergi+yenikalan
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)
                else:
                    gelir_vergisi_matrahi1=gelir_vergisi_matrahi*20/100
                    ##print("24k dan fazla ")
                    ##print("Kamuflatif miktar = ",kamuflatifgelirvergisimatrahi)
                    #print ("son değer 24k dan %20 cıkartıyoruz")
                    ##print("Toplam gelir vergisi matrahı = ",gelir_vergisi_matrahi1)
                    kmufaylar.append(kamuflatifgelirvergisimatrahi)
                    asgari_brut_mesai_maas_hesaplama1(brutlu_maass1,i,saydir,gelir_vergisi_matrahi1)
                    #print (i,"ayı kamuflatif vergi matrahı ",kamuflatifgelirvergisimatrahi)        
            
            
            
            
            say1=1
            kamuflatifgelirvergisimatrahi+=gelir_vergisi_matrahi
ilksoru()








