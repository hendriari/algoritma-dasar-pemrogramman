price_product = 15000

price_delivery = 0.08

price_selling_products = 25000

total_day = 31

# TCP = TOTAL COUNT PRODUCT PER DAY
tcp = int(input('Total Konsistensi Produksi Produk Per Hari : '))

# -----------------------------------------------------------------------------------
# 1. Total biaya produksi (termasuk biaya tetap dan biaya pengiriman) dalam sebulan.
# -----------------------------------------------------------------------------------

# TPP = TOTAL PRICE PRODUCTION
tpp = price_product * tcp * total_day
# TPD = TOTAL PRICE DEILVERY
tpd = tpp * price_delivery
# TOTAL PRODUCTION COST IN A MONTH
monthly_fee = tpp + tpd

# print(tcp)
print(f"Total Biaya Produksi Dalam 1 Bulan : Rp. {monthly_fee}")

# -----------------------------------------------------------------------------------
# 2. Total pendapatan dalam sebulan.
# -----------------------------------------------------------------------------------

profit = (price_selling_products * tcp) * total_day

print(f"Total Keuntungan Dalam 1 Bulan : Rp. {profit}")

# -----------------------------------------------------------------------------------
# 3. Keuntungan bersih dalam sebulan setelah dikurangi semua biaya
# -----------------------------------------------------------------------------------

net_profit = profit - monthly_fee

print(f"Jika Terjual Semua Maka Total Keuntungan Bersih Dalam 1 Bulan : Rp. {net_profit}")