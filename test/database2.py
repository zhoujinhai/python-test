# coding=utf-8

# 例子2 利用mysql-connector-python

# 导入MySQL驱动
import mysql.connector

from io import IOBase

conn = mysql.connector.connect(host='localhost', user='root', password='z2457098495924', database='test')

cur = conn.cursor()
cur.execute('select * from student')
result = cur.fetchall()
print result

# cur.execute("insert into student (id, name, class, age) values (%s, %s, %s, %s)", ['2', 'Jerry', '3 year 2 class', '10'])

conn.commit()
cur.close()
conn.close()

