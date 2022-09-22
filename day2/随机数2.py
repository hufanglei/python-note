import random
import string

s = string.ascii_letters
print(s)
s = string.digits
print(s)
s = string.ascii_letters + string.digits
print(s)
s = random.sample(s, 5)
print(s)
s = "".join(s)
print(s)