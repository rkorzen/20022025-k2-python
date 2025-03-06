
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from datetime import datetime
from mini_projekt import Library, JsonAdapter

class LibraryGUI:
    def __init__(self, master, library):
        self.master = master
        self.library = library
        self.master.title("Biblioteka")

        # Frame dla przycisków
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.add_button = tk.Button(self.frame, text="Dodaj Książkę", command=self.add_book)
        self.add_button.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.frame, text="Szukaj Książki", command=self.search_books)
        self.search_button.pack(side=tk.LEFT)

        self.refresh_button = tk.Button(self.frame, text="Odśwież", command=self.load_books)
        self.refresh_button.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self.master, columns=("ID", "Tytuł", "Autor", "Rok", "Dostępna"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tytuł", text="Tytuł")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Rok", text="Rok")
        self.tree.heading("Dostępna", text="Dostępna")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<Double-1>", self.on_item_selected)

        self.load_books()

    def load_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.library.get_all_books():
            self.tree.insert("", "end", values=(book.id, book.title, book.author, book.year, book.available))

    def add_book(self):
        title = simpledialog.askstring("Dodaj Książkę", "Tytuł:")
        author = simpledialog.askstring("Dodaj Książkę", "Autor:")
        year = simpledialog.askinteger("Dodaj Książkę", "Rok wydania:")
        isbn = simpledialog.askstring("Dodaj Książkę", "ISBN:")
        genre = simpledialog.askstring("Dodaj Książkę", "Gatunek:")
        if title and author and year and isbn:
            self.library.add_book(title, author, year, isbn, genre)
            self.load_books()

    def search_books(self):
        query = simpledialog.askstring("Szukaj", "Wpisz tytuł lub autora:")
        if not query:
            return
        for row in self.tree.get_children():
            self.tree.delete(row)
        for book in self.library.search(query):
            self.tree.insert("", "end", values=(book.id, book.title, book.author, book.year, book.available))

    def on_item_selected(self, event):
        selected_item = self.tree.selection()[0]
        book_id = int(self.tree.item(selected_item, 'values')[0])
        book = self.library.get_book_by_id(book_id)

        action = messagebox.askquestion("Akcja",
                                        f"Co chcesz zrobić z książką '{book.title}'? (TAK - Wypożycz, NIE - Zwrot)")
        if action == "yes":
            if self.library.borrow_book(book_id):
                messagebox.showinfo("Wypożyczenie", "Książka została wypożyczona.")
            else:
                messagebox.showwarning("Wypożyczenie", "Książka jest już wypożyczona.")
        else:
            if self.library.return_book(book_id):
                messagebox.showinfo("Zwrot", "Książka została zwrócona.")
            else:
                messagebox.showwarning("Zwrot", "Książka była już dostępna.")
        self.load_books()


if __name__ == '__main__':
    root = tk.Tk()
    db_adapter = JsonAdapter("dane/books.json")
    library = Library(db_adapter)
    app = LibraryGUI(root, library)
    root.mainloop()
