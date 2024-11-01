price_ticket = 50000

age = int(input("Usia Anda : "))

def result(discount):
    discount_amount = price_ticket * (discount / 100)
    final_price = price_ticket - discount_amount
    return final_price

def outputs(age, discount, priceTicket):
    return (f"\nUsia : {age}" + f"\nDiskon : {discount}%" + f"\nHarga Tiket : {priceTicket}")

if age < 12:
    print(outputs(age, 10, result(10)))
elif age >= 12 and age < 17:
    print(outputs(age, 5, result(5)))
elif age >= 18 and age <= 59:
    print("Maaf tidak ada diskon")
elif age >= 60:
    print(outputs(age, 20, result(20)))
else:
    print('Usia tidak valid')
