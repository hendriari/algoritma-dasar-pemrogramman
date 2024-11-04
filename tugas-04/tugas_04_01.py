from datetime import datetime
import math
from general_failure import GeneralFailure

class Receipt:
    def __init__(self, name, date, count, price):
        self.name = name
        self.date = date
        self.count = count
        self.price = price

    def print_receipt(self):
        return "\nNota Pembelian" + f"\nNama Pembeli : {self.name}" + f"\nTanggal Pembelian : {self.date}" + f"\nJumlah Kaleng Cat : {self.count}" + f"\nTotal Harga : {self.price}"
    
    @staticmethod
    def from_json(data):
        return Receipt(
            name=data['name'],
            date=data['date'],
            count=data['count'],
            price=data['price'],
        )

# ---------------------------------------------------------------------------

while True:
    try:
        wide_walls = float(input("Masukkan luas dinding dalam m² : "))
        break
    except ValueError:
        print("\nLuas dinding tidak valid. Mohon masukkan angka yang benar!")

while True:
        buyer_name = input("Nama pembeli : ").strip()
        if buyer_name and buyer_name.replace(" ", " ").isalpha():
            break
        else:
            print("\nNama tidak valid. Mohon masukkan nama yang benar!")

while True:
    try:
        date = input("Masukkan tanggal pembelian (format: Hari/Bulan/Tahun) : ")
        date_convert = datetime.strptime(date, "%d/%m/%Y")
        format_date = date_convert.strftime("%d %B %Y")
        break
    except ValueError:
        print("\nTanggal tidak valid. Mohon masukkan tanggal yang benar!")


def outputs_receipt(buyer, date, wide):
    try:
        if wide < 1:
            raise GeneralFailure("Luas dinding kurang dari 1 meter persegi")
        
        count_paint = wide / 10
        total_paint = math.ceil(count_paint)

        price = 25000

        if total_paint > 10 and total_paint <= 25:
            price = 24500
        elif total_paint >= 26 and total_paint <= 50:
            price = 23000
        else:
            price = 22000

        total_price = price * total_paint

        data = {
            "name": buyer,
            "date": date,
            "count": total_paint,
            "price": total_price,
        }

        result = Receipt.from_json(data)

        return result.print_receipt()
    except GeneralFailure as e:
        return e.message
    except Exception as e:
        return f"Terjadi kesalahan {e}"
    

print(outputs_receipt(buyer_name, format_date, wide_walls))
