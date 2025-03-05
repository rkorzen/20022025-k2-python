"""
Zaimplementuj klasę Vector, reprezentujaca wektor na płaszczyźnie

v1 = Vector(1, 1)
v2 = Vector(-2, 2)

v1 + v2  # add
v1 > v2  # gt
v1 == v2 # eq
v1 <= v2 # le
v1 >= v2
v1 > v2

print(v1)
'Vector(x=1, y=1)`


"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

if __name__ == "__main__":

    v1 = Vector(1, 1)
    v2 = Vector(-2, 2)
    print(v1)
    assert v1.length() == (1 ** 2 + 1 ** 2 ) ** 0.5
    assert v2.length() == (2 ** 2 + 2 ** 2 ) ** 0.5

    assert v1 + v2 == Vector(-1, 3)
    assert (v1 > v2) is False
    assert (v1 < v2) is True