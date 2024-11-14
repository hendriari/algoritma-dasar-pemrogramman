count_data = int(input("Masukkan Berapa banyak data yang kamu inginkan : "))

def outputs(count):
    for i in range(count):
        input(f"Masukkan data ke {i+1} : ")
    print("Data sudah lengkap")
        
print(outputs(count_data))