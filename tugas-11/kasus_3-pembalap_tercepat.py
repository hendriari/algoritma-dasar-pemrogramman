def faster_racer():
    result = []
    for i in range(5):
        while True:
            try:
                time = float(input(f"Waktu tempuh pembalap ke {i+1} : "))
                if time < 0:
                    print("Waktu tidak boleh negatif")
                    continue
                else:
                    break
            except ValueError:
                print("Maaf, Mohon masukkan angka yang valid.")
        result.append(time)

    for i in range(len(result)):
        min_index = i
        for j in range (i, len(result)):
            if result[j] < result[min_index]:
                min_index = j
                result[i], result[min_index] = result[min_index], result[i]
        
    return result

def winner_racer(data):
    if not data:
        return 0
    return min(data)

if __name__ == "__main__":
    racer = faster_racer()
    winner = winner_racer(racer)
    print(f"Waktu tempuh dari yang tercepat ke paling lambat : {racer}")
    print(f"Pemenang adalah pembalap dengan waktu tercepat : {winner} detik")