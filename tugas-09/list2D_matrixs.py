matrix_1 = [
    [2, 4, 7, 7, 1],
    [8, 9, 1, 8, 2],
    [5, 3, 6, 3, 1],
    [7, 8, 1, 0, 5],
    [2, 1, 3, 4, 9]
]

matrix_2 = [
    [-9, 4, 7, 5, 1],
    [3, 1, 1, 5, 2],
    [2, 3, 2, 3, 9],
    [4, 3, 1, 0, 5],
    [1, 2, 3, 4, 0]
]

def show_matrixs(matrix_1, matrix_2):
    print("List matrix :")
    for i, e in enumerate(matrix_1):
        print(f"Matrix 1 row {i+1}: {e}")
    print("")
    for i, e in enumerate(matrix_2):
        print(f"Matrix 2 row {i+1}: {e}")

def matrix_addition(matrix_1, matrix_2):
    list_data = []
    if len(matrix_1) != len(matrix_2):
        print("\nPenjumlahan gagal, Panjang jumlah matrix harus sama")
        return None
    for i in range(len(matrix_1)):
        row_data = []
        for j in range(len(matrix_1[0])):
            if j < len(matrix_2[i]):
                row_data.append(matrix_1[i][j] + matrix_2[i][j])
            else:
                row_data.append(matrix_1[i][j])
        list_data.append(row_data)

    print("\nPenjumlahan matrix : ")
    for e in list_data:
        print(e)
    return list_data

def matrix_substaction(matrix_1, matrix_2):
    list_data = []
    if len(matrix_1[0]) != len(matrix_2[1]):
        print("\nPengurangan gagal, Lebar jumlah matrix harus sama")
        return None
    for i in range(len(matrix_1)):
        list_data.append(matrix_1[0][i] - matrix_2[1][i])

    print("\nPengurangan matrix : ")
    for e in list_data:
        print(e)
    return list_data

def matrix_multiplication(matrix_1, matrix_2):
    list_data = []
    if len(matrix_1) != len(matrix_2):
        print("Perkalian gagal, Panjang jumlah matrix harus sama")
        return None
    for i in range(len(matrix_1)):
        row_data = []
        for j in range(len(matrix_1[0])):
            if j < len(matrix_2[i]):
                row_data.append(matrix_1[i][j] * matrix_2[i][j])
            else:
                row_data.append(matrix_1[i][j])
        list_data.append(row_data)
    
    print("\nPerkalian matrix : ")
    for e in list_data:
        print(e)
    return list_data

if __name__ == "__main__":
    show_matrixs(matrix_1, matrix_2)
    matrix_addition(matrix_1, matrix_2)
    matrix_substaction(matrix_1, matrix_2)
    matrix_multiplication(matrix_1, matrix_2)
