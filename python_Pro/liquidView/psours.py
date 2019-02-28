import pymysql as pm

def  queryEmpSex(* args):
    conn = pm.connect(host="127.0.0.1",port=3306,database="demo",user="root",password="root",charset="utf8")

    dbcursor = conn.cursor()
    sql = "SELECT COUNT(*),ssex	FROM t_students	   GROUP BY  ssex"

    dbcursor.execute(sql,args)

    datas = dbcursor.fetchall()

    print(datas)
    return datas