"""

Iplementujemy funkcjonalnosc biblioteki (Library)

Chcemy mieć dostępne operacje typu CRUD (Create, Read, Update, Delete) dla zasobów biblioteki

Zasobem biblioteki jest ksiazka (Book)

Book
   id: int
   title: str
   author: str
   year: int
   isbn: int
   genre: Optional[str]
   available: bool (default= True)
   added_on: datetime = datetime.now()
   last_borrowed_on: Optional[datetime] = None
   last_return_on: Optional[datetime] = None

Logika biznesowa jest zawarta w klasie Library

Adapter

    read -> list[Book]

    write(file_name, data: list[Book]) -> None


Library

    __init__(self, adapter)
        self.adapter = adapter
        self.books = self.adapter.read()

    def add_book  # Create

    def get_all_books -> list[Book]

    def get_book_by_id -> Book  # READ

    def search(q=None) -> list[Book]
        "na razie niech to bedzie szukanie po zawartosci w tytule

    def update_book  # UPDATE

    def delete_book  # DELETE

    def borrow_book

    def return_book


    def _update_db

"""


if __name__ == '__main__':

    # Inicjalizacja adaptera bazy danych i biblioteki
    db_adapter = JsonAdapter("data/books_database.json")
    library = Library(db_adapter)

    # Dodawanie książek
    library.add_book("Pan Tadeusz", "Adam Mickiewicz", 1834, "9788373271685", "poezja")
    library.add_book("Lalka", "Bolesław Prus", 1890, "9788374350037", "powieść")
    library.add_book("Quo Vadis", "Henryk Sienkiewicz", 1896, "9788373271906", "powieść historyczna")

    # Wyświetlanie wszystkich książek
    print("\nWszystkie książki:")
    for book in library.get_all_books():
        print(book)

    # Wyszukiwanie książek
    query = "prus"
    print(f"\nWyniki wyszukiwania dla '{query}':")
    for book in library.search_books(query):
        print(book)

    # Wypożyczanie książki
    book_id = 2
    book = library.get_book_by_id(book_id)
    assert book.available is True
    library.borrow_book(book_id)
    assert book.available is False


    # Aktualizacja danych książki
    library.update_book(1, genre="epopeja narodowa", year=1834)

    # Wyświetlanie zaktualizowanej książki
    book = library.get_book_by_id(1)
    print(f"\nZaktualizowane dane książki: {book.title} - gatunek: {book.genre}")

    # Zwrot książki
    if library.return_book(book_id):
        print(f"\nKsiążka o ID {book_id} została zwrócona.")

    # Usuwanie książki
    if library.delete_book(3):
        print("\nKsiążka została usunięta.")


    # Wyświetlanie wszystkich książek po operacjach
    print("\nAktualna lista książek:")
    for book in library.get_all_books():
        print(book)


13:23 wracamy