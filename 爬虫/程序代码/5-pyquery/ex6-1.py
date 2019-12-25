#pyquery
"""
#1---安装验证
print('1---安装验证')
from pyquery import PyQuery as pq
d = pq("<html>hello world</html>")
result = d('html').text()     #寻找html标签
print(d)   #<html>hello world</html>
#print(dir(d))
print(type(d))    #<class 'pyquery.pyquery.PyQuery'>
print(type(result)) #<class 'str'>
#print(dir(result))
print(result,'\n')   # hello world


#2---字符串的初始化
print('2---字符串的初始化')
from pyquery import PyQuery as pq
 
html = '''<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''
 
doc = pq(html)
#print(doc)
#print(type(doc))
print(doc('li'))
print(doc('li').text(),'\n')

#3---打开html文件
print('3---打开html文件')
#注意路径问题

from pyquery import PyQuery as pq
doc = pq(filename='index.html')
#print(doc)
print(doc('head'),'\n')
"""
#4---打开某个网站

print('4---打开某个网站')
from pyquery import PyQuery as pq

doc = pq('https://www.baidu.com',encoding='utf-8')#有乱码，需要用utf-8
#doc1 = pq(url='https://www.baidu.com')
print(type(doc('head')))
print(doc('head'),'\n')  

