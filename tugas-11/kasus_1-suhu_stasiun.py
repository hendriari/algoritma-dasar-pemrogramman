def list_temperature():
    result = []
    for i in range(5):
        while True:
            try:
                suhu = float(input(f"Masukkan suhu kota ke {i+1} : "))
                break
            except ValueError:
                print("Maaf, Mohon masukkan angka yang valid.")
        result.append(suhu)

    for i in range(0, len(result)):
        for j in range(0, len(result)-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    return result

def lowest_temperature(data):
    if not data:
        return 0
    return min(data)

def average_temperature(data):
    average = 0
    for i, e in enumerate(data):
        average += e
    result = average / len(data)
    return result

if __name__ == "__main__":
    data = list_temperature()
    print('')
    for i in range(len(data)):
        print(f"Suhu kota ke {i+1} : {data[i]}")
    print(f"Suhu terendah: {lowest_temperature(data)}")
    print(f"Suhu rata rata : {average_temperature(data)}")