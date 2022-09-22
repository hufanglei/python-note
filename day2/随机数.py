import random

# number = random.choice("abcdefghijklmnopqrstuvwxyz")
# print(number)

a = ["alex", "jim", "rain"]
print(random.choice(a))

print("--------------------------")

b = list(range(20))
print(b)
print(random.sample(b,3))
print(random.sample(b,5))

print("----------------------------")

n = "-".join(["a","b","c"])
print(n)

n = "".join(["a","b","c"])
print(n)

n=random.randint(1,100)
print(n)
