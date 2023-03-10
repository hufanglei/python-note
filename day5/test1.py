# def stu_register(name,age,*args,**kwargs):
#  print(name,age,args,kwargs)
#
# stu_register("Alex",22)
# 输出
#Alex 22 () {}#后⾯这个{}就是kwargs,只是因为没传值,所以为空

# stu_register("Jack",32,"CN","Python",sex="Male",province="ShanDong")
# 输出
# Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'}

# d = {"name": "Alex", "age": 26, "hobbie": "⼤保健"}
# l = ["Rebeeca", "Katrina", "Rachel"]
#
# def change_data(info, girls):
#     info["hobbie"] = "学习"
#     girls.append("XiaoYun")
#
# change_data(d, l)
# print(d, l)

import sys
print(sys.path)


