import  cx_Oracle as cxo

conn = cxo.connect("student/student@127.0.0.1/XE")
dbcursor = conn.cursor()

sql="select round(ssalary/(select sum(ssalary) from t_students),3)" \
    " from t_students where sname='孙婕'"

dbcursor.execute(sql)
data = dbcursor.fetchone()

#print(data)     #(0.155,)
print("{0}".format(data))   #(0.155,)
print("%s"%(data))      #0.155

def connDB():
    conn = cxo.connect("student/student@127.0.0.1/XE")
    dbcursor = conn.cursor()
    return dbcursor

def getPageDatas(pageNub):
    #conn = connDB()
    #dbcursor = conn.cursor()
    dbcursor = connDB()

    sql="select * from (select rownum rm ,e.* from t_students e where  rownum<=:endNub)" \
        " tmp where tmp.rm>:startNub"

    pages={"endNub":pageNub*3,"startNub":(pageNub-1)*3}
    dbcursor.execute(sql,pages)

    datas = dbcursor.fetchall()

    print(datas)
    print(datas[0])
    print("{0}".format(datas))
    for values in datas:
        print("{0}".format(values))
        #print("%s"%values)  错的

getPageDatas(2)