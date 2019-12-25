#网页解释
#创建beautifulsoup对象

from bs4 import BeautifulSoup
import re 

html_doc = """  
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p class="title"><b>The Dormouse's story</b></p>  
<p class="story">Once upon a time there were three little sisters; and their names were  
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,  
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;  
and they lived at the bottom of a well.</p>  
<p class="story">...</p>  
"""


#根据HTML网页字符串创建beautifulSoup对象
soup = BeautifulSoup(
    html_doc,               #HTML文档字符串
    'html.parser' ,          #HTML解释器
    #from_encoding='utf8'    #HTML文档的编码
    )

#搜索节点（find_all,find）
#方法： find(name, attrs, string)
'''
#查找所以标签为a的节点
s1=soup.find_all('a')
print(s1)




#查找所有标签为div，class为abc，文字为Python的节点
s2=soup.find_all('a',class_='sister',string='Tillie')
print(s2)

#获取查找到的节点的标签名称
#node.name
print(s2[0].name)
#获取查找到的a节点的href属性
#node['href']
print(s2[0]['href'])

#获取查找到的a节点的链接文字
#node.get_text()
print(s2[0].get_text())

#-----------
print("获取所有的链接")
links = soup.find_all('a')  #a标签
for link in links:
    print(link.name,link['href'],link.get_text())

#只获取href=http://example.com/lacie的链接
print("获取lacie链接")
link1 = soup.find('a',href="http://example.com/lacie")
print(link1)
print(link1.name," ***  ",link1['href']," ***  ",link1.get_text())
'''
#正则表达式实现模糊匹配
print("正则匹配 href中带有“ill”的")
import re #导入re包
link2 = soup.find('a',href=re.compile("ill"))

print(link2.name,link2['href'],link2.get_text())

#P段落文字，获取指定class的内容
link3 = soup.find('p',class_="title") #class是关键字 需要加_
print(link3.name,link3.get_text())

