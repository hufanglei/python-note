def sayhi():
    print("Hello, I'm nobody")

sayhi()

def calc(x, y):
    res = x + y
    print(res)

calc(5, 22)

def sayhi(name, age):
    print(f"hello， my name is {name}， I am {age} old")
    print("ddd")


sayhi("Alex", 22)


def stu_register(name, age, course='PY', country='CN'):
    print("----注册学⽣信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)


stu_register("王⼭炮", course='PY', age=22, country='JP')


def stu_register(name, age, *args):  # *args 会把多传⼊的参数变成⼀个元组形式
    print(name, age, args)


stu_register("Alex", 22)

stu_register("Jack", 32, "CN", "Python")


def stu_register(name, age, *args, **kwargs):  # *kwargs 会把多传⼊的参数变成⼀个dict形式
    print(name, age, args, kwargs)


stu_register("Alex", 22)
# 输出
# Alex 22 () {}#后⾯这个{}就是kwargs,只是因为没传值,所以为空
stu_register("Jack", 32, "CN", "Python", sex="Male", province="ShanDong")
# 输出
# Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'


def print_info(*args, **kwargs):
    print(args, kwargs)

print_info(name="Alex",age=22,sex="M")


def stu_register(name, age, course='PY', country='CN'):
    print("----注册学⽣信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)
    if age > 22:
        return False
    else:
        return True,age,course,country

registriation_status = stu_register("王⼭炮", 21, course="PY全栈开发", country='JP')
print(registriation_status)
if registriation_status:
    print("注册成功")
else:
    print("too old to be a student.")



