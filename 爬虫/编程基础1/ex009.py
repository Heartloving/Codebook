#单分支
x = input('Input two number:')
a, b = map(int, x.split())
if a > b:
   a, b = b, a    #序列解包，交换两个变量的值
print(a, b)
