"""

Utworz iterator Vowels który z zadanego tekstu bedzie zwracac kolejne samogloski

for char in Vowels("a b c d e"):
    print(char)
a
e


"""

class Vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = "aeiouAEIOU"
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        while self.index < len(self.string):
            current_char = self.string[self.index]
            self.index += 1
            if current_char in self.vowels:
                return current_char

        raise StopIteration


for char in Vowels("a b c d e"):
    print(char)