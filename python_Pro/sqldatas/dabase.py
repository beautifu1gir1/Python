import pymysql

#定义一个连接数据的方法
def connDB():
    conn = pymysql.connect(host="127.0.0.1", port=3306, database="njpi", user="root", password="root",
                           charset="utf8")
    return conn


#定义一个学生登录验证并查询的方法
def checkLoginDB(name,pwd):

    result=""

    conn = connDB()

    dbcursor = conn.cursor()

    sql="SELECT  stata FROM t_students WHERE sname=%s AND spwd=%s"

    dbcursor.execute(sql,(name,pwd))

    data = dbcursor.fetchone()

    print(data)
    #print(type(data))

    if data is None:
        result="None"

    elif data[0] == 2:
        result="已毕业"

    elif data[0] == 3:
        result = "休学"

    elif data[0] == 1:
        sql = "SELECT  scid FROM t_students WHERE sname=%s AND spwd=%s"

        dbcursor.execute(sql, (name, pwd))

        sdata = dbcursor.fetchone()

        print(sdata)
        #print(type(sdata[0]))
        result=sdata[0]

    return result
#checkLoginDB("孙婕","12345")