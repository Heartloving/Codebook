#嵌套函数定义2
def linear(a, b):
    def result(x):              #在Python中，函数是可以嵌套定义的
        return a * x + b
    return result               #返回可被调用的函数
