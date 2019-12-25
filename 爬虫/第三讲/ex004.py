#ex004.py: 使用writelines()写文件
f1=open('hello1.txt','w+')
f2=open('hello2.txt','w+')

str='hello world!\nhello China!\n' 
context=['hello world!\n','hello China!\n']
f1.writelines(context)
f2.write(str)
f1.close()
f2.close()
