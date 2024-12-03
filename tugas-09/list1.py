def list_data():
    result = []
    while len(result) < 20:
        inputter = str(input(f"Masukkan data ke {len(result) + 1} = "))
        result.append(inputter)
    print('Data telah selesai di masukkan')
    print('')
    return result

def outputs():
    data = list_data()
    print('Hasil :')
    for i, e in enumerate(data):
        print(f"Data ke {i + 1} = {e}")

outputs()