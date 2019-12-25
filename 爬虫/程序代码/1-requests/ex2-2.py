#ex2-2: requests的get请求

#基本GET请求
import requests

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.text)
print(type(response.content))
print(response.content.decode("utf-8"))

#带参数的GET请求
#import requests

response1 = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response1.text)
print(response1.content.decode("utf-8"))

#如果我们想要在URL查询字符串传递数据，
#通常我们会通过httpbin.org/get?key=val方式传递。
#Requests模块允许使用params关键字传递参数，以一个字典来传递这些参数

#import requests
data = {
#    "name":"zhaofan",
    "name":None,
    "age":22
}
response2 = requests.get("http://httpbin.org/get",params=data)
print(response2.url)
print(response2.text)
