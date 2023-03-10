names = ["alex","jack","tom"]
print(names)

# names.insert(2,[1,2,3])
# print(names)
#
# names.insert(2,"mike")
# # print(names)
#
# print(names[2])
#
# print(names[3][1])
#
# names1=names.pop()
# # print(names.pop())
# print(names1)
# print(names)

# names.clear()
# print(names)

# print(names.count("jack"))
print(names.index("tom"))

# del names[2]
# print(names)
names.insert(2,[1,2,3])
print(names)

print(names.pop(0))
print(names)

names[1:4]
print(names[2:])

enumerate

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[0:7:3])
print(arr[::3])

a = [83,4,2,4,6,19,33,21]
a.sort()
print(a)
a.reverse()
print(a)

for i in enumerate(a):
    print(i[0],i[1])





