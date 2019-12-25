#ex005.py:文件删除

#open('hello1.txt','w')
import os
if os.path.exists('hello2.txt'):
    os.remove('hello2.txt')
