a = "Alex 金角大王"
# 打印效果 ---------------Alex 金角大王----------------
print(a.center(40,"-"))
# 统计打印次数 后面2个参数是查找范围
print(a.count("e",0,4))
# 判断是否以王八结尾
print(a.endswith("王八"))
# 字符查找，返回字符的索引 返回-1代表没找到
print(a.find("e"))
# 是不是整数
print(a.isdigit())
# 判断是否是整数
print("22".isdigit())

l = ["Alex", "blackgirl", "peiqi"]
# 拼接字符串 Alex-blackgirl-peiqi
print("-".join(l))

# 字符串替换 1代表只替换一个
b = a.replace("l", "m",1)
# Amex 金角大王
print(b)
# Alex 金角大王
print(a)
# ['Alex', '金角大王']
print(a.split())
# ['A', 'ex 金角大王']
print(a.split("l"))
# AMex 金角大王
print(a.replace("l","M",1))
# ['A', 'ex 金角大王']
print(a.split("角"))



