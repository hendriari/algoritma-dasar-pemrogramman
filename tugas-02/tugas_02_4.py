a = 1
b = 4
print("Hasil a yang pertama: "+str(a))
print("Hasil b yang pertama: "+str(b))

b = a
a -= b
print("Hasil a yang kedua: "+str(a))
print("Hasil b yang kedua: "+str(b))

a = b + 1
b = a // b 
print("Hasil a yang kedua: "+str(a))
print("Hasil b yang kedua: "+str(b))