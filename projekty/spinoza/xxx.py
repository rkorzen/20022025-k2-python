liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
liczby_pierwsze = [] 




# for liczba in liczby:
#     is_prime = True
#     if liczba > 1:
#         for dzielnik in range(2, liczba):
#             if liczba % dzielnik == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             liczby_pierwsze.append(liczba)

# print(liczby_pierwsze)

def is_prime(liczba):
    if liczba > 1:
        for dzielnik in range(2, liczba):
            if liczba % dzielnik == 0:
                return False
        return True
    return False


for liczba in liczby:
    if is_prime(liczba):
        liczby_pierwsze.append(liczba)

print(liczby_pierwsze)