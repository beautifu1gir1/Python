# 1.导入Python web  flask  应用框架
from  flask import Flask
from flask import jsonify
from flask import request
from util.creatcode import *
from graduation.dboper import *


#2.创建 flask web 应用对象
wxapp = Flask(__name__)
print(__name__)

#4.用户在客户端发起一个请求，并执行构造的方法

#验证码功能
@wxapp.route("/code")
def sedcode():
    print("-------")

    codeVal = creatcode(4)
    return jsonify({"codeValue":codeVal})

#验证学生信息
@wxapp.route("/checklogin")
def checkLogin():
    # 接受客户端数据,获取请求参数
    usernumb = request.args.get("usernumb")
    userpwd = request.args.get("userpwd")

    print(usernumb, userpwd)

    result = checkLoginDB(usernumb, userpwd)
    print(result)

    return jsonify({"rescheck":result})

#学生注册
@wxapp.route("/register")
def register():
    #客户端获取的值
    username = request.args.get("username")
    usernumb = request.args.get("usernumb")
    userpwd = request.args.get("userpwd")
    userphone = request.args.get("userphone")
    usersex = request.args.get("usersex")
    userclass =request.args.get("userclass")

    scid = int(userclass) + 1
    scid = str(scid)
    #print(type(userclass))
    print(scid)
    #val=[usernumb,username,userpwd,usersex,scid,userphone]
    #print(username,usernumb, userpwd,userphone,usersex,userclass)
    #print(val)

    resdatas = registerDB(usernumb,username,userpwd,usersex,scid,userphone)
    print(resdatas)

    return jsonify({"resregister":resdatas})
#3.找到应用的入口
if __name__ == "__main__":
    wxapp.run(debug=True,port=8090)
