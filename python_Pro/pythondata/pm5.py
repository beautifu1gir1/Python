import  pymysql

def dele(* args):
    conn=pymysql.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    dbcursor=conn.cursor()

    sql="DELETE FROM t_students WHERE sid=%s"

    dbcursor.execute(sql,args)

    conn.commit()

dele("1")