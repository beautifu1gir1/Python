# 1.连接数据库 导入模块
import pymysql as pm

#2.声明一个连接对象
conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")
print(conn)

#获取操作数据库的游标对象      连接的对象
dboperator = conn.cursor()

# 执行sql语句
sql="INSERT INTO t_students(sname,spwd,sphone,sface,saddress,ssex)" \
    "VALUES(%s,%s,%s,%s,%s,%s);"

dboperator.execute(sql,("孙琰","123456","18751810006","a6.jpg","徐州","男"))

#提交插入的数据到数据库  python操作数据 是手动  ，就需要你commit()
#insert   into|  update |delete
conn.commit()