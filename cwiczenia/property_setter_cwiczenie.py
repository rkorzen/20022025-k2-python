"""

Tworzymy klasę Square
I chcemy zadbać o to by niemożliwe było ustawienie bok o ujemnej długości

Square(-10) # blad

s = Square(10)
print(s.side)
#s.side = -10 # blad

s.area == 100
s.rectangle == 40

s.area = 25
s.side == 5

s.rectangle = 40
s.side == 10

"""
from plotly.graph_objs.layout.map.layer import Circle


class Square:
    def __init__(self, side: float):
        self.side: float = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Square side must be greater than or equal to zero")
        self._side: float = value

    @property  # s.area
    def area(self):
        return self.side * self.side

    @area.setter # s.area = 10
    def area(self, value):
        self.side = value ** 0.5

    @property
    def rectangle(self):
        return self.side * 4

    @rectangle.setter
    def rectangle(self, value):
        self.side = value / 4

s = Square(10)
s.side = 16
print(s.side)

## zrob analogiczny przyklad dla Circle

from math import pi

c = Circle(10)
c.radius
c.diameter
c.area
c.rectangle


