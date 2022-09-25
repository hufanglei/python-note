# f = open("name_list2",encoding="utf-8")
# f.seek(8)
# print(f.readline())

f = open("seek_write","w")
f.write("hello1\n")
print("返回光标当前位置: ",f.tell())

f.write("hello2\n")
print("返回光标当前位置: ",f.tell())

f.write("hello3\n")
print("返回光标当前位置: ",f.tell())
f.seek(10)
# f.write("-----")
