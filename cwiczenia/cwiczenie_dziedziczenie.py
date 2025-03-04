"""

ZADANIE: SYSTEM ZARZĄDZANIA PRACOWNIKAMI

W tym zadaniu stworzysz prosty system zarządzania pracownikami firmy,
wykorzystując dziedziczenie klas w Pythonie.

Twoim zadaniem jest zaimplementowanie hierarchii klas reprezentujących różne
typy pracowników w firmie, z odpowiednimi atrybutami i metodami.

rejestracja czasu - jeśłi <=8 h to to są standardowe godzint
                    jeśli więcej niż 8:
                        8 standardowych godzin
                        reszta to nagodziny - nagodziny sa liczone podwójnie

standardowy pracownik: Employee
Pracownik premiun:     EmployeePremium

Pracownik przedstawia sie

>>> e = Employee("Rafał", rate_per_hour=100)
>>> e.introduce()
'Jestem Rafał, moja stawka to 100/h, nierozliczone godziny s:0 n:0 t:0'
>>> e.pay_salary()
0
>>> e.register_time(5)
>>> e.pay_salary()
500
>>> e.pay_salary()
0
>>> e.register_time(10)
>>> e.introduce()
'Jestem Rafał, moja stawka to 100/h, nierozliczone godziny s:8 n:2 t:10'
>>> e.pay_salary()
1200
>>> e.introduce()
'Jestem Rafał, moja stawka to 100/h, nierozliczone godziny s:0 n:0 t:0'

Pracownik Premium ma mozliwosc otrzymania bonusa
1
# >>> pe = PremiumEmployee("Adam", rate_per_hour=200)
# >>> pe.register_time(5)
# >>> pe.add_bonus(1000)
# >>> pe.add_bonus(500)
# >>> pe.add_percentage_bonus(10)
# >>> pe.pay_salary()
# 2750
# >>> pe.pay_salary()
# 0

2
>>> pe = PremiumEmployee("Adam", rate_per_hour=200)
>>> pe.register_time(5)
>>> ba1 = AmountBonus(1000)
>>> ba2 = AmountBonus(500)
>>> pe.add_bonus(ba1)
>>> pe.add_bonus(ba2)
>>> pb = PercentageBonus(10)
>>> pe.add_bonus(pb)
>>> pe.pay_salary()
2750
>>> pe.pay_salary()
0
>>> pe.add_bonus(XTimesBonus(10))
>>> pe.pay_salary()
0
>>> pe.register_time(5)
>>> pe.add_bonus(XTimesBonus(10))
>>> pe.pay_salary()
11000


"""

class Employee:

    def __init__(self, name: str, rate_per_hour: int):
        self.name = name
        self.rate_per_hour = rate_per_hour

        self.hours: int = 0
        self.over_hours: int = 0


    def introduce(self) -> str:
        return (f"Jestem {self.name}, moja stawka to {self.rate_per_hour}/h, "
                f"nierozliczone godziny s:{self.hours} n:{self.over_hours} t:{self.over_hours + self.hours}")

    def pay_salary(self) -> int:
        to_pay = self.hours * self.rate_per_hour + self.over_hours * self.rate_per_hour * 2
        self.hours = 0
        self.over_hours = 0
        return to_pay

    def register_time(self, hours: int) -> None:
        if hours <= 8:
            self.hours = hours
        else:
            self.hours = 8
            self.over_hours = hours - 8

class PremiumEmployee(Employee):

    def __init__(self, name: str, rate_per_hour: int):
        super().__init__(name, rate_per_hour)
        self.bonuses: list[Bonus] = []


    def add_bonus(self, bonus: "Bonus") -> None:
        self.bonuses.append(bonus)

    def pay_salary(self) -> int:
        to_pay = super().pay_salary()
        for bonus in self.bonuses:
            to_pay = bonus.calculate(to_pay)

        self.bonuses = []
        return to_pay

# SOLID

class Bonus:

    def __init__(self, value: int):
        self.value = value

    def calculate(self, to_pay: int) -> int:
        raise NotImplementedError

class AmountBonus(Bonus):

    def calculate(self, to_pay: int) -> int:
        return to_pay + self.value


class PercentageBonus(Bonus):

    def calculate(self, to_pay: int) -> int:
        return to_pay + int(to_pay * self.value / 100)


class XTimesBonus(Bonus):

    def calculate(self, to_pay: int) -> int:
        return to_pay + to_pay * self.value