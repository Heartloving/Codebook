#ex007.py:使用shutil模块实现文件的复制和移动
import shutil

#将hello.txt的内容复制给hello2.txt
shutil.copyfile('hello.txt','hello2.txt')

#将hello2.txt移动到当前目录的父目录
shutil.move('hello2.txt','../')

#将hello.txt移动到当前目录，重命名为hello3.txt
shutil.move('hello.txt','hello3.txt')

