#ex011.py:用递归函数遍历目录
import os

def VisitDir(path):
    ls=os.listdir(path)
    for p in ls:
        pathname=os.path.join(path,p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print(pathname)

if __name__=="__main__":
    path="D:\courses\python"
    VisitDir(path)
