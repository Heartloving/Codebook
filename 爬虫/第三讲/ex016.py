#ex016.py:私有成员的访问
class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2
    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2
    def show(self):
        print(self._value1)
        print(self.__value2)
