#1.连接数据库   导入数据库
import pymysql

#2.构造方法
def count(* args):
    #声明一个连接对象
    conn = pymysql.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="uft8")

    #获取操作数据库的连接对象
    dbcursor = conn.cursor()

    # 执行的sql语句
    sql="SELECT COUNT(*) FROM t_students WHERE sname=%s AND spwd=%s"

    dbcursor.execute(sql,args)