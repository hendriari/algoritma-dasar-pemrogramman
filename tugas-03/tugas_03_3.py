import math

# NOTE :
#   - PAK OUTPUT YANG DIMAKSUD APA YA?
#   - APA YANG HARUS DIKALKULASI?
#   - YANG PENTING BILANGANA POSITIF KAH?

jari_jari_tabung = 2.0
tinggi_tabung = 12.0

volume_tabung = math.pi * (jari_jari_tabung ** 2) * tinggi_tabung

while True:
    try:
        volume_kelereng = float(input('Masukkan volume kelereng dalam cm³ : '))
        if volume_kelereng <= 0:
            raise ValueError("Volume harus lebih dari 0")
        break
    except ValueError: 
        print("\nInput tidak valid. Mohon masukkan angka dengan benar")

jari_jari_kelereng = ((3 * volume_kelereng) / (4 * math.pi)) ** (1/3)

print(f"Jari-jari kelereng: {jari_jari_kelereng:.3f} cm")

if volume_kelereng > volume_tabung:
    print("Kelereng tidak dapat masuk di dalam tabung")
else:
    sisa_volume = volume_tabung - volume_kelereng
    print(f"Sisa volume di tabung setelah dimasukin kelereng: {sisa_volume:.3f} cm³")
