import requests
import ssl
sy=open("sayfa.html","w")
sy.close()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)
while True:
    
    url=raw_input("url giriniz = ")
    
    res=rq.get(url,allow_redirects=False,verify=False)
    rm=res.content
    print res.content
    sy=open("sayfa.html","w")
    sy.write(str(rm))
    sy.close()
print "bitti sayfa.html bak"
