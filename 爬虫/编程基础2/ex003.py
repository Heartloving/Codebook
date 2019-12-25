#ex003.py: 使用read()返回指定字节的内容
f=open('story.txt')
context=f.read(5)  #读取文件前5个字节的内容
print(context)
print(f.tell())    #返回文件对象当前指针的位置

context=f.read(10) #继续读取10个字节的内容
print(context)
print(f.tell())    #输出文件当前的位置

f.close()
