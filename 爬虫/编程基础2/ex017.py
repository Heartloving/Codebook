#ex017.py: __new__函数使用

class Demo(object):
    total = 0
    def __new__(cls, *args, **kwargs):           #该方法在__init__()之前被调用
        if cls.total >= 3:                       #最多允许创建3个对象
            raise Exception('最多只能创建3个对象')
        else:
            return object.__new__(cls)
    def __init__(self):
        Demo.total = Demo.total + 1	
