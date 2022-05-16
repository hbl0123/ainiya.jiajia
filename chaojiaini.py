print("爱你呀,尹琪佳")
'''a = int(input('输入一个数字小于十')
    print(a)
b = []
c = True
if  b :
    print ('nihao')
if c :
    print ("你好呀")
d = 10
if 3<d<100 :
    print ("aini")
if(d = 1):
    print ("sha")'''
'''s = input("输入一个数字")
if int (s)<10:
    print ("s是小于十的数")
else:
    print("s是小于10的数")
s = 99
print ("s是大于10的数字"if int(s)>10 else"s是小于十的数字")
s = int(input("输入一个数字"))
if s>10:
    print("niahoya 很高兴见到你")'''
#2022年5月1号
#测试选择结构的的嵌套
'''score = int(input("输入一个1~100的数字"))
grade = ''
if score >100 or score <0:
    score = input ("请重新输入一个1~100的数字")
else:
    if(score >= 90):
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        garde = "D"
    else:
        grade = "E"
        print("分数为{0}，等级为{1}".format(score,grade))
''''''
score = int (input("输入数字"))
degree = "ABCDE"
num = 0
if score > 100 or score < 0:
    print("在输入一个数字")
else:
    num = score//10
    if num < 6:
        num = 5
    print ("分数是{0},等级是{1}".format(score,degree[9-num]))
#一定要注意缩进问题，不然会导致代码错误'''
'''num = 0
while num <10:
    print (num)
    num += 1
#计算1~100之间数字的累加和
num  = 0
sum_all = 0
while num<=100:
    sum_all = sum_all + num
    num +=1
print(sum_all)
#计算1~100之间数字的和，偶数和，奇数和
sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(101):
    sum_all += x
    if x % 2 == 1:
        sum_odd +=x
    else:
        sum_even +=x
print ("总和{0}，奇数和{1}，偶数和{2}".format(sum_all,sum_odd,sum_even))

for x in range(5):
    for y in range(5):
        print(x,end = "\t")
    print()
#用字典和列表来实现表格的打印
r1 = dict(name = "高效1",age = "18",salary= 30000,city = "北京"  )
r2 = dict(name = "高效2",age = "19",salary= 20000,city = "上海"  )
r3 = dict(name = "高效3",age = "20",salary= 15000,city = "深圳"  )

tb = [r1,r2,r3]
for x in tb:
    if x.get("salary") > 15000:
        print(x)

#要求输入员工的薪资，若薪资小于0则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
empNum = 0  #员工人数
salarySum = 0   #薪资总和
salarys = []    #员工薪资，
while True:
    s = input("请输入员工的薪资（按Q或q结束）")
    if s.upper() == "Q":
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    empNum +=1
    salarys.append(float(s))
    salarySum +=float(s)

print ("员工数{0}".format(empNum) )
print ("录入薪资：",salarys)
print ("平均薪资{0}".format(salarySum/empNum))
'''
#测试zip()并行迭代
'''
for i in [1,2,3]:
    print(i)

names = ("你哈",'你好呀',"宝宝","好喜欢你")
ages = (12,20,30,20)
jobs = ("niha","nihaoya","baobao","haoxihuani")

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))
#利用数组进行访问
for i in range(3):
        print("{0}-{1}--{2}".format(names[i],ages[i],jobs[i]))
'''

#两种不同的方式来写这个循环语句
'''
y = [x*2 for x in range(1,50) if x%5==0]
print(y)
y = []
for x in range(1,50):
    if x%5==0:y.append(x*2)
print(y)

#字典推导式
my_text = 'i love you, i love 尹琪佳，i love 尹琪佳'
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

#使用普通循环实现上面的推导式（我忒笨了，没有写出来，知识不够熟练）
char_count = {}
my_text = "i love you,i love 尹琪佳，i love 尹琪佳"
for c in my_text:
    my_text.count(c).hash(my_text)
print(char_count)
'''
#画⚪的形状
'''
import turtle
t = turtle.Pen()
t.width(4)
t.speed(0)
my_colors = ("red","blue","yellow","green")
for i in range(50):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(10 * (i + 1))
turtle.done()

#画18*18的棋盘
import turtle
q = turtle.Pen()
q.speed(0)
q.width(3)
for j in range(19):
    q.penup()
    q.goto(-300,300-20*j)
    q.pendown()
    q.goto(60,300-20*j)
for y in range(19):
     q.penup()
     q.goto(-300+20*y,300)
     q.down()
     q.goto(-300+y*20,-60)

turtle.done()
'''
#测试函数的定义和调用
'''
def test01():
    print("*"*10)
    print("0"*10)

test01()
for x in range(10):
    test01()
'''
#利用函数比较大小
'''
def printMAx(a,b):
    if a>b:
        print(a,"较大值")
    if b>a:
        print(b,'较大值')

printMAx(10,20)
printMAx(50,30)
help(printMAx.__doc__)
'''
#测试返回值的基本用法
def add(a,b):
    print("计算两个数的和：{0}，{1}，{2}".format(a,b,(a+b)))
    return a+b
def test02():
    print("set")
    print("gao")

    return

    print("hello")
c = add(20,50)
print(c*10)
test02()
print(test02())

def test03(a,b,c):
    return [a*10,b*10,c*10]

print(test03(10,20,30))