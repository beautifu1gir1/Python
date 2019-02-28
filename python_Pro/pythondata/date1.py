a = 10
print(a)

a1 = input("请输入数值")
print(a1)

def sf():
    print("******")
sf()
'''
input 内是string类型 
如果想要比较，需要强制类型转换 
'''
if int(a1)>0:
    print("a1大于零")
else:print("a1小于零")