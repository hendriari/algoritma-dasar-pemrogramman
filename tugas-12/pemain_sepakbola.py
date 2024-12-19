import pandas as pd
from tabulate import tabulate

class FootballClub:
    def __init__(self, no, name, club):
        self.no = no
        self.name = name
        self.club = club

    def get_list_club():
        resut = []
        for i in range(7):
            name = "Ronaldo" if i == 0 else "Messi" if i == 1 else "Benzema" if i == 2 else "Azpilicueta" if i == 3 else "Pogba" if i == 4 else "Vazquez" if i == 5 else "Salah"
            club = "Juventus" if i == 0 else "Barcelona" if i == 1 else "Real Madrid" if i == 2 else "Chelsea" if i == 3 else "Manchester United" if i == 4 else "Real Madrid" if i == 5 else "Liverpool"
            resut.append(FootballClub(i+1, name, club))
        
        if resut:
            club_frame = [{"Nomor Pungung": item.no, "Nama Pemain": item.name, "Asal Club": item.club} for item in resut]
            df = pd.DataFrame(club_frame)
            print(tabulate(df.values, headers=df.columns, tablefmt='grid'))
        return resut
    
    def search_soccer_player(self, list_data):
        player = input("Masukkan nama atau nomor punggung pemain : ")
        list_data = list_data
        if list_data:
            for e in list_data:
                if player.lower() == e.name.lower() or player == str(e.no):
                    return e
            choice = input("Data pemain tidak tersedia, apakah anda ingin mengulanginya (y/n) ? : ")            
            if choice.lower() == 'y':
                return self.search_soccer_player(self, list_data)
            elif choice.lower() == 'n':
                print("Baiklah...")
                return None
            else:
                print("Maaf, pilihan anda tidak valid mohon masukkan (y/n)")
                return self.search_soccer_player(self, list_data)
        else:
            print("Data tidak tersedia")
            return None
        
    def show_soccer_player(player):
        if player:
            print("")
            df = [["Nomor Punggung", player.no],
                ["Nama Pemain", player.name],
                ["Asal Club", player.club]]
            print(tabulate(df, headers=["Keterangan", "Data"], tablefmt="grid"))
        else:
            print("Data pemain tidak tersedia")

        
if __name__ == "__main__":
    football = FootballClub
    list_data = football.get_list_club()
    player = football.search_soccer_player(football, list_data)
    result = football.show_soccer_player(player)

        