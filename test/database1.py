# coding=utf-8

# 例子1 利用MySQL-python
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='z2457098495924',
    db='test',
)

cur = conn.cursor()

# 创建数据表 student
# cur.execute('create table student(id int, name varchar(20), class varchar(30), age varchar(10))')

# 增
# cur.execute("insert into student values('1','Tom','3 year 2 class','9')")

# 查
cur.execute("select * from student where id=%s", ('1',))
list = cur.fetchall()
print list


# 改
# cur.execute("update student set class='3 year 1 class' where name='Tom'")



# 关闭游标
cur.close()

# 提交事务
conn.commit()

# 关闭数据库
conn.close()



