from collections import namedtuple
from dataclasses import dataclass
Vector = namedtuple("Vector", ["x", "y"])


v = Vector(1, 2)

print(v)

print(v.x)

print(type(v))

print(dir(v))


class Vector:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y


v = Vector(1, 2)
# v.z = 3
# print(vars(v))

@dataclass(slots=True, frozen=True)
class Vector:
   x: int
   y: int

v = Vector(1, 2)
v.x = 10