name = "Alex Li"

def change_name():
    # 就是想在函数⾥修改全局变量怎么办？
    global name
    name = "Alex ⼜名⾦⻆⼤王,爱⽣活、爱⾃由、爱姑娘"
    print("after change", name)


change_name()
print("在外面看看name改了么?", name)


# 传递列表、字典产⽣的现象

def change_data(info, girls):
    info["hobbie"] = "学习"
    girls.append("XiaoYun")


d = {"name": "Alex", "age": 26, "hobbie": "⼤保健"}
l = ["Rebeeca", "Katrina", "Rachel"]
change_data(d, l)
print(d, l)
