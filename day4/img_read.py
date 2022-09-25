
# 二进制读
# f = open("img.png","rb")
#
# for line in f:
#     print(line)

# wb二进制写

f = open("wb_file","wb")
s = "路飞"
# f.write(s.encode("gbk"))
# f.write(s.encode("utf-8"))
f.write("路飞")
