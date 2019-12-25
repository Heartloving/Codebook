#ex011.py:使用os.walk()遍历目录
import os

def VisitDir(path):
    for root,dirs,files in os.walk(path):
        print("root=",root)
        print("dirs=",dirs)
        print("files=",files,'\n')
        for filepath in files:
            print(os.path.join(root,filepath),'\n')

if __name__=="__main__":
    path="D:\courses\python"
    VisitDir(path)
