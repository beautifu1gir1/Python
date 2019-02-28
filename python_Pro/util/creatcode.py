import random

def creatcode(clen):
    codeValue=[]
    #生成四位数的验证码
    while len(codeValue)<(clen):
        code = random.randint(0,9)

        #验证是否重复
        if code not in codeValue:
            codeValue.append(code)

    print("验证码数组-->",codeValue)

    codestr=""
    for item in codeValue:
        codestr+= str(item)

    print("验证码-->",codestr)
    return codestr
#creatcode(4)
