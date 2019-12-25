#urllib超时设置

import urllib.request

file=urllib.request.urlopen("http://www.ucas.ac.cn",timeout=0.01)
print(file.status)


