#urllib自动模拟HTTP请求

import urllib.request

#===搜索英文
keywd="python" 

#===搜索中文
#keywd="中国科学院大学" 
#keywd=urllib.request.quote(keywd) 

url="http://www.baidu.com/s?wd="+keywd
print(url)
req=urllib.request.Request(url)

data=urllib.request.urlopen(req).read()
fh=open("2.html","wb")  #二进制写入形式打开文件
fh.write(data)
fh.close()
