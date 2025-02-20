"""

napisz fynkcję

is_palindrome(tekst)

która sprawdzwi czy zadany tekst to palindrom


is_palindrome("Kajak") -> True
is_palindrome("kajak") -> True


is_palindrome("Kot") -> False

is_palindrome("Kobyła ma mały bok") -> True
is_palindrome("Kobyła !ma, mały- bok") -> True

"""

print(dir(str))



def is_palindrome(tekst):
    tekst = tekst.lower()
    choosen = [s for s in tekst if s.isalnum()]
    return choosen == choosen[::-1]


assert is_palindrome("Kot") is False
assert is_palindrome("Kajak") is True
assert is_palindrome("Kobyła ma mały bok") is True