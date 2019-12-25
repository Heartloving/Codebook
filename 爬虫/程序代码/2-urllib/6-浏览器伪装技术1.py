#浏览器伪装技术

       
import urllib.request
url="http://www.oschina.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
opener=urllib.request.build_opener()
#urlopen默认是无法添加包头的，需要用别的方法，其中build_opener()就是一种
#build_opener()就是创建一个opener对象，然后利用该对象的addheaders方法添加包头
opener.addheaders=[headers]

#opener对象下的open方法可以打开对应的网页，此时包含包头
data=opener.open(url).read()

fh=open("5.html","wb")
fh.write(data)
fh.close()

