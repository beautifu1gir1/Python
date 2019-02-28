import yagmail

def sedEmpMail(title,content,tomail):
    #构建邮件发送对象
    mailObj = yagmail.SMTP(user="1543949877@qq.com",password="yejqpmdczdhujjgb",host="smtp.qq.com")

    #发送邮件
    mailObj.send(tomail,title,content)

    print("------发送成功---------")