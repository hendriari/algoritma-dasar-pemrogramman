while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    for i in range(1, length + 1):
        if i % 2 == 1:
            for j in range(i, length + 1):
                print(j ** 2, end=' ')
        else:
            for j in range(i, length + 1):
                print(j, end=' ')
        print()

outputs(number_length)
