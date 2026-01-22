import random

#While - cycle with precondition
#until user will enter correct number, ...

# while True:
#     print(random.randint("I'm teapot"))

required_number = 7
user_number = None

while required_number != user_number:
    user_number = random.randint(0,10)
    print(f'User entered number {user_number}')

iteration_count = 10
i = 0

while i < iteration_count:
    print(f"Current iteration: {i}")
    i+=1

#For. Dict and list iterating

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]
from pprint import pprint

for user in users:
    pprint(f"User {user['name']} is {user['age']} years old")


d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for item in d:
    pprint(item)

for item in d.values():
    pprint(item)

for item in d.items():
    pprint(item)

for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

#for i in range - cycle with iterator

iteration_count = 10

for i in range (iteration_count):
    print(f'Current itteration: {i}')
print('-----------------------------')
for i in range (0, 10, 2):
    print(f'Current itteration: {i}')

#Break/Continue/Else - cycle interruption

for i in range (iteration_count):
    if i % 2 == 0:
        continue
        print('I never run')

    if i > 7:
        break
    print(f"The number {i} is 'odd'")

for i in range(5):
    for j in range(5):
        print(i, j)
        if j == 3:
            continue

        if j == 4:
            break

#enumerate - return pare(index, value)

cities = ['Toronto', 'Vaughn', 'Markham']

for i, city in enumerate(cities):
    print(f"{city} is on {i + 1} place by air pollution")