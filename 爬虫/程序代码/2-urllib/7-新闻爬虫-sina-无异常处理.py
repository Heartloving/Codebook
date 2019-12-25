#爬取新闻：新浪--无异常处理

import urllib.request
import re
data=urllib.request.urlopen("http://news.sina.com.cn/").read()
data2=data.decode("utf-8")

#data2=data.decode("utf-8","ignore")

pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)
for i in range(0,len(allurl)):
    thisurl=allurl[i]
    file="sinanews1/"+str(i)+".html"
    urllib.request.urlretrieve(thisurl,file)
    

