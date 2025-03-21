"""

Napisz funkcje id_generator(prefix), która zwróci funkcję, generująca kolejne unikalne identyfukatory


user_id = id_generator("user_")
print(user_id()) # user_1
print(user_id()) # user_2
print(user_id()) # user_3

order_id = id_generator("order_")
print(order_id()) # order_1
print(order_id()) # order_2
print(order_id()) # order_3

przydatne rzeczy:
nonlocal
global
"""


def id_generator(prefix):
    counter = 0

    def inner():
        nonlocal counter
        counter += 1

        return f"{prefix}{counter}"

    return inner


user_id = id_generator("user_")
print(user_id())  # user_1
print(user_id())  # user_2
print(user_id())  # user_3

order_id = id_generator("order_")
print(order_id())  # order_1
print(order_id())  # order_2
print(order_id())  # order_3
