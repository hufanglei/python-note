# 格式化打印
name=input("name:")
age=input("age:")
job=input("job:")
hobbie=input("hobbie")

# print(name)
# print(age)
# print(hometown)
# print(hobbie)


# 关键点: 加上f 可以打印好看的格式化信息
msg = f'''
---------------info {name}-------------------------------
Name   : {name}
Age    : {age}
job    : {job}
hobbie : {hobbie}
---------------end---------------------------------------
'''

print(msg)
