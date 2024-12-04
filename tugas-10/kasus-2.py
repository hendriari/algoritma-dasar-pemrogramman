import pandas as pd

class MyProperty:
    def __init__(self, name, count, price, total_price):
        self.name = name
        self.count = count
        self.price = price
        self.total_price = total_price

def input_property():
        data = []

        while True:
            try:
                total_data = int(input("Berapa banyak data yang ingin anda input : "))
                if total_data <= 0:
                    print("Mohon input angka yang lebih dari 0")
                    continue
                else:
                    break
            except ValueError:
                print("Input harus berupa angka")

        for i in range(total_data):
            property_name = input(f"Masukkan nama barang ke-{i+1}: ")
            while True:
                try:
                    property_count = int(input(f"Masukkan jumlah barang ke-{i+1} : "))
                    if property_count <= 0:
                        print("Jumlah barang harus lebih dari 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Input tidak valid, mohon masukkan angka dengan benar!")
            while True:
                try:
                    property_price = float(input(f"Masukkan harga barang ke-{i+1}: "))
                    if property_price <= 0:
                        print("Harga barang harus lebih dari 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Input tidak valid, mohon masukkan angka dengan benar!")
            data.append(MyProperty(property_name, property_count, property_price, 0))

        return data

def count_stock(list_data):
    current_data = list_data
    for data in current_data:
        data.total_price = data.count * data.price
    return current_data

def show_my_property(list_data):
    data_list = [{"Nama": data.name, "Jumlah": data.count, "Harga": f"Rp.{data.price}", "Total Harga": f"Rp.{data.total_price}"} for data in list_data]
    data_frame = pd.DataFrame(data_list)
    print(data_frame)

def total_price_all_property(list_data):
    total_price = 0
    for e in list_data:
        total_price += e.total_price
    return total_price
    
if __name__ == "__main__":
    data = input_property()
    data_total_price = count_stock(data)
    show_data = show_my_property(data_total_price)
    print("")
    grand_total = total_price_all_property(data_total_price)
    print(f"Total nilai seluruh stock : Rp.{grand_total}")
    
    