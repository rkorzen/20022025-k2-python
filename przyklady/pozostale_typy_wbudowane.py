

napis = "zażółć gęślą jaźń"
print(napis.encode("UTF-8"))# unicode

print("ż".encode("UTF-8-SIG"))
print("ż".encode("CP1250"))


data = b'\xef\xbb\xbf\xc5\xbc'

print(data.decode("UTF-8-SIG"))

b = bytearray()
print(dir(b))
b.append(65)
print(b)

print(bytearray([65, 66, 67]))

b.append(ord("J"))
print(b)

print(ord("A"), chr(65))

print(bytes(b))