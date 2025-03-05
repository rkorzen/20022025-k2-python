# with open("praca_z_plikami.md") as f:
#     for nr, line in enumerate(f, start=1):
#         # print(f"{nr:4} {line[:-1]}")
#         if line.startswith("## "):
#             print(f"{nr:4} {line[:-1]}")


with open("dane/plik.txt", "w") as f:
    f.write("nowa linia\n")
