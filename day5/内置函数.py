# s = ascii("中国")
# print(s)
#
#
# exec("print('hellworld')")
#
# a = [1, 4, 9, 1849, 2025, 25, 36]
# b = ["a", "b", "c", "d"]
# list(zip(a,b))
#
# # abs取绝对值
# print(abs(-10))
# #
# b = [1, 0, 9, 1849, 2025, 25, 36]
#
# print(all(a))
#
# #any 任意一个值为Ture
# print(any(b))
#
# print(chr(97))

# print(dict())
# # dict的另外一种写法
# print(dict(name="alex",age=22))

# name="alex"
# age=22
# #打印内存中所有的变量
# #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'age', 'name']
# print(dir())
# # __file__ 当前文件所在路径
# print(__file__)
#
# #locals（）打印当前程序(作用域) 的所有变量名 & 变量值
# print(locals())

# 一个列表转成map
# map()

l = list(range(10))
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l)

# def calc(x):
#     return x**2  # 平方
#
# print(calc(5))  #只能定义一个参数
# print(calc)
# # 并没有执行
# m = map(calc, l)
# # <function calc at 0x00000158EA633EB0>
# # print(map(calc, l))
# for i in m: #每循环一次，就把列表里的每一个元素扔给Calc函数执行
#     print(i,end=" ") #0 1 4 9 16 25 36 49 64 81

# max
# l = list(range(10))
# print(max(l))
# print(min(l))
# print(sum(l))


# ord 与 chr好像相反
# 60
print(ord("<"))

# #0 0
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
# for index,val in enumerate(range(10)):
#     print(index, val)

# 4.14
# print(round(4.1415926,2))
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(str(list(range(10))))
# s = str(list(range(10)))
# # <class 'str'>
# print(type(s))

# a = ["alex", "jack", "rain"]
# b = ["black girl","racheal","City","Cathrine"]
# # ('alex', 'black girl')
# # ('jack', 'racheal')
# # ('rain', 'City')
# for i in zip(a, b):
#     print(i)


l = list(range(10))

def compare(x):
    if x > 5:
        return x

list = filter(compare, l)
# 6 7 8 9
for i in list:
    print(i, end=" ")
