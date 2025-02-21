a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2, 3, 6, 7}

empty_set = set()


print(a | b)
print(a.union(b))
print(a & b)
print(b - a)
print(a ^ b)

print(a.issubset(c))
print(b.issubset(c))
print(c.issuperset(a))
