from decimal import Decimal

a = 123
a = a + 100
a = a - 200
a = a / 2
a = a * 3
a = a ** 3
a = (100 + 200) / 300*400

a = 11123453464567546854745634523412434654684673452364567452134523

a = 0b11001010010
a = 0o1234567
a = 0x1234567890abcdef

a = 0.5

print(a)

a = 0.1 + 0.2
# assert a == 0.3

import math

print(math.pi)

import random


random.seed("another word") # return the same values each time for random.randint
print("RANDOM")
print("----------------")
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print("----------------")

print(round(1.333333, 2))
