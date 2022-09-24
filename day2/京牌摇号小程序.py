import random
import string

count = 0
while count < 3:
    car_nums = []  # 存储供用户选择的号
    count = count + 1
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)  # 生成车牌的第一个字母
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num)  # 把生成的号码添加到列表
        print(i + 1, c_num)
    print("---------------------------")
    choice = input("输入你选择的车牌号")
    # strip去空格
    if choice.strip() in car_nums:  # 代表选择是合法的
        print(f"恭喜你选择了新车牌号:{choice}")
        break
        exit("Good Luck")
    else:
        print("不合法的输入")
    if count == 3:
        break
