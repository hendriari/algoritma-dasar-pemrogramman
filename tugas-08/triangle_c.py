while True:
    try:
        number_length = int(input("Masukkan batasan: "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    current = 1
    for i in range(1, length + 1):
        if i % 2 == 1:
            for j in range(i):
                print(current, end=' ')
                current += 1
        else:
            start = current + i - 1
            for j in range(i):
                print(start, end=' ')
                start -= 1
                current += 1
        print()

outputs(number_length)
