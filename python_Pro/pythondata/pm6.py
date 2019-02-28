# 连接数据库   导入模块
import  pymysql

# 构造方法       count函数
def count(* args):
    conn = pymysql.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    print(conn)
    # 获取操作数据库的游标对象
    dbc = conn.cursor()

    sql="SELECT COUNT(*) FROM t_students WHERE sname=%s AND spwd=%s"

    dbc.execute(sql,args)

    datas = dbc.fetchone()
    print(datas[0])

#  调用方法
count("王岚","123456")