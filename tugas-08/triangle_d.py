while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')
        
def outputs(length):
    for i in range(length):
        for j in range(i, length):
            print(j + 1, end='')
        print()

outputs(number_length)
