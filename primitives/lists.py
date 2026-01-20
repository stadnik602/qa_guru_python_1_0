l = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

print(l[0])
print(l[-1])
print(l[-1][0])
print("---------------")
print(l[1:8:2])
print(l[-1:-10:-3])
print(l[::-1])


l.append("new element")
print(l)

l.extend(["elem", "another elem"])
print(l)

print(len(l))

l.reverse()
print(l)

l[0] = 200
print(l)
print("-----------------------------")

s = {1, 2, 3, 4, 5, 5, 5, 5, 5}
s2 = {1, 2, 5, 5}
print(s)
print(s2)

print(s.intersection(s2))

print(s - s2)

print(set([1, 2, 3, 4, 5, 5, 5]))
print(list(set([1, 2, 3, 4, 5, 5, 5])))
