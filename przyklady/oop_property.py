from datetime import datetime


class Person:

    def __init__(self, name, b_year):
        self.name: str = name
        self.b_year: int = b_year

    @property  # atrybut dynamiczny
    def age(self):
        return datetime.now().year - self.b_year

    @age.setter
    def age(self, value):
        self.b_year = datetime.now().year - value

    @age.deleter
    def age(self):
        # tutaj mozemy cos posprzatac jak usuwamy nasz obiekt
        print("Sprzątam")


p = Person("Rafał", 1980)
print(p.age)  # 45

p.b_year = 1976
print(p.age)


p.age = 55
print(p.age, p.b_year)

del p.age
# print(p)

print(getattr(p, "b_year"))
setattr(p, "xxx", 65)
print(getattr(p, "xxx", "yyy"))

def foo():
    print("jestem foo")

foo.x = 10
setattr(foo, "y", 1110)
print(foo.y)


