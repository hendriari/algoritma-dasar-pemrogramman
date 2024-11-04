import datetime
import math
from general_failure import GeneralFailure

# MENCOBA MENGGUNAKAN OOP DI PYTHON

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
        wide_walls = float(input('Luas dinding dalam m² : '))
        break
    except ValueError: 
        print("\nInput tidak valid. Mohon masukkan angka dengan benar.")

while True:
    buyer_name = input('Nama pembeli : ').strip() 
    if buyer_name and buyer_name.replace(" ", "").isalpha(): 
        break
    else:
        print("\nInput tidak valid. Mohon masukkan nama yang hanya terdiri dari huruf.")

date_now = datetime.datetime.now().strftime("%Y-%m-%d")

def outputs_receipt(wide, name):
    try:   
        if wide < 1:
            raise GeneralFailure("Luas dinding kurang dari 1 meter persegi")

        count_paint = wide / 10
        total_paint = math.ceil(count_paint)
            
        price = 25000 * total_paint

        data = {
            "name": name,
            "date": date_now,
            "count": total_paint,
            "price": price,
        }

        result = Receipt.from_json(data)

        return result.print_receipt()
    except GeneralFailure as e:
        return e.message()
    except Exception as e:
        return f'Terjadi kesalahan: {e}'
    
print(outputs_receipt(wide_walls, buyer_name))
