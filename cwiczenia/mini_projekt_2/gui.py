import tkinter as tk

from main import calculate


def dodaj():
    d = distance.get()
    pl = price_per_l.get()
    lp100 = l_per_100.get()


    d = int(d)
    pl = float(pl)
    lp100 = float(lp100)

    wynik.configure(text=calculate(d, pl, lp100))


root = tk.Tk()

root.geometry("800x600")

distance_a = tk.Label(root,text="distance")
distance_a.pack()

distance = tk.Entry(root)
distance.pack()

price_per_l_b = tk.Label(root,text="cena paliwa za 1 l")
price_per_l_b.pack()

price_per_l = tk.Entry(root)
price_per_l.pack()

l_per_100_label = tk.Label(root,text="spalanie na 100")
l_per_100_label.pack()

l_per_100 = tk.Entry(root)
l_per_100.pack()

button = tk.Button(root,text="OK", command=dodaj)
button.pack()

wynik = tk.Label(root,text="")
wynik.pack()

root.mainloop()

