while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    for i in range(length):
        result = "".join(str(i + 1) for i in range(5))
        print(result)

outputs(number_length)
