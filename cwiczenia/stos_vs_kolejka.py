"""
LIFO - Last in First Out

d
c
b
a


FIFO - First in First Out
abcd


0123
xyzź

zdejmuje x

012
yzż

0123
xyzź

zdejmuję ź

012
xyz


Napisz klasę realizującą stos w oparciu o pythonwą listę
klasa ma mieć dwie metody - append i pop
niech wywolanie metody dodatkowo printuje informacje


stos = Stos()

stos.append("x")
Dodano element "x"

stos.append("y")
Dodano element "y"

el = stos.pop()
Zdjęto element "y"
print(el)
y


"""

class Stack:
    def __init__(self):
        self._stack = []

    def append(self, x):
        print(f"Dodano element: {x}")
        self._stack.append(x)

    def extend(self, xs: list):
        for element in xs:
            self.append(element)


    def pop(self):
        x = self._stack.pop()
        print(f"Usunięto element: {x}")
        return x



data = [1, 2, 3]
stack = Stack()

stack.extend(data)








