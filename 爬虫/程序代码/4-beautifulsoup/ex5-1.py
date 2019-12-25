#ex5-1: beautifulsoup
#BeautifulSoup默认支持Python的标准HTML解析库，但是它也支持一些第三方的解析库

#1---创建对象
print("1--创建对象")
#导入库：

from bs4 import BeautifulSoup
import urllib.request 
'''
#创建实例：

url='http://www.baidu.com'
resp=urllib.request.urlopen(url)
html=resp.read()

#创建对象：

bs=BeautifulSoup(html,"lxml") #最常用的解析库

#格式化输出内容：
#print(bs.prettify()) #对输入的html文件进行补全，格式化
print(type(bs.prettify()))
print(bs.title.string)  #将title中的内容输出
print(bs.title)

'''


html1='''
<a class="css1" href="http://example.com/cdd" id="css">abc<!--def -->bgh</a>
<b class="css1" href="http://example.com/cdd" id="css">abc<!--def -->bgh</a>

'''
bs1=BeautifulSoup(html1,"html.parser")

#内容是注释和字符串混合，此时可以用contents获取全部对象：

for i in bs1.a.contents:
    print(i)            
print('\n')


#如果需要不想输出注释内容的话，可以利用get_text()或者.text：

print(bs1.a.get_text())   

#传入正则表达式：
import re
print(bs1.find_all(re.compile('^b'))) 
#所有以b开头的标签对象都会被找到。
