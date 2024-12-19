import pandas as pd
from tabulate import tabulate

class Liblary:
    def __init__(self, no, index, title):
        self.no = no
        self.index = index
        self.title = title

    def get_list_book():
        result = []
        for i in range(6):
            no = 101 if i == 0 else 203 if i == 1 else 304 if i == 2 else 312 if i == 3 else 408 if i == 4 else 542
            title = "Laskar Pelangi" if i == 0 else "Bumi Manusia" if i == 1 else "Negeri 5 Menara" if i == 2 else "Perahu Kertas" if i == 3 else "Tenggelamnya Kapal Van Der Wijck" if i == 4 else "Seperti Dendam, Rindu Harus Dibayar Tuntas"
            result.append(Liblary(no, 0, title))

        if result:
            book_frame = [{"Nomor Seri": item.no, "Judul Buku": item.title} for item in result]
            df = pd.DataFrame(book_frame)
            print(tabulate(df.values, headers=df.columns, tablefmt='grid'))
        return result
    
    def search_book(data, target):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid].no == target:
                f_data = data[mid]
                result = Liblary(no=f_data.no, index=mid, title=f_data.title)
                return result
            elif data[mid].no < target:
                left = mid + 1
            else:
                right = mid - 1
        return
    
    def show_book(book):
        if book:
            print("")
            df = [["Seri Buku", book.no],
                ["Indexs", book.index],
                ["Judul Buku", book.title]]
            print(tabulate(df, headers=["Nomor Seri", "Index","Judul Buku"], tablefmt="grid"))
        else:
            print("Nomor seri tidak ditemukan")

if __name__ == "__main__":
    liblary = Liblary
    list_book = liblary.get_list_book()
    if list_book:
        while True:
            try: 
                choice = int(input("Masukkan nomor seri buku : "))
                break
            except ValueError: 
                print("Maaf inputan anda tidak valid, mohon masukan angka")
                continue
        
        book = liblary.search_book(list_book, choice)
        result = liblary.show_book(book)
