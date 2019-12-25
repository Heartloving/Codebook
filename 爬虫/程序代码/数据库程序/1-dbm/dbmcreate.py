#dbmcreate.py：创建持久字典

import dbm
db=dbm.open('websites','c') #第一个参数是数据库名，第二个参数是打开方式

db['www.python.org']='Pyhton home page' #写入一个数据

print(db['www.python.org'])  #访问一个数据

db.close()  #关闭并保存

