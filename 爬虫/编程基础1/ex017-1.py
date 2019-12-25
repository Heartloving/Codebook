#Generator函数:使用一般方法求Fibonacci数列的前N项
def fab(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
