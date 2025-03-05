from datetime import datetime

class Person:

    def __init__(self, name, b_year):
        self.name: str = name
        self.b_year: int = b_year

    @property  # atrybut dynamiczny - getter - co ma sie stac jak pobieram te wartosc
    def age(self):
        return datetime.now().year - self.b_year

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.b_year == other.b_year

p1 = Person("A", 1980)
p2 = Person("A", 1980)


print(p1 == p2)
# print(p2 > p1)

# if p2.age > p1.age:
#     ...


class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

    def __add__(self, other):
        return self.__class__((self.side ** 2 + other.side ** 2) ** 0.5)

    def __gt__(self, other):
        return self.area > other.area

    def __mul__(self, other):
        return  Square(self.side * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"Square of {self.side} side"

    def __repr__(self):
        return f"<Square: {self.side}>"


s1 = Square(2)
s2 = Square(3)

print(s2 > s1)
print(s2.side > s1.side)



def add_squres(s1, s2):
    return Square((s1.side ** 2 + s2.side ** 2)**0.5)

s3 = add_squres(s1, s2)

s4 = s1 + s2


"""
+   __add__
-   __sub__
*   __mul__
/   __truediv__
//  __floordiv__
%   __mod__
"""

print(s1 * 5)
print(5 * s1)

print([s1, s2, s3, s4])

print(str(s1))
print(repr(s1))