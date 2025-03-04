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
"Jestem Rafał, moja stawka to 100/h, nierozliczone godziny s:0 n:0 t:0
>>> e.pay_salary()
0
>>> e.register_time(5)
>>> e.pay_salary()
500
>>> e.pay_salary()
0
>>> e.register_time(10)
>>> e.introduce()
"Jestem Rafał, moja stawka to 100/h, nierozliczone godziny s:8 n:2 t:10
>>> e.pay_salary()
1200

Pracownik Premium ma mozliwosc otrzymania bonusa

>>> pe = PremiumEmployee("Adam", rate_per_hour=100)
>>> pe.register_time(5)
>>> pe.add_bonus(1000)
>>> pe.pay_salary()
1500

"""