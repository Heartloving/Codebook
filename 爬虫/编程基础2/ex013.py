#ex013.py: 类的定义
class Person(object):
    #Class to represent a person
    def __init__(self): #类的构造函数
        self.name=''
        self.age=0
    def display(self):  #类中定义的方法
        print("Person(%s,%d)"%(self.name,self.age))
