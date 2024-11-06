from datetime import datetime
import math

class BrandAmountPrice:
    def __init__(self,min_amount, max_amount, price):
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.price = price

class Brand:
    def __init__(self, brand_id, brand_name, list_price):
        self.brand_id = brand_id
        self.brand_name = brand_name
        self.list_price = list_price

    @staticmethod
    def add_list_brand():
        list_brand = []
    
        for i in range(5):
            brand_id = "DUL" if i == 0 else "CAT" if i == 1 else "NIP" if i == 2 else "AVI" if i == 3 else "MOW"
            brand_name = "Dulux" if i == 0 else "Catylac" if i == 1 else "Nippon Paint" if i == 2 else "Avitex" if i == 3 else "Mowilex"
            list_brand.append(Brand(brand_id, brand_name, []))
        
        for element in list_brand:
            for i in range(3):
                if element.brand_id == "DUL":
                    element.list_price.append(BrandAmountPrice(1 if i == 0 else 26 if i == 1 else 51, 25 if i == 0 else 50 if i == 1 else math.inf, 24500 if i == 0 else 23000 if i == 1 else 22000))
                elif element.brand_id == "CAT":
                    element.list_price.append(BrandAmountPrice(1 if i == 0 else 26 if i == 1 else 51, 25 if i == 0 else 50 if i == 1 else math.inf, 23500 if i == 0 else 22500 if i == 1 else 21000))
                elif element.brand_id == "NIP":
                    element.list_price.append(BrandAmountPrice(1 if i == 0 else 26 if i == 1 else 51, 25 if i == 0 else 50 if i == 1 else math.inf, 23500 if i == 0 else 22000 if i == 1 else 20500))
                elif element.brand_id == "AVI":
                    element.list_price.append(BrandAmountPrice(1 if i == 0 else 26 if i == 1 else 51, 25 if i == 0 else 50 if i == 1 else math.inf, 20000 if i == 0 else 19000 if i == 1 else 17500))
                elif element.brand_id == "MOW":
                    element.list_price.append(BrandAmountPrice(1 if i == 0 else 26 if i == 1 else 51, 25 if i == 0 else 50 if i == 1 else math.inf, 18500 if i == 0 else 17000 if i == 1 else 16000))
        return list_brand

    @staticmethod
    def print_pricelist(brands):
        print("\n********************* MENU *****************")
        for i, brand in enumerate(brands):
            print(f"{'' if i == 0 else '--------------------------------------'}" + f"\nBrand Id: {brand.brand_id}, Brand Name: {brand.brand_name}")
            for price in brand.list_price:
                print(f"   Min Amount : {price.min_amount}, Max Amount: {'Tak terbatas' if price.max_amount == math.inf else price.max_amount}, Price: {price.price}")

class Receipt:
    def __init__(self, name, date, count, brand_name, price):
        self.name = name
        self.date = date
        self.count = count
        self.brand_name = brand_name
        self.price = price

    def print_receipt(self):
        return "\nNota Pembelian" + f"\nNama Pembeli : {self.name}" + f"\nTanggal Pembelian : {self.date}" + f"\nMerk Kaleng : {self.brand_name}"+ f"\nJumlah Kaleng Cat : {self.count} kaleng" + f"\nTotal Harga : {self.price}"
    
    @staticmethod
    def from_json(data):
        return Receipt(
            name=data['name'],
            date=data['date'],
            brand_name=data['brand_name'],
            count=data['count'],
            price=data['price'],
        )

# ---------------------------------------------------------------------------


brand_price_list = Brand.add_list_brand()

Brand.print_pricelist(brand_price_list)

print("\n----------------------\n")

while True:
        paint_brand = input("Merk Cat : ").strip()
        selected_brand = next((item for item in brand_price_list if item.brand_id == paint_brand.upper()), None)
        if paint_brand and paint_brand.replace(" ", "").isalpha():
            if selected_brand == None:
                print("\nMerk Cat tidak ditemukan, mohon masukkan ID cat sesuai menu diatas")
            else:
                break
        else:
            print("\nMerk Cat tidak valid. Mohon masukkan nama hanya dengan huruf!")

while True:
    try:
        wide_walls = float(input("Masukkan luas dinding dalam m² : "))
        if(wide_walls < 1):
            print("\nLuas dinding tidak boleh kurang dari 1 m²")
        else:
            break  
    except ValueError:
        print("\nLuas dinding tidak valid. Mohon masukkan angka yang benar!")

while True:
        buyer_name = input("Nama pembeli : ").strip()
        if buyer_name and buyer_name.replace(" ", "").isalpha():
            break
        else:
            print("\nNama tidak valid. Mohon masukkan nama hanya dengan huruf!")

while True:
    try:
        date = input("Masukkan tanggal pembelian (format: Hari/Bulan/Tahun) : ")
        date_convert = datetime.strptime(date, "%d/%m/%Y")
        format_date = date_convert.strftime("%d %B %Y")
        break
    except ValueError:
        print("\nTanggal tidak valid. Mohon masukkan tanggal yang benar!")


def outputs_receipt(buyer, date, wide, brand):
    try:
        count_paint = wide / 10
        total_paint = math.ceil(count_paint)

        discount_price = next((item for item in brand.list_price if total_paint < item.max_amount and total_paint >= item.min_amount), None)

        total_price = discount_price.price * total_paint

        data = {
            "name": buyer,
            "date": date,
            "brand_name": f"{brand.brand_name} ({brand.brand_id})",
            "count": total_paint,
            "price": total_price,
        }

        result = Receipt.from_json(data)

        return result.print_receipt()
    except Exception as e:
        return f"Terjadi kesalahan {e}"
    

print(outputs_receipt(buyer_name, format_date, wide_walls, selected_brand))

