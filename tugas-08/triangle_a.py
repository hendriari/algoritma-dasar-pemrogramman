while True:
    try:
        number_length = int(input("Masukkan batasan triangle : "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(length):
    result = 0
    numbers = 1
    for i in range(length):
        for j in range(i+1):
            numbers + i
            result = numbers + j
            print(f"{result}", end=' ')
        print()

outputs(number_length)