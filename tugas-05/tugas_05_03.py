import random
import locale
import time

# IBU ANDA ULANG TAHUN, ANDA INGIN MEMBELIKAN SESUATU UNTUK IBU ANDA, 
# NAMUN ANDA TIDAK TAU BARANG APA YANG COCOK UNTUK IBU.
# ANDA MENANYAKAN APA YANG IBU INGINKAN, ANDA AKAN MEMBELI KAN APAPUN YANG IBU ANDA SEBUTKAN JIKA SALDO ANDA CUKUP

class MomFavorite:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def generate_favorite_items():
        list_favorite = []

        for i in range(8):
            name = "Emas" if i == 0 else "Berlian" if i == 1 else "Mobil" if i == 2 else "Jet Pribadi" if i == 3 else "Pesawat Garuda" if i == 4 else "Helikopter" if i == 5 else "Moge" if i == 6 else "Nasi Pecel"
            price = 1000000 if i == 0 else 500000000 if i == 1 else 654003000 if i == 2 else 452352135223525235 if i == 3 else 35423756256234623 if i == 4 else 485645627356256752 if i == 5 else 35423543267 if i == 6 else 10000
            list_favorite.append(MomFavorite(name, price))
        return list_favorite

    @staticmethod
    def get_mom_choice(list_favorite):
        return random.choice(list_favorite)
    
locale.setlocale(locale.LC_ALL, '')

while True:
    try:
        your_wallet = float(input("Masukkan saldo dompet anda : "))
        break
    except ValueError:
        print("Input tidak valid. Silakan coba lagi!")


mom_list_choice = MomFavorite.generate_favorite_items()

def outputs(wallet, list_choice):
    print("\nAnda menanyakan yang ibu inginkan")
    
    print("\nIbu sedang berfikir..")
    time.sleep(1)

    mom_choice = MomFavorite.get_mom_choice(list_choice)

    print(f"\nIBU : Nak Ibu pengen beli {mom_choice.name}, harganya murah cuman {locale.currency(mom_choice.price, grouping=True)}")

    while True:
        if wallet > mom_choice.price:
            print('\nANDA : Oke Bu tak belikke sekarang, gas!')
            break
        else:
            print('\nANDA : Apakah ndak ada yang lain Bu?')
            time.sleep(.5)
            print("\nIBU : Sebentar, apa ya kira-kira..")
            time.sleep(2)
            mom_choice = MomFavorite.get_mom_choice(list_choice)
            print(f"\nIBU : Yaudah kalo gitu {mom_choice.name} saja nak, harganya cuman {locale.currency(mom_choice.price, grouping=True)}")

            if wallet < mom_choice.price:
                print('\nANDA : Ah ibu aneh aneh aja, yausudah nggak jadi')
                break
            else:
                print('\nANDA : Gas ayo beli!')
                break

outputs(your_wallet, mom_list_choice)
