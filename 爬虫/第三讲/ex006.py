#ex006.py:用read()、write()实现文件复制
#创建文件hello.txt
src=open('hello.txt','w')
context=['hello world!\n','hello China!\n']
src.writelines(context)
src.close()

#将hello.txt复制到hello2.txt
src=open('hello.txt','r')
dst=open('hello2.txt','w')
dst.write(src.read())
src.close()
dst.close()

