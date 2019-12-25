import sqlite3

con = sqlite3.connect("sales1.db") #创建SQLite数据库：sales1.db

con.execute("create table region(id primary key, name)") 
            #创建表：regions，包含2个列，id（主码）和name

