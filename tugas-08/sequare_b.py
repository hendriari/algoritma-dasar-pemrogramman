while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    binary = "01010"
    binary2 = "10101"
    for i in range(length):
        if i % 2 == 0:
            print(binary2)
        else:
            print(binary)

outputs(number_length)