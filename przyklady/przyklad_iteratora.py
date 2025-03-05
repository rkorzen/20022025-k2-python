

class Odliczanie:
    def __init__(self, limit):
        self.limit = limit
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.limit:
            raise StopIteration

        value = self.index
        self.index += 1
        return value



iterator = Odliczanie(3)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for x in iterator:
    print(x)



