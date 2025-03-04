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


class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Square side must be greater than or equal to zero")
        self._side = value


s = Square(10)
s.side = 16
print(s.side)

