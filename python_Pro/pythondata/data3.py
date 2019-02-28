s1 = True           #1
s2 = False          #0
print(type(s1))

print("----------")
s3 = s1+1           #bool可以执行运算
print(s3)
print(type(s3))

s4 ="111"
s5=s4+str(s1)
print(s5)           #bool和str之间不能直接运算，要类型转换
print(type(s5))