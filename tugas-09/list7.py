def outputs():
    data = [1, 2, 3, 7, 4, 5, 6, 7, 2]
    
    for i in range(len(data) - 1, -1, -1):
        if data[i] % 2 != 0:
            print(f"{data[i]} terdapat pada index ke-{i}")
            break

outputs()
