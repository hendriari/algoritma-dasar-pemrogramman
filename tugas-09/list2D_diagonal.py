matrix = [
    [2, 4, 7, 7, 1],
    [8, 9, 1, 8, 2],
    [5, 3, 6, 3, 1],
    [7, 8, 1, 0, 5],
    [2, 1, 3, 4, 9]
]

def outputs(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    print(f'Hasil : {total}')

outputs(matrix)
