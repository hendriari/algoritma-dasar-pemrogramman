def jumlah_hadir():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah hadir : "))
            if jumlah < 0 or jumlah > 31:
                print("Jumlah kehadiran harus antara 0 dan 31.")
                continue
            return jumlah
        except ValueError:
            print("Maaf, Mohon masukkan angka yang valid.")

def nama_karyawan():
    return input("Masukkan nama anda : ")

def uang_transport(jumlah_kehadiran):
    if jumlah_kehadiran >= 20:
        return 300000
    return 0
    
def uang_bonus(jumlah_kehadiran):
    if jumlah_kehadiran >= 22:
        return 100000 * jumlah_kehadiran
    return 0
    
def gaji_pokok():
    return 3000000 

def outputs():
    nama = nama_karyawan()
    jumlah = jumlah_hadir()
    transport = uang_transport(jumlah)
    bonus = uang_bonus(jumlah)
    gaji = gaji_pokok()
    total_gaji = gaji + transport + bonus
    print(f"Nama : {nama}")
    print(f"Jumlah Kehadiran : {jumlah} hari")
    print(f"Gaji Pokok : Rp {gaji}")
    print(f"Uang Transport : Rp {transport}")
    print(f"Bonus : Rp {bonus}")
    print(f"Gaji Total : Rp {total_gaji}")

if __name__ == "__main__":
    outputs()