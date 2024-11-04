while True:
    try:
        body_weight = float(input("Berat badan Anda : "))
        break
    except ValueError:
        print("Mohon masukkan angka saja!")

while True:
    try:
        body_height = float(input("Tinggi badan Anda : "))
        break
    except ValueError:
        print("Mohon masukkan angka saja!")

def outputs(weight, height):
    bmi = weight / (height ** 2)

    description = ""

    if bmi < 18:
        description = "Under Weight/Kurus – Sebaiknya mulai menambah berat badan dan mengkonsumsi makanan berkarbohidrat di imbangi dengan olah raga"
    elif bmi < 25:
        description = "Normal Weight/Normal – Bagus, berat badan anda termasuk kategori ideal"
    elif bmi < 27: 
        description = "Over Weight/Kegemukan – anda sudah masuk kategori gemuk. sebaiknya hindari makanan berlemak dan mulailah meningkatkan olahraga seminggu minimal 2 kali"
    else:
        description = "Obesitas – Sebaiknya segera membuat program menurunkan berat badan karena anda termasuk kategori obesitas/ terlalu gemuk dan tidak baik bagi kesehatan"

    return f"BMI : {bmi}" + f"\nKeterangan : {description}"

print(outputs(body_weight, body_height))