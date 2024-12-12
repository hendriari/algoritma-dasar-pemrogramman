def input_array():
    result = []
    while True:
        try:
            length_data = int(input("Berapa data yang ingin anda masukkan ? : "))
            if length_data >= 1:
                break
            else:
                continue
        except ValueError:
            print("Maaf, Mohon masukkan angka yang valid.")

    for i in range(length_data):
        while True:
            try:
                data = int(input(f"Masukkan data ke-{i+1} : "))
                break
            except ValueError:
                print("Maaf, Mohon masukkan angka yang valid.")
        result.append(data)

    return result

def check_shorted_data(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

if __name__ == "__main__":
    array = input_array()
    is_shorted = check_shorted_data(array)
    print(f"Array sudah ke shorting ? = {is_shorted}")
