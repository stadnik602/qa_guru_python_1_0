from os import name

d = {
    "key": "value",
     "key2": "value2"
}
print(d)

user = {
    "name": "Vasya",
    "age": 22,
}

user2 = {
    "name": "Peter",
    "age": 20,
}

user3 = {
    "name": "Mariia",
    "age": 26,
}

users = {
    25: user,
    42: user2,
}

print(user["name"])
print(user2["age"])

print(("-----------------------"))

print(users[42])
print(users)
print(users.pop(25))
print(users)
users.clear()
print(users)

print(("-----------------------"))

users = {
    10: user,
    12: user2,
    14: user3
}

print(users)
print(("-------items-------"))
from pprint import pprint
dict_items = users.items()
print(dict_items)
print(list(dict_items))
pprint(list(dict_items))
print(("-------values-------"))
dict_values = users.values()
print(dict_values)
print(list(dict_values))
pprint(list(dict_values))
print(("-------keys-------"))
dict_keys = users.keys()
print(dict_keys)
print(list(dict_keys))
print(("-----------------------"))

print(users.get(50, {"name": "default user"}))
print(users.get(55))
users[55] = {"name": "new user"}
print(users[55 ])
# users[50] #error

