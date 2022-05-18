#return 的作用
'''
def add(a,b):
    print("计算两个数的和:{0},{1},{2}".format(a,b,a+b))

    return a+b
    print("zaijian")
def test():
        print("nihaoya ,佳佳")
c = add(10,9)
print(c)
print(add(20,40)*10)
test()
#如果要返回多个值可以用列表,元组，字典，集合等
def test02(z,x,c):
    return (z*10,x*8,c*9)
b  =  test02(10,3,8)
print(b)
print(test02(10,3,8))

#测试函数也是对象
def test():
    print("sxtsxt")
test()
c = test
c()

print(id(test))
print(id(c))

#全局变量与局部变量

a = 3   #全局变量

def test():
    b = 4   #局部变量
    print(b*10)

test()
print(a)
print(b)
'''
