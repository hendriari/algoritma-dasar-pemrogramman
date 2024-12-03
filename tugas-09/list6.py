def outputs():
    data = [1, 2, 3, 7, 4, 5, 6, 7]
    count = 0
        
    for i, e in enumerate(data):
        if e % 2 == 0:
            count += 1
            if count == 2:
                print(f"Angka {e} ditemukan di index ke-{i}")

outputs()