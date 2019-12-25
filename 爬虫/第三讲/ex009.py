#ex009.py:修改文件后缀名
import os

files=os.listdir('.') #返回当前目录的文件列表
#print(type(files))
#print(files)
print(" ")
for filename in files:      #获取当前目录中的每个文件名
    #print(type(filename))
    #print(filename)
    pos = filename.find('.')  #查找'.'的所在位置
    #print(type(filename[pos+1:]))
    #print(filename[pos+1:])
    #print(" ")
    if filename[pos+1:]=='html':  #判断后缀是否为html
        newname=filename[:pos+1]+'htm'  #若是html，则该为htm
        os.rename(filename,newname)   #重命名
