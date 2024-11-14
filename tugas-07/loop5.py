count = 0
average = 0

for i in range(1, 61):
    if i % 3 == 0:
        print(i, end=' ')
        count += i
        average +=1

print(f"\nRata rata = {count / average if average > 0 else 0}")