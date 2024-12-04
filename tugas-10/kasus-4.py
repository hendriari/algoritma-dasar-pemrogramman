def input_number():
    while True:
        try:
            numbers = int(input("Masukkan bilangan bulat positif : "))
            if numbers <= 0:
                print("Mohon masukkan bilangan bulat positif")
                continue
            else:
                return numbers
        except ValueError:
            print("Input yang Anda masukkan bukanlah bilangan bulat positif")

def factorial(n):
    if n == 0:
        return 0
    else:
        return n % 10 + factorial(n // 10)
    
if __name__ == "__main__":
    number = input_number()
    result = factorial(number)
    print(f"Faktorial dari {number} adalah {result}")

    
