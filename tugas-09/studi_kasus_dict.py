# EKO INGIN MEMBUAT SISTEM TASK MANAGEMENT SEDERHANA, BERISIKAN [ID TASK, TASK NAME, TASK DESCRIPTION, DEADLINE], BANTU EKO MEMBUAT SISTEM TERSEBUT
import random
from datetime import datetime
from tabulate import tabulate
import pandas as pd

def show_task(list_task):
    print("Daftar Task:")
    if list_task:
        task_df = [{"ID":e['id'], "Nama":e['task_name'], "Deskripsi":e['task_description'], "Tengat":e['deadline']} for e in list_task]
        df = pd.DataFrame(task_df)
        print(tabulate(df.values, headers=df.columns, tablefmt='grid'))
    else:
        print("Tidak ada task yang tersedia")

def add_task(current_task):
    result = current_task
    data = {
        "id": None,
        "task_name": None,
        "task_description": None,
        "deadline": None
    }
    name = input("Nama Task : ")
    description = input("Deskripsi Task : ")
    while True:
        try:
            date = input("Tengat Task (format: Hari/Bulan/Tahun) : ")
            convert = datetime.strptime(date, "%d/%m/%Y")
            deadline = convert.strftime("%d %B %Y")
            break
        except ValueError:
            print("Tengat harus berupa tanggal yang valid (format: Hari/Bulan/Tahun)")
    data['id'] = random.randint(100,999)
    data["task_name"] = name
    data["task_description"] = description
    data['deadline'] = deadline
    result.append(data)

    print("Sukses menambah task baru")
    return result

def menu():
    print("1. Menampilkan Task")
    print("2. Menambah Task")
    print("3. Keluar")
    while True:
        try:
            choice = int(input("Pilih Menu (1/2/3) : "))
            if choice < 1 or choice > 3:
                print("Opsi menu tidak tersedia (1/2/3)")
                continue
            elif choice == 3:
                return None
            else:
                break
        except ValueError:
            print("Pilihan anda tidak valid, mohon masukkan angka")
    return choice

if __name__ == "__main__":
    current_task = []
    while True:
        print("")
        menu_choice = menu()
        if menu_choice is None:
            print("Terima kasih..")
            break
        elif menu_choice == 1:
            print("")
            show_task(current_task)
        elif menu_choice == 2:
            print("")
            current_task = add_task(current_task)
        
    

    