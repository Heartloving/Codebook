# redis


#1---连接方式

'''
import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
r.set('name','baby')
print(r.get('name'))
print(r.dbsize())
'''
#2--连接池

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'zhangsan')   #添加，覆盖前面的baby值
print (r.get('name'))   #获取

