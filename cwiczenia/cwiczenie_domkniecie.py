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

x = 1

def foo():
    y = 10

    def inner():
        nonlocal y
        y = 12

    inner()
    print("y", y)
    global x
    x += 1

foo()

print(x)