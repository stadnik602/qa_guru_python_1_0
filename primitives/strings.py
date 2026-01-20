
s = "Hello, world!"
s = 'Hello, world!'

s = 'Hello, \' world!'
s = '''Hello, '' world!'''
s = """Hello, "" world!"""

s = """He
llo, 
world
!"""
print(s)

s = "Hello, \n world!"
print(s)

s = ("Hello, "
     "world!")
print(s)
s = "Hello,"\
     " world!"
print(s)

print("--------------------")

email = "user@domain.com"
print(email[1])
print(email[-2])

print(email[0:5])
print(email[:5])

print(email[0:10:2])

print(email[::-1])

print("--------------------")
a = "Hello"
b = "World"

print(a + ", " + b + "!")
print(f"{a}, {b.upper()}!")

print(f"{a=}, {b=}!")

print("%s, %s!" % (a, b))
print("--------------------")

s = "1234"
n = 1234
assert s.isdigit()
assert s == str(n)
assert int(s) == n