import json
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    isbn: int
    genre: Optional[str] = None
    available: bool = True
    added_on: datetime = field(default_factory=datetime.now)
    last_borrowed_on: Optional[datetime] = None
    last_return_on: Optional[datetime] = None

    def serialize(self):
        data = vars(self)
        data["added_on"] = self.added_on.isoformat()
        data["last_borrowed_on"] = self.last_borrowed_on.isoformat() if self.last_borrowed_on else None
        data["last_return_on"] = self.last_return_on.isoformat() if self.last_return_on else None
        return data

    @classmethod
    def deserialize(cls, data: dict):
        data["added_on"] = datetime.fromisoformat(data["added_on"])
        data["last_borrowed_on"] = datetime.fromisoformat(data["last_borrowed_on"]) if data.get("last_borrowed_on") else None
        data["last_return_on"] = datetime.fromisoformat(data["last_return_on"]) if data.get("last_return_on") else None
        return cls(**data)

class JsonAdapter:

    def __init__(self, file_name):
        self.file_name = file_name


    def read(self, file_name=None) -> list[Book]:
        if not file_name:
            file_name = self.file_name
        with open(file_name) as json_file:
            data = json.load(json_file)
            data = [Book.deserialize(d) for d in data]
        return data

    def write(self, data: list[Book], file_name=None):
        if not file_name:
            file_name = self.file_name
        with open(file_name, 'w') as file:
            data = [r.serialize() for r in data]
            json.dump(data, file, indent=4)

class BookDoesNotExist(Exception):
    pass

class Library:

    def __init__(self, adapter):
        self.adapter = adapter
        self._books = self.adapter.read()

    def add_book(self, title, author, year, isbn, genre) -> Book:
        id_ = len(self._books) + 1
        book = Book(id=id_, title=title, author=author, year=year, isbn=isbn, genre=genre)
        self._books.append(book)
        return book

    def get_all_books(self) -> list[Book]:
        return self._books

    def search(self, q=None) -> list[Book]:
        if not q:
            return []

        def condition(q, b):
            return q.lower() in b.title.lower() or q in b.author.lower()

        result = [b for b in self._books if condition(q, b)]
        return result

    def get_book_by_id(self, id) -> Book:
        for book in self._books:
            if book.id == id:
                return book
        raise BookDoesNotExist("Book with id {} does not exist".format(id))

    def borrow_book(self, id) -> bool:
        try:
            book = self.get_book_by_id(id)
        except BookDoesNotExist:
            return False
        if book.available:
            book.available = False
            book.last_borrowed_on = datetime.now()
            return True
        return False

    def return_book(self, id) -> bool:
        try:
            book = self.get_book_by_id(id)
        except BookDoesNotExist:
            return False
        if not book.available:
            book.available = True
            book.last_return_on = datetime.now()
            return True
        return False

    def update_book(self, id, **kwargs) -> Book | bool:
        try:
            book = self.get_book_by_id(id)
        except BookDoesNotExist:
            return False
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        return book

    def delete_book(self, id) -> bool:
        try:
            book = self.get_book_by_id(id)
        except BookDoesNotExist:
            return False
        if book:
            self._books.remove(book)
            return True
        return False

    def update_db(self):
        self.adapter.write(self._books)


if __name__ == '__main__':


    # Inicjalizacja adaptera bazy danych i biblioteki
    db_adapter = JsonAdapter("dane/books.json")
    library = Library(db_adapter)


    # Dodawanie książek
    library.add_book("Pan Tadeusz", "Adam Mickiewicz", 1834, "9788373271685", "poezja")
    library.add_book("Lalka", "Bolesław Prus", 1890, "9788374350037", "powieść")
    library.add_book("Quo Vadis", "Henryk Sienkiewicz", 1896, "9788373271906", "powieść historyczna")

    print(library._books)

    # Wyświetlanie wszystkich książek
    print("\nWszystkie książki:")
    for book in library.get_all_books():
        print(book)

    # Wyszukiwanie książek
    query = "prus"
    print(f"\nWyniki wyszukiwania dla '{query}':")
    for book in library.search(query):
        print(book)

    print()
    # Wypożyczanie książki
    book_id = 2
    book = library.get_book_by_id(book_id)
    print(book)

    print(library.borrow_book(book_id))
    print(library.borrow_book(book_id))
    print(book.id, book.available)

    # Aktualizacja danych książki
    book = library.get_book_by_id(1)
    print(book.genre, book.year)

    library.update_book(1, genre="epopeja narodowa", year=1834)

    print(book.genre, book.year)


    # Zwrot książki
    if library.return_book(book_id):
        print(f"\nKsiążka o ID {book_id} została zwrócona.")
    book = library.get_book_by_id(book_id)
    print(book)

    # Usuwanie książki
    if library.delete_book(3):
        print("\nKsiążka została usunięta.")

    # Wyświetlanie wszystkich książek po operacjach
    print("\nAktualna lista książek:")
    for book in library.get_all_books():
        print(book)

    # print(library.get_book_by_id(10))
    # library.delete_book(10)

    library.update_db()
