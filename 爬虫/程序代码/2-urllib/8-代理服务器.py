#代理服务器

import urllib.request

#定义实现代理服务器功能的函数
def use_proxy(url,proxy_addr): 
    proxy=urllib.request.ProxyHandler({"http":proxy_addr})

    #要使用代理，需要使用opener。
    #第一个参数是IP，第二个参数是http处理器
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)

    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data

proxy_addr="........" 

url="http://www.baidu.com"  
data=use_proxy(url,proxy_addr)
print(len(data))
#print(data)
    

