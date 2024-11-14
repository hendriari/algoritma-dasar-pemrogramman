jumlah_ayam = 3
usia_ayam = 3
jangka_usia_ayam_bertelur = 20 - usia_ayam
telur_ayam_sehari_per_ayam = 3
hari_dalam_sebulan = 30
biaya_pakan_perbulan = 200000
harga_telur_per_kg = 14500 
butir_per_kg_telur = 14

jumlah_telur_dihasilkan = 0
total_kilo_telur = 0
keuntungan_penjualan = 0

for i in range(jangka_usia_ayam_bertelur):
    usia_ayam+=1
    if usia_ayam > 4:
        jumlah_telur_perbulan = (telur_ayam_sehari_per_ayam * jumlah_ayam) * hari_dalam_sebulan
        jumlah_telur_dihasilkan += jumlah_telur_perbulan
        print(f"Bulan ke {i+1} semenjak membeli ayam : {jumlah_telur_dihasilkan} telur")
    else:
        print(f"Bulan ke {i+1} semenjak membeli ayam : 0 telur")

total_biaya_pakan = biaya_pakan_perbulan * jangka_usia_ayam_bertelur
total_kilo_telur = jumlah_telur_dihasilkan / butir_per_kg_telur
keuntungan_penjualan = total_kilo_telur * harga_telur_per_kg - total_biaya_pakan

print()
print(f"Biaya pakan keseluruhan : Rp.{total_biaya_pakan:,.2f}")
print(f"Toal telur dalam kilogram : {total_kilo_telur:.2f}kg")
print(f"Keuntungan penjualan : Rp.{keuntungan_penjualan:,.2f}")

