def count_data():
    while True:
        try:
            total = int(input("Masukkan jumlah data yang diinginkan : "))
            return total
        except ValueError:
            print("Invalid input. Mohon masukkan angka!\n")

def input_list(length, current_index):
    result = []
    while len(result) < length:
        try:
            index = (current_index + len(result)) + 1
            inputter = float(input(f"Masukkan data ke {index} berupa angka : "))
            result.append(inputter)
        except ValueError:
            print("Invalid input. Mohon masukkan angka!\n")
            
    return result

def process_list():
    list_data = []
    while True:
        length = count_data()  
        new_data = input_list(length, len(list_data))
        list_data.extend(new_data)
        repeat = input("Apakah Anda ingin menginput lagi? (Y/N) : ").lower()
        
        while repeat not in ['y', 'n']:
            print("Invalid input. Mohon masukkan Y atau N!\n")
            repeat = input("Apakah Anda ingin menginput lagi? (Y/N) : ").lower()
        if repeat == 'n':
            break
    
    return list_data

def filter_data(data):
    while True:
        try:
            find_item = float(input("Data apa yang anda cari ? : "))
            break
        except ValueError:
            print("Invalid input. Mohon masukkan angka!\n")
    
    for i, e in enumerate(data):
        if find_item == e:
            return f"Data {e} ditemukan pada index ke-{i}"
    
    return f"Data {find_item} tidak ditemukan"

def outputs():
    result = filter_data(process_list())
    print(result)

outputs()

