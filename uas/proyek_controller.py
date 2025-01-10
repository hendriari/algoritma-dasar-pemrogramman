from proyek_entities import ProyekEntities
import pandas as pd
from tabulate import tabulate

class ProyekController():
    def __init__(self):
        self.proyek = ProyekEntities

    def get_data(self):
        return self.proyek.init_data()

    def menu(self):
        print("Menu Sistem :")
        print("1. Tampilkan Proyek")
        print("2. Tambah Proyek")
        select_menu = None
        try:
            choice = int(input("Menu yang anda pilih : "))
            select_menu = choice
            return select_menu 
        except ValueError:
            print("Menu tidak ditemukan")

    def show_proyek(self):
        data = self.proyek.init_data()
        if data:
            for e in data:
                persentase = e.waktu_berjalan / e.durasi * 100
                e.persentase_penyelesaian = persentase
                
            frame = [{"Nama proyek": item.nama_proyek, "Manager":item.manager_proyek, "Anggaran": item.anggaran, "Durasi": item.durasi, "Waktu Pengerjaan Berjalan": item.waktu_berjalan, "Persentase Penyelesaian (%)": item.persentase_penyelesaian} for item in data]
            df = pd.DataFrame(frame)
            print(tabulate(df.values, headers=df.columns, tablefmt='grid'))
            return data
        else:
            print("Data projek tidak ditemukan")

    def update_proyek(self, list_data):
        data = list_data
        while True:
            try:
                user_choice = int(input("Apa yang ingin anda lakukan (0 : update | 1 : add) ? "))
                if user_choice < 0 and user_choice > 1:
                    print("Pilihan tidak ada, mohon ulangi lagi")
                    continue
                else:
                    break
            except ValueError:
                print("Mohon masukkan angka yang valid")

        if user_choice == 0:
            print('Proyek mana yang ingin di update ? ')
            for i in range(len(data)):
                print(f"{i+1}. {data[i].nama_proyek}")

            update_choice = input('Nama proyek : ')
            selected_proyek = None
            selected_index = None
            while True:
                for i in range(len(data)):
                    if data[i].nama_proyek.lower() == update_choice.lower():
                        selected_proyek = data
                        selected_index = i
                    break
                if selected_proyek is None:
                    print('Proyek tidak ditemukan, proyek saat ini :')
                    break
                        
            if selected_proyek:
                print(f"Update data proyek {selected_proyek.nama_proyek}")
                data.remove(selected_proyek)
                selected_proyek.nama_proyek = input('Nama proyek : ')
                selected_proyek.manager_proyek = input('Manager proyek : ')
                
                while True:
                    try:
                        anggaran = int(input('Anggaran : '))
                        if anggaran < 1:
                            print("Anggaran tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            selected_proyek.anggaran = anggaran
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

                while True:
                    try:
                        durasi = int(input('Durasi : '))
                        if durasi < 1:
                            print("Durasi tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            selected_proyek.durasi = durasi
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

                
                while True:
                    try:
                        waktu_berjalan = int(input('Waktu Berjalan : '))
                        if durasi < 1:
                            print("Waktu berjalan tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            selected_proyek.waktu_berjalan = waktu_berjalan
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

                selected_proyek.persentase_penyelesaian = selected_proyek.waktu_berjalan / selected_proyek.durasi * 100

                data.insert(selected_index, selected_proyek)

        else:
            new_nama_proyek = input("Masukkan nama proyek: ")
            new_manager_proyek = input("Masukkan nama manager proyek: ")

            while True:
                    try:
                        new_anggaran = int(input('Anggaran : '))
                        if new_anggaran < 1:
                            print("Anggaran tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

            while True:
                    try:
                        new_durasi = int(input('Durasi : '))
                        if new_durasi < 1:
                            print("Durasi tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

                
            while True:
                    try:
                        new_waktu_berjalan = int(input('Waktu Berjalan : '))
                        if new_waktu_berjalan < 1:
                            print("Waktu berjalan tidak valid, mohon masukkan angka yang benar")
                            continue
                        else:
                            break
                    except ValueError:
                        print('Mohon masukkan angka yang valid')

            new_persentase = new_waktu_berjalan / new_durasi * 100
            new_proyek = ProyekEntities(new_nama_proyek, new_manager_proyek, new_anggaran, new_durasi, new_waktu_berjalan, new_persentase)
            data.append(new_proyek)


        frame = [{"Nama proyek": item.nama_proyek, "Manager":item.manager_proyek, "Anggaran": item.anggaran, "Durasi": item.durasi, "Waktu Pengerjaan Berjalan": item.waktu_berjalan, "Persentase Penyelesaian (%)": item.persentase_penyelesaian} for item in data]
        df = pd.DataFrame(frame)
        print(tabulate(df.values, headers=df.columns, tablefmt='grid'))

        