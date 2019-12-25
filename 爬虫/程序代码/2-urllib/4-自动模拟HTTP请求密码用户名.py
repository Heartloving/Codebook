#urllib自动模拟HTTP请求，对于简单用户名和密码的处理

import urllib.request
import urllib.parse


url="..."


mydata=urllib.parse.urlencode({
"name":"xxxx",
"pass":"xxxx"
    }).encode("utf-8")
req=urllib.request.Request(url,mydata)
data=urllib.request.urlopen(req).read()
fh=open("test.html","wb")
fh.write(data)
fh.close()

