#查询一个数据库，而且可以创建一个新的数据库，在新数据库中创建表


import pymysql
 
connect = pymysql.connect(    #连接数据库服务器
    user="test",
    password="test",
    host="127.0.0.1",
    port=3306,
    db="TESTDB",
    charset="utf8"
    )
conn = connect.cursor()        #创建操作游标
''' 
#                          查看
conn.execute("SELECT * FROM user")    #选择查看自带的user这个表  (若要查看自己的数据库中的表先use XX再查看)
rows = conn.fetchall()                #fetchall(): 接收全部的返回结果行，若没有则返回的是表的内容个数 int型
for i in rows:
    print(i)
 
#                          创建表
conn.execute("drop database if exists new_database")   #如果new_database数据库存在则删除
conn.execute("create database new_database")   #新创建一个数据库
'''
conn.execute("use new_database")        #选择new_database这个数据库
# sql 中的内容为创建一个名为new_table的表
sql = """create table new_table(id BIGINT,name VARCHAR(20),age INT DEFAULT 1)"""  #()中的参数可以自行设置
#conn.execute("drop table if exists new_table") # 如果表存在则删除
conn.execute(sql)   # 创建表
 
#                           删除
# conn.execute("drop table new_table")

conn.close()           #   关闭游标连接
connect.close()        #   关闭数据库服务器连接 释放内存
 

