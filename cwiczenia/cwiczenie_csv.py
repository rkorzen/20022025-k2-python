"""

Twoje zadanie polega na napisaniu skryptu w Pythonie, który:

    Wczyta plik CSV i wyświetli jego zawartość w czytelnej formie.
    Obliczy całkowitą wartość sprzedaży dla każdego produktu (cena × ilość).

    Zapisze wyniki do nowego pliku sales_summary.csv w formacie:

    nazwa;suma


"""
from typing import TypedDict
from collections import defaultdict
from dataclasses import dataclass
import csv



@dataclass
class Record:
    id: int
    product: str
    price: int
    quantity: int
    date: str

    # def __init__(self, id: int, product: str, price: int, quantity: int, date: str):
    #     self.id = int(id)
    #     self.product = product
    #     self.price = int(price)
    #     self.quantity = int(quantity)
    #     self.date = date

    def __post_init__(self):
        self.id = int(self.id)
        self.price = int(self.price)
        self.quantity = int(self.quantity)

    def total_price(self):
        return self.price * self.quantity

# data_dict = dict(id=1, product="Laptop", price=10, quantity=2, date="2023-12-12")
# data_dict2 = {'id': 1, 'product': 'Laptop', 'price': 10, 'quantity': 2, 'date': '2023-12-12'}
#
# print(data_dict, "\n", data_dict2)
#
d = Record(id=1, product="Laptop", price=10, quantity=2, date="2023-12-12")
# d2 = Record(**data_dict)
print(d)
# print(d2)

Summary = dict[str, int]

def read_data(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [Record(**d) for d in csv_reader]
    return data

def process_data(data: list[Record]) -> Summary:
    summaries: Summary = defaultdict(int)

    for record in data:
        summaries[record.product] += record.total_price()

    return summaries

def export_summary(data: Summary, file_name):
    with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product", "total_price"])
        writer.writerows(data.items())
        print(f"Dane wyeksportowane do pliku: {file_name}")

data = read_data("dane/sales.csv")
summaries = process_data(data)
export_summary(summaries, "dane/sales_summary.csv")
