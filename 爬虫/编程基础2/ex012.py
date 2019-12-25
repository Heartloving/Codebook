#ex012.py:返回当前目录中的文件和文件夹
import os

def list_cwd():
    return os.listdir(os.getcwd()) #返回当前目录

def files_cwd():
    return [p for p in list_cwd() #返回当前目录中的文件
            if os.path.isfile(p)]

def folders_cwd():
    return [p for p in list_cwd() #返回当前目录中的文件夹
            if os.path.isdir(p)]
