while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    for i in range(length):
        result = ''.join(str((i + j) % 10) for j in range(1, 6))
        print(result)

outputs(number_length)
