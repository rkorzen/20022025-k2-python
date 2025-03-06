# wszystkie napisy w python 3 sa unicodem


text = "zażółć gęślą jaźń"

zakodowane = text.encode()

# zakodowane = b'za\xc5\xbc\xc3\xb3\xc5\x82\xc4\x87 g\xc4\x99\xc5\x9bl\xc4\x85 ja\xc5\xba\xc5\x84'

print(zakodowane.decode())

text = """Rafał;Michał;Robert;Adam
40;41;42;43
a;"b;c";"a"";""c";"d"";"
"""

with open("dane/osoby_cp1250.csv", "w", encoding="CP1250") as f:
    f.write(text)