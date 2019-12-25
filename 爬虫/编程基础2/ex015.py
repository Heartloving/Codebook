#ex015.py: 对象的显示方法
class Person(object):
    #Class to represent a person
    def __init__(self): #类的构造函数，用于初始化对象
        self.name=''
        self.age=0
    def display(self):  #类中定义的方法
        print("Person(%s,%d)"%(self.name,self.age))

    def __str__(self):  
        return "Person(%s,%d)"%(self.name,self.age)

    def __repr__(self):  
        return "Person(%s,%d)"%(self.name,self.age)


if __name__=='__main__':
    p=Person()
    print(p)
    print(p.age)
    print(p.name)
    p.age=25
    p.name='Jack'
    p.display()
    print(str(p))
    print(repr(p))
    print(p)
