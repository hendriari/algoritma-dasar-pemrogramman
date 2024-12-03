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
        repeat = input("Apakah Anda ingin menginput lagi? (Y/N) : ")
        while repeat not in ['y', 'n']:
            print("Invalid input. Mohon masukkan Y atau N!\n")
            repeat = input("Apakah Anda ingin menginput lagi? (Y/N) : ").lower()
        if repeat == 'n':
            break

    return list_data

def outputs():
    data = process_list()
    for i, e in enumerate(data):
        print(f"Data ke {i + 1}: {e}")

outputs()

