from pprint import pprint

data = {}
# data = dict()

pprint([x for x in dir(data) if not x.startswith('_')])

help(data.fromkeys)

new_data = dict.fromkeys("abcd", 0)
print(new_data)


d1 = {"a": 2, "b": 3, "e": 4}
d2 = {"a":4, "c": 2}

d1.update(d2)

print(d1)

for k in d1:
    print(k, d1[k])

for k in d1.keys():
    print(k, d1[k])

for k, v in d1.items():
    print(k, v)

print(d1.items())

data = [('a', 4), ('b', 3), ('e', 4), ('c', 2)]
data2 = ["ab", "dd", "ea", "xz"]
print(dict(data))
print(dict(data2))

print(dict(a=1, b=2, c=3, d=4))

data3 = {"e": 1, "f":2}
print(dict(a=1, b=2, c=3, d=4, **data3))

lista = [1, 2, 3]


def foo(a, b, c):
    print(a + b + c)
# foo(lista)  foo([1, 2, 3])
foo(*lista)  # foo(1, 2, 3)

a, b = 1, 2

a, *b, c = 1, 2, 3, 4, 5, 6

print(a, b, c)

help(dict.setdefault)

data3.setdefault("x", 9)
print(data3)

from collections import defaultdict

d = defaultdict(float)
d["x"] += 1
print(d["x"])


