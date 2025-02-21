"""
Pobierz od użytkownika n liczb.


Przykład:

Podawaj liczbe i nacisnij enter lub wcisnij enter bez podawania niczego by zakonczyc

Podaj liczbe: 1
Podaj liczbe: 4
Podaj liczbe: 7
Podaj liczbe:

Unikalnych liczb: 3
Parzystych liczb: 1
Nieparzystch liczb z zakresu (1-101): 1
Suma liczb: 12
Srednia: 4

przydatne rzeczy:
* range
* input
* int
* help
"""


def get_data():
    print("Podawaj liczbe i nacisnij enter lub wcisnij enter bez podawania niczego by zakonczyc")

    data = []

    while True:
        answer = input("Podaj liczbę: ")
        if answer == "":
            break
        data.append(int(answer))
    return data

def get_len_of_unique_elements(data): return len(set(data))

def get_len_of_even_numbers(data):
    filtered = [d for d in data if d % 2 == 0]
    return len(filtered)

def get_len_of_odd_numbers_from_range(data, start=1, stop=101):
    odd_in_range = {x for x in range(start, stop, 2)}
    return len(set(data) & odd_in_range)

def get_mean(data):
    return sum(data) / len(data)

def main():
    data = get_data()

    print(f"Unikalnych liczb: {get_len_of_unique_elements(data)}")
    print(f"Parzystych liczb: {get_len_of_even_numbers(data)}")
    print(f"Nieparzystch liczb z zakresu (1-101): {get_len_of_odd_numbers_from_range(data)}")
    print(f"Suma liczb: {sum(data)}")
    print(f"Srednia: {get_mean(data)}")


# print(dir())
# print(__name__)

if __name__ == "__main__":
    print("Cos tam")
    main()

# Przerwa do 10:5