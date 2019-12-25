#ex2-1: 

import requests

response  = requests.get("https://www.baidu.com")

print(type(response))
print("")
#print(type(response.text))
#print(response.text)

print(type(response.content))
print(response.content)

print(type(response.content.decode("utf-8")))
print(response.content.decode("utf-8"))

'''
response.headers

response.headers['content-type']
response.cookies


'''
