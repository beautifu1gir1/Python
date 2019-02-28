# 1.导入Python web  flask  应用框架
from flask import Flask
from flask import request
from flask import jsonify
from sqldatas.sface import *

#2.创建 flask web 应用对象
wxapp = Flask(__name__)
print(__name__)

#4.用户在客户端发起一个请求，并执行构造的方法
@wxapp.route("/queryface")
def queryUserFace():
    #获取用户请求的数据
    name = request.args.get("username")
    print("接收到的值为：",name)

    #去查询数据库
    userImgPath = queryFacePath(name)
    userImgPath = "http://4qm4hs.natappfree.cc/static" + userImgPath

    #jsonify()把一个字段转换成json数据格式
    return jsonify({"imagePath":userImgPath})

#3.找到应用的入口
if __name__ == "__mian__":
    wxapp.run(debug=True,port=8090)


