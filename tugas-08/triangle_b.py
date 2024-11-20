while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    for i in range(1, length + 1):
        result = []
        for j in range(1, i + 1):
            result.append(2 * j)
        result = result + result[::-1][1:]
        print(" ".join(map(str, result)))

outputs(number_length)
