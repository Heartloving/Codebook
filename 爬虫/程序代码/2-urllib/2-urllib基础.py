#urllib基础：各函数的使用

import urllib.request

urllib.request.urlretrieve("http://www.ucas.ac.cn",filename="2.html")

urllib.request.urlcleanup()

file=urllib.request.urlopen("http://www.ucas.ac.cn")
print(file.info())

#===getheaders():获取头部信息
print(file.getheaders())  #对比print(file.info())
print(file.getheader("server")) #获取服务器信息

#===getcode():返回获取当前网页的状态码
print(file.getcode())
print(file.status)      #获取状态码

#===geturl()：获取当前所爬的网页的url
print(file.geturl())
