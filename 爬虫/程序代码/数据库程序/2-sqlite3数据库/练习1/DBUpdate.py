import sqlite3
regions = [("021", "上海"),('022', "天津"),("023", "重庆"),("024", "沈阳")]

con = sqlite3.connect("sales1.db")

#使用不同的方法分别插入一行数据
#con.execute("insert into region(id, name) values ('020', '广东')")
#con.execute("insert into region(id, name) values (?, ?)", ('001', '北京'))

#插入多行数据
#con.executemany("insert into region(id, name) values (?, ?)", regions)

#con.execute("update region set name=? where id=?", ('广州','020')) #修改一行数据

n=con.execute("delete from region where id=?", ("021",)) #删除一行数据

print('删除了', n.rowcount, '行记录')

con.commit()           #提交
con.close()            #关闭数据库
