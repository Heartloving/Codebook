#关键字参数

def shop(where ='store',what='pasta',howmuch='10 pounds'):
    print('I want you to go to the',where,'and buy',howmuch,'of', what+'.')
    
shop()
shop(what='towels')
shop(howmuch='a ton',what='towels')
shop(howmuch='a ton',what='towels',where='bakery')
