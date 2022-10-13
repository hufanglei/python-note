import random

# # 返回1-10之间的一个随机数，不包括10
# n = random.randint(1, 100)
# print(n)
#
# #返回1-10之间的一个随机数，包括10
# random.randint(1,10)
#
# #随机选取到0-100间的偶数 2是步长
# random.randrange(0,100,2)
#
# # 返回一个随机浮点数
# random.random()

# 返回一个给定数据集合中的随机字符 只返回1个
# choice = random.choice('abce3#$@1')
# print(choice)

# 从多个字符中选取特定数量的字符  返回多个
# sample = random.sample('abcdefghij',3)
# print(sample)

# import string
#
# #从多个字符中选取特定数量的字符
# join = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
# print(join)  #8u3tjx

#
# import random
# # 随机生成小数
# random_random = random.random()
# print(random_random)

#洗牌
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)
