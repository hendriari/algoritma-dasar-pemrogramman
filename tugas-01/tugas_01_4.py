a = 'Investasi'
b = 234.2
c = 2025
d = True
e = ["tahun",2024, "budi memulai investasinya"]
f = {"total": 12131332323223.2, "kenyataan": False}

print("Budi suka", a, type(a), "\n")
print("Total assetnya dalam emas sekarang", b, "kilo", type(b), "\n")
print("Budi akan kaya pada tahun", c, type(c),"\n")
print("Sekarang budi", "bisa" if d else "tidak bisa", "membeli mobil", type(d),"\n")
for element in e:
    print(element,f"{type(element)}", type(e), "\n")
print("total kekayaan budi sebesar", f['total'], type(f['total']), type(f), "\napakah mimpi budi tersebut akan menjadi nyata?", f["kenyataan"], type(f['kenyataan']), type(f))