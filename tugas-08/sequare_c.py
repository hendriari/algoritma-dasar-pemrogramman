while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    binary = "11011"
    binary2 = "00000"
    for i in range(length):
        if i % 3 == 2: 
            print(binary2)
        else:
            print(binary)

outputs(number_length)
