from datetime import datetime

menu = [
    {"id": 1, "name": "Ice Tea", "price": 6000},
    {"id": 2, "name": "Caramel Machiato", "price": 30000},
    {"id": 3, "name": "Green Tea Latte", "price": 25000},
    {"id": 4, "name": "Milkshake", "price": 15000},
    {"id": 5, "name": "Chocolate Hazelnut", "price": 25000},
]

while True:
    buyer_name = input("Nama pembeli : ").strip()
    if buyer_name and buyer_name.replace(" ", " ").isalpha():
        break
    else:
        print("\nNama tidak valid, mohon ulangi lagi")

while True:
    try:
        date = input("Masukkan tanggal pembelian (format: Hari/Bulan/Tahun) : ")
        date_convert = datetime.strptime(date, "%d/%m/%Y")
        date_format = date_convert.strftime("%d %B %Y")
        break
    except ValueError:
        print("\nTanggal tidak valid, mohon ulangi lagi dengan format hari/bulan/tahun")

while True:
    try:
        menu_id = int(input("Masukan ID menu : "))
        found_menu = False

        for element in menu:
            if element["id"] == menu_id:
                found_menu = True
                break
        
        if not found_menu:
            raise ValueError
        else:
            break
        
    except ValueError:
        print("\nMenu tidak di temukan, mohon ulangi lagi")

while True:
    try:
        purcase_amount = int(input("Masukkan jumlah pembelian : "))
        break
    except ValueError:
        print("\nJumlah pembelian tidak valid, mohon ulangi lagi")

def outputs(name, date, drink_id, amount):
    drink_name = next((item['name'] for item in menu if item['id'] == drink_id), None)
    drink_price = next((item['price'] for item in menu if item['id'] == drink_id), None)
    total_price = drink_price * amount
    return "----------------------------\n"+"\nNota Pembelian" + f"\nNama : {name}" + f"\nTanggal : {date}" + "\n" + f"\n{drink_name}  {amount}x" + f"\nTotal : {total_price}"


print(outputs(buyer_name, date_format, menu_id, purcase_amount))
