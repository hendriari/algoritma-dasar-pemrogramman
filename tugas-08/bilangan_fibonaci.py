while True:
    try:
        fibonacci_length = int(input("Jumlah fibonacci yang di inginkan : "))
        break
    except ValueError:
        print('Hanya boleh memasukkan angka! mohon ulangi lagi\n')

def outputs(lenght_number):
    a = 0
    b = 1
    length = 0
    while length < lenght_number:
        result = a
        print(result, end=' ')
        result = a + b
        a = b
        b = result
        length += 1
    return

outputs(fibonacci_length)