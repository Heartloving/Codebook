#dbmaccess.py： 访问持久字典
import dbm

#open existing file
db=dbm.open('websites','c')

#add another item
db['www.baidu.com']='Baidu home page'
'''
#verity the previous item remains
if db['www.python.org']!=None:
    print('Found www.pyhton.org')
else:
    print('Error: Missing item')
'''
#Iterate over the keys.May be slow
#May use a lot of memory
for key in db.keys():
    print("key= ",key, " value= ",db[key])

del db['www.baidu.com']
print('After deleting www.baidu.com,we have: ')
          
for key in db.keys():
    print("key= ",key, " value= ",db[key])

#close and save to disk
db.close()
