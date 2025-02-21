def outer_function(msg):
    def inner_function():
        print(f"Zapamiętana wiadomość to: {msg}")

    return inner_function


closure = outer_function("Hello ALX")
closure2 = outer_function("Hello Rafał")
closure()
closure2()


def incrementator_fabric(step=1):

     def incrementator(value):
         return value + step

     return incrementator


incr_by_10 = incrementator_fabric(10)
print(incr_by_10(121))