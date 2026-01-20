from copy import deepcopy

l1 = [1, 2, 3]
l2 = l1
l2.append(4)
print(l1)
print(l2)
print("_______________")

l2 = l1.copy()
l2.append(5)
print(l1)
print(l2)
print("_______________")

l2 = deepcopy(l1)
print("deepcopy", l2)
l2[-1] = 8
l2.append(9)
print(l2)
print("_______________")

l3 =[1, 2, 3, [4, 5, 6]]
l3[-1].append(7)
print(l3)
l3.append(22)
print(l3)
print(l3[-2][-2])
l4 = l3[-2]
print(l4)

print("____кортежи_____")

t = (1, 2, 3, 4, 5)
print(t)
print(t.index(5, 1, 5))

w = frozenset({4,5,6,7,8,8,8})
print(w)


