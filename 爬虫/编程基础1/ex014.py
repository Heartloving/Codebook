#嵌套函数定义1：
def func():
    x=1
    y=2
    m=3
    n=4
    def sum(a,b):
        return a+b
    def sub(a,b):
        return a-b
    return sum(x,y)*sub(m,n)
