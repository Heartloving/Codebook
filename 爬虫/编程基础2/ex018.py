#ex018.py:实例变量和类变量
class Fruit(object):
    price = 0 #类属性

    def __init__(self):
        self.color='red' #实例属性
        zone ='China'    #局部变量

if __name__=='__main__':
    print(Fruit.price)   #使用类名调用类变量
    apple=Fruit()        #实例化apple
    print(apple.color)
    Fruit.price +=10    #将类变量加10
    print("apple's price:" + str(apple.price))

    banana=Fruit()
    banana.color='yellow'
    print(banana.color)
    print(Fruit.price)
    print("banana's price:"+str(banana.price))
