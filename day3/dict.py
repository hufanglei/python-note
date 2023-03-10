

dic = {
    "Alex": [23,"CEO",66000],
    "黑姑娘": [24,"行政",4000],
    "佩奇": [26,"讲师",4000],
}

print("佩奇" in dic)
print(dic.get("佩奇"))

dic2 = {
    "Alex": 16,
    "黑姑娘": 27,
    "佩奇": 26,
}
print(dic2)
print('-----------------')
for k,v in dic.items():
  print(k,v)
print('-----------------')
for k in dic:
  print(k,dic[k])