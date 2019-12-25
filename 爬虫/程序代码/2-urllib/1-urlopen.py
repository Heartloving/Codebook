#ex1-1：urlopen
import urllib.request

response = urllib.request.urlopen('http://www.ucas.ac.cn')
#返回一个response对象，保存返回的信息

print(type(response))

#print(response.read()) #输出的内容太多，一般不用执行

#print(response.read().decode('utf-8'))

print(response) 

