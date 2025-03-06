import csv
import json
from dataclasses import dataclass
from datetime import date

@dataclass
class Record:
    id: int
    product: str
    price: int
    quantity: int
    date: date

    def __post_init__(self):
        self.id = int(self.id)
        self.price = int(self.price)
        self.quantity = int(self.quantity)
        self.date = date.fromisoformat(self.date)

    def total_price(self):
        return self.price * self.quantity

    def serialize(self):
        """To dict serialzie - zamienia obiekty takie date na napisy"""
        return {
            "id": self.id,
            "product": self.product,
            "price": self.price,
            "quantity": self.quantity,
            "date": self.date.isoformat()
        }


class CSVAdapter:

    def read(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [Record(**d) for d in csv_reader]
        return data

    def write(self, data: list[Record], file_name):
        if not data:
            return

        with open(file_name, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].__dict__.keys())
            csv_writer.writeheader()
            csv_writer.writerows([vars(d) for d in data])


class TextAdapter:

    def read(self, file_name, product_line_counter=5):
        with open(file_name) as csv_file:
            keys = []
            for i in range(product_line_counter):
                keys.append(next(csv_file).strip())

            data: list[Record] = []
            temp = []
            for i, line in enumerate(csv_file, start=1):
                temp.append(line.strip())
                if i % product_line_counter == 0:
                    data.append(Record(**dict(zip(keys, temp))))
                    temp = []
        return data

    def write(self, data: list[Record], file_name):
        header = data[0].__dict__.keys()
        with open(file_name, 'w') as file:
            for h in header:
                file.write(f"{h}\n")

            for d in data:
                for el in d.__dict__.values():
                    file.write(f"{el}\n")


class JsonAdapter:

    def read(self, file_name) -> list[Record]:
        with open(file_name) as json_file:
            data = json.load(json_file)
            data = [Record(**d) for d in data]
        return data

    def write(self, data: list[Record], file_name):
        with open(file_name, 'w') as file:
            data = [r.serialize() for r in data]
            json.dump(data, file, indent=4)


adapter = TextAdapter()
adapter2 = CSVAdapter()
adapter3 = JsonAdapter()
dane = adapter.read("dane/sales.txt")
print(dane)

r = Record(31, "Tablet", 1400, 1, "2025-03-06")
dane.append(r)

adapter.write(dane, "dane/sales.txt")
adapter2.write(dane, "dane/sales.csv")
adapter3.write(dane, "dane/sales.json")

print(adapter3.read("dane/sales.json"))