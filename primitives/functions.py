from operator import itemgetter
from pprint import pprint


def my_func():
    print("Hello World")

my_func()
my_func()


users = [
    {"name": "Oleg", "age": 66},
    {"name": "Marina", "age": 44},
    {"name": "Martin", "age": 22},
    {"name": "John", "age": 11}
]

#Функция с позиционными аргументами

def sum_numbers(a:int, b:int):
    print(a + b)

sum_numbers(10, 29)
sum_numbers(20, -30)
sum_numbers(-4395834592, 1)

#Функция с именнованными аргументами

sum_numbers(b = 10, a = 99)

#Функция с аргументами по умолчанию

def multiply(n, mult: int = 2):
    print(n * mult)

multiply(10)
multiply(10, 5)

print(1, 2, 3, 4, 5, sep=" | ")
#Возвращаем значение

def sum(a:int, b:int):
    return a + b

n = sum(10, 15)
print(n)

#Возвращаем несколько значений
def return_tuple():
    return 1, 2, 3

t = return_tuple()
print(t)
t1, t2, t3 = return_tuple()
print(t1)
print(t2)
print(t3)

t1, *t2 = return_tuple()
print(t1, t2)
t1, *_ = return_tuple()
print(t1)

#Переменное количество аргументов на примере print

def custom_print(*args):
    for arg in args:
        print(arg)
    print(args)
    print(*args)

custom_print(1, 2, 3, 4, 5)

print('-----------------------')

#Переменное количество именнованных аргументов
def custom_name_print(*args, **kwargs):
    print(args)
    print(*args)
    print(args, kwargs)
    print(*args, *kwargs)
    print(*args, **kwargs)

custom_name_print(1, 2, 3, 4, 5, end="!\n", sep=" | ")

#Область видимости

v = 123

def my_awesome_func():
    v = 456
    print(v)

my_awesome_func()
print(v)

#Функция тоже объект

p = print

p(1, 2, 3, 4, 5)

users_list = [
    {"name": "Oleg", "age": 66},
    {"name": "Marina", "age": 44},
    {"name": "Martin", "age": 22},
    {"name": "John", "age": 11},
    {"name": "Gleb", "age": 18}
]

def get_age(users_list):
    return users_list["age"]

users_list.sort(key=get_age, reverse=True)
pprint(users_list)
print("-----------------")
users_list.sort(key=lambda user: user["age"])
pprint(users_list)
print("-----------------")

users_list.sort(key=itemgetter('name'))
pprint(users_list)
print("-----------------")
