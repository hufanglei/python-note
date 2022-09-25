
f = open("嫩模联系方式.txt","r+",encoding="utf-8")
print(f.readline())
print(f.tell())
f.seek(f.tell())
f.write("又来了一个新模特....")