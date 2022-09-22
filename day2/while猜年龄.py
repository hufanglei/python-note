
count = 0
black_girl_age = 26
while count < 3:
    guess = int(input("输入您的猜测: "))
    count = count + 1
    if guess > black_girl_age:
        print("你讨厌，人家哪有那么老。。。")
    elif guess < black_girl_age:
        print("真开心，但实际我比这个岁数要大呢。。。")
    else:
        print("恭喜你，猜对了，可以今天把我领回家了。。。")
        break


print("后面的代码....")