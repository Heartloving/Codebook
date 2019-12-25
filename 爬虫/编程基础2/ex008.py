#ex008.py:修改文件名
import os

ls=os.listdir('.') #返回当前目录的文件列表
print(ls)
if 'hello3.txt' in ls:
    os.rename('hello3.txt','hello.txt')
