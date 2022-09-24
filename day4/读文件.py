f = open("嫩模联系方式.txt")

for line in f:
    line = line.split()
    height = int(line[3])
    weight = int(line[4])
    if height >= 170 and weight <= 50:
        print(line)
