import csv

osoby = ["Rafał", "Michał", "Robert", "Adam"]
wiek = [40, 41, 42, 43]
xxx = ['a', "b;c", 'a";"c', "d"]
dane = [osoby, wiek, xxx]



r = "Rafał"
r_e = r.encode("CP1250")

print(r_e)
osoby[-1] = r_e

print(osoby)


# with open("dane/osoby.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";")
#     # writer.writerow(osoby)
#     # writer.writerow(wiek)
#     writer.writerows(dane)


#
with open("dane/osoby.csv") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)