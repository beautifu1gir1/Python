import pymysql as pm

#连接数据库的conn
def connDB():
    conn = pm.connect(host="127.0.0.1", port=3306, database="xinxixi", user="root", password="root", charset="utf8")
    dbcursor = conn.cursor()
    return dbcursor

def connect():
    conn = pm.connect(host="127.0.0.1", port=3306, database="xinxixi", user="root", password="root", charset="utf8")
    return conn

#学生登录验证
def checkLoginDB(numb,pwd):

    result =""

    dbcursor = connDB()

    sql="SELECT COUNT(*) FROM t_students WHERE snumber= %s AND spwd = %s"

    dbcursor.execute(sql,(numb,pwd))
    data =  dbcursor.fetchone()

    if data[0] ==1:
        sql = "SELECT  sid FROM t_students WHERE snumber=%s AND spwd=%s"

        dbcursor.execute(sql, (numb, pwd))
        idata = dbcursor.fetchone()

        print(idata[0])
        result=idata[0]
    else:
        result ="失败"
    print(data)
    return result

#学生注册
def registerDB(* args):

    resdata = ""

    conn = connect()
    dbcursor = conn.cursor()

    sql="INSERT INTO t_students(snumber,sname,spwd,ssex,scid,sphone)" \
        "VALUES(%s,%s,%s,%s,%s,%s);"
    returndata = dbcursor.execute(sql,args)

    conn.commit()
    print(returndata)
    if returndata ==1:
        resdata="success"
    else:
        resdata = "fail"

    return resdata















