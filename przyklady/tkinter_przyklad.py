import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

def dodaj():
    a = entry_a.get()
    b = entry_b.get()

    a, b = int(a), int(b)

    wynik.configure(text=str(a+b))



root = tk.Tk()

root.geometry("800x600")

label_a = tk.Label(root,text="A")
label_a.pack()

entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root,text="B")
label_b.pack()

entry_b = tk.Entry(root)
entry_b.pack()

button = tk.Button(root,text="OK", command=dodaj)
button.pack()

wynik = tk.Label(root,text="")
wynik.pack()

root.mainloop()

