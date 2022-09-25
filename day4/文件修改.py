
f = open("stock_data", "r+",encoding="utf-8")

# 1.加载到内存
data = f.read()
new_data= data.replace("吉⻉尔","路飞学城")
print(new_data)
# 截断文件

# 2.清空文件
f.seek(0)
f.truncate()

# 3.把新内容写会硬盘
f.write(new_data)