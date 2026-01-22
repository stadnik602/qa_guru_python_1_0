
#Boolean
b = bool

t = True
f = False
n = None

# if/elif/else
if True:
    print('Running')
if False:
    print('Never Running')

code = 200

if 200 <= code < 400:
    print('Test passed, good response')
elif 400 <= code < 600:
    print('Test failed, bad response')
else:
    print('Incorrect code')

#empty objects
user_list = []
if user_list == []:
    pass

if user_list:
    pass

items_count = 0
if items_count == 0:
    pass

if items_count:
    pass

if 'abc' == '':
    pass

print(bool(100))
print(bool(-100))

print(bool('abc'))
print(bool(''))

print(bool([]))
print(bool([1, 2, 3]))

print(bool([False]))
print(bool([[]])) 

