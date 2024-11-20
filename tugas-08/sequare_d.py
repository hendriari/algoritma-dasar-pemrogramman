while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    binary = "01110"
    binary2 = "10001"
    count = 0
    for i in range(length):
        if count == 0 or count == 4:
            print(binary)
        else:
            print(binary2)
        count += 1
        if count == 5:
            count = 0

outputs(number_length)
