#Generator函数:使用yield函数求Fibonacci数列的前N项
def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        #print(b)
        a,b=b,a+b
        n=n+1
