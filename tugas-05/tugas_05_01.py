while True:
    name = input("Nama anda : ").strip()
    if name and name.replace(" ", "").isalpha():
        break
    else:
        print("\nNama tidak valid, mohon masukkan Nama hanya menggunakan huruf")

while True:
    try:
        nim = int(input("NIM anda : "))
        if nim >= 1:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nNIM tidak valid, mohon masukkan NIM dengan benar")
    
address = input("Alamat anda : ")

while True:
    try:
        ipk = float(input("IPK anda : "))
        if ipk > .1:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nIPK tidak valid, mohon masukkan IPK dengan benar")

while True:
    try:
        semester = int(input("Semester anda : "))
        if semester >= 1:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nSemester tidak valid, mohon masukkan Semester dengan benar")

while True:
    parent_name = input("Nama orang tua anda : ").strip()
    if parent_name and parent_name.replace(" ", "").isalpha():
        break
    else:
        print("\nNama Orang Tua tidak valid, mohon masukkan Nama hanya menggunakan huruf")

female_parent_job = input("Pekerjaan orang tua Perempuan : ")

while True:
    try:
        parent_sallary = float(input("Gaji orang tua per bulan : "))
        if parent_sallary > 1:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nGaji Orang Tua tidak valid, mohon masukkan Gaji dengan benar")


def scholarship():
    if ipk >= 3:
        if semester >= 5 and parent_sallary < 3000000:
            return "Selamat, Anda Berhak Menerima Beasiswa"
    elif ipk < 3:
        return "Maaf Anda Belum Diterima, IPK Anda Kurang Dari 3.00"
    
print(scholarship())