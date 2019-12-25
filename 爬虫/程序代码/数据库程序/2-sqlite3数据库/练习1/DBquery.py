import sqlite3   

con = sqlite3.connect("sales1.db")  #打开SQLite数据库：sales.db 

cur = con.execute("select id, name from region")
                  #查询数据库表的记录内容

for row in cur:   #循环输出结果
    print(row)
con.close()
