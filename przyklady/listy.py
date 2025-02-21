print([x for x in dir(list) if not x.startswith("_")])


dane = [1, 2, 3]

dane2 = [4, 5, 6]
#
# for d in dane2:
#     dane.append(d)

dane.extend(dane2)
print(dane)


x = dane
dane.append("Last")

print(x, dane)


x = dane.copy()  # płytka kopia shallow copy
dane.append("Last")

print(x, dane)


x = [1, 2, 3]
y = ["a", x]

z = y.copy()

x.append(4)

print(y, z)

print(z is y)

from copy import deepcopy

x = [1, 2, 3]
y = ["a", x]

z = deepcopy(y)

x.append(4)
print(y, z)
print(z is y)

last = x.pop()
last = x.pop()
print(last)
print(x)

x.remove(1)
print(x)

del x[0]
print(x)

del x
# print(x)
