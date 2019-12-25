'''
#=============================
#1---cookies

import requests

response = requests.get("https://www.baidu.com")
print(response.cookies)
print(response.cookies.items())
for key, value in response.cookies.items():
    print(key + '='+value)

#=============================
#2---回话维持
#cookies的主要作用就是登陆网址用的

import requests

requests.get("http://httpbin.org/cookies/set/number/123456789")
#设置一个cookies
response =  requests.get("http://httpbin.org/cookies")
#获取cookies
print(response.text)

#requests的Session对象，模拟了一个回话

import requests

s=requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
#设置一个cookies
response =  s.get("http://httpbin.org/cookies")
#获取cookies
print(response.text)

#=================================
#3---证书验证

import requests

response = requests.get("https://www.12306.cn")
print(response.status_code)

#--------
import requests

response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)

#---------
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn",verify=False)
print(response.status_code)
#导入原生的urllib3包，通过它来消除警告信息


#=============================
#5----超时设置
import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get("http://www.microsoft.com",timeout=0.1)  #单位：秒
    print(response.status_code)
except ReadTimeout:
    print("Time out")






