# 1.导入Python web  flask  应用框架
from flask import Flask
# 渲染一个模板
from flask import render_template   #跳转到py内的HTML
from flask import jsonify
from flask import request
from sqldatas.sface import *
from sqldatas.dabase import *
from util.sendmail import *
from util.creatcode import *
import os
from werkzeug.utils import secure_filename
import time

# 2.创建 flask web 应用对象
wxapp = Flask(__name__)
print(__name__)

#4.用户在客户端发起一个请求，并执行构造的方法
@wxapp.route("/")
def defaultView():
    print("-----加载首页-----")
    return "哈哈哈哈"

@wxapp.route("/default")
def loginView():
    return render_template("login.html")

@wxapp.route("/login")
def checkLogin1():
    return jsonify({"flag":"5"})

@wxapp.route("/queryface",methods = ["POST","GET"])
def queryUserFace():
    #获取用户请求的数据

    name = request.args.get("username")     #username为小程序内data键
    print("接收到的值为：",name)

    #去查询数据库
    userImgPath = queryFacePath(name)
    userImgPath = "http://8hmb6d.natappfree.cc/static" + userImgPath

    userInformation = queryinfor(name)


    #jsonify()把一个字段转换成json数据格式
    return jsonify({"imagePath":userImgPath,"userInfor":userInformation})

@wxapp.route("/queryinfor")
def  queryUserAllInfor():
    # 获取用户请求的数据
    name = request.args.get("username")
    print("输入的用户名为：" , name)

    datas = queryinfor(name)

    userInfor={}

    userInfor["sphone"] = datas[0]
    userInfor["saddress"] = datas[2]
    userInfor["sex"] = datas[3]
    userInfor["sface"] = "http://pnfssm.natappfree.cc/static" + datas[1]
    userInfor["mimage"] = "http://pnfssm.natappfree.cc/static" + datas[4]
    userInfor["audio"] = "http://pnfssm.natappfree.cc/static" + datas[5]
    userInfor["video"] = "http://pnfssm.natappfree.cc/static" + datas[6]

    print(userInfor)

    return jsonify({"userInformation":userInfor})

#用户名是否存在
@wxapp.route("/checkuser")
def checkUserName():
    name = request.args.get("username")
    print("输入的姓名为：",name)

    data = checkDBUser(name)

    value=""

    if data == 0:
        value="ok"
    else:
        value="no"

    return jsonify({"flag":value})

#学生通讯录
@wxapp.route("/querylist")
def queryAllInfor():
    #直接查询数据
    list = queryDBAll()
    #print(list)

    studentlist =[]

    for data in list:
        stulist ={}

        stulist["name"] = data[0]
        stulist["phone"] = data[1]
        stulist["mail"] = data[2]+"@qq.com"
        stulist["img"] = "http://n23d87.natappfree.cc/static/usering/" + data[3]

        studentlist.append(stulist)

    #print(studentlist)
    return jsonify({"list":studentlist})

#发送邮件
@wxapp.route("/sendmail")
def sendEmailTo():
    print("------接受发送邮件的参数--------")

    title = request.args.get("mailtitle")
    content = request.args.get("mailcn")
    mailnum = request.args.get("mailnum")

    print(title, content, mailnum)

    sedEmpMail(title,content,mailnum)


    return jsonify({"flag":"发送成功"})

#传轮播图和验证码
@wxapp.route("/int")
def sendPicCode():
    print("-------初始化--------")

    codeVal = creatcode(4)

    return  jsonify({"codeValue":codeVal},{"changeImgPath":["http://n23d87.natappfree.cc/static/usering/8.jpg",
                                                            "http://n23d87.natappfree.cc/static/usering/9.jpg",
                                                            "http://n23d87.natappfree.cc/static/usering/10.jpg"]})

#重新请求验证码
@wxapp.route("/restcode")
def ResetLoadCode():
    print("重新生成验证码")

    codeVal = creatcode(4)

    return jsonify({"codeValue": codeVal});


#验证学生的状态
@wxapp.route("/checklogin")
def checkLogin():
    #接受客户端数据,获取请求参数
    username = request.args.get("username")
    userpwd = request.args.get("userpwd")

    print(username,userpwd)

    result = checkLoginDB(username,userpwd)

    print(result)

    return jsonify({"checked":result})

#上传图片
@wxapp.route("/upload",methods=["POST","GET"])
def getUpLoad():
    print("开始上传文件")

    if request.method =="POST":
        #获取上传的文件
        getuploadFils = request.files["fileimages"]
        print("getuploadFils",getuploadFils)

        #获取上传的文件名
        upFileName = getuploadFils.filename
        print("upFileName--->",upFileName)

        #获取文件后缀名
        splitNames = os.path.splitext(upFileName)
        print("splitNames-->", splitNames)
        #print(type(splitNames))

        #重新命名获取来的文件
        print("现在的时间：",time.localtime())
        timeName = time.strftime("%Y%m%d%H%M%S",time.localtime())
        #print(timeName)
        #print(type(timeName))

        codeVal = creatcode(4)
        #print(type(codeVal))

        newFileName=timeName+"_"+codeVal+splitNames[1]
        print("新的文件名",newFileName)

        #上传到目录      插入数据库
        basePath = os.path.dirname(__file__)
        print("所在目录：",basePath)

        saveFilePath = os.path.join(basePath, 'static/upimg', secure_filename(newFileName))
        print(saveFilePath)

        #将文件保存在saveFilePath
        getuploadFils.save(saveFilePath)

    return jsonify("that'ok")

# 3.找到应用的入口
if __name__ == "__main__":
    wxapp.run(debug=True,port=8090)