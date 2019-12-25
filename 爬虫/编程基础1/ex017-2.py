#Generator函数:使用列表List求Fibonacci数列的前N项
def fab(max):
    n,a,b=0,0,1
    L=[]
    while n<max:
        L.append(b)
        a,b=b,a+b
        n=n+1
    return L
