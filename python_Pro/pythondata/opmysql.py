#1.连接数据库Python--->mysql
#导入模块
import pymysql  # as  pm     as关键字是取一个别名
#声明一个连接对象
'''连接的IP地址：host="127.0.0.1"
    端口号：port=3306,
    数据库名：database="demo",
    用户名及密码：user="root",password="root",
    charset="utf8"'''
connectionObj = pymysql.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")
print(connectionObj)

#2.获取操作数据库的游标对象
dboperator = connectionObj.cursor()

#3.构建sql语句
#sql="select * from t_students"
sql = "select sname,sphone,sface from t_students"
#4.使用游标对象执行sql语句
dboperator.execute(sql)

#5.获取数据    select 查询 fetchall -->查询所有数据
'''alldatas = dboperator.fetchall()
    print(alldatas)'''

print("------------")
#   fetchone --> 查询一条数据
#onedata = dboperator.fetchone()
#print(onedata)

#  查询指定条数据
datas = dboperator.fetchmany(3)
print(datas)