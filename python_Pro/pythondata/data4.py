tup1 =(1,2,3)       #int组成的元祖
print(tup1)
print(type(tup1))
print(id(tup1))

print("-------------")
tup2 =(1,2,3)
print(tup2)
print(type(tup2))
print(id(tup2))

print("-----------")
print( tup1 == tup2)
print(tup1 is tup2)

#元祖是定长定值的
print(tup1[1])
print(len(tup1))

print("-----------")
'''tup1[0]=4           #'tuple' object does not support item assignment     元祖不能改变值和长度
print(tup1)'''

#元祖类型的遍历
tup3 =("a","b","c")     #string组成的元祖
for key in tup3:
    print("每一个数值为：",key)

print("----------")

tup4=tup3,tup1
print(tup4)
print(type(tup4))

print("------------")
tup5=tup3+tup1
print(tup5)
print(type(tup5))

print("----------")
#求和
a2=(1,"2",3,"8")
print(a2)
print(type(a2))
a1=a2[0]+int(a2[1])+a2[2]+int(a2[3])
print(a1)
print(type(a1))

