#爬虫的异常处理

#import urllib.request
#import urllib.error

from urllib import request,error
try:
    response=request.urlopen("http://www.oschina.net/")
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    #print(e.headers)
except error.URLError as e:
    print(e.reason)
else:
    print("reqeust successfully")


'''
from urllib import request,error
try:
    response=request.urlopen("http://www.oschina.net/")
except error.URLError as e:
    if hasattr(e,"code"):  
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
'''
