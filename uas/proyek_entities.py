class ProyekEntities():
    def __init__(self, nama_proyek, manager_proyek, anggaran, durasi, waktu_berjalan, persentase_penyelesaian):
        self.nama_proyek = nama_proyek
        self.manager_proyek = manager_proyek
        self.anggaran = anggaran
        self.durasi = durasi
        self.waktu_berjalan = waktu_berjalan
        self.persentase_penyelesaian = persentase_penyelesaian
        

    def init_data():
        data = []
        for i in range(4):
            nama_proyek = 'Jembatan Lombok Bali' if i == 0 else 'Mall Citragrand' if i == 1 else 'Gedung Garuda IKN' if i == 2 else 'Gedung Aula SMA Sidojati'
            manager_proyek = 'Andi Pratama' if i == 0 else 'Budi Santoso' if i == 1 else 'Citra Dewi' if i == 2 else 'Dwi Hartono'
            anggaran = 500 if i == 0 else 750 if i == 1 else 600 if i == 2 else 400
            durasi = 12 if i == 0 else 18 if i == 1 else 24 if i == 2 else 8
            waktu_berjalan = 6 if i == 0 else 9 if i == 1 else 15 if i == 2 else 8
            persentase = 0
            data.append(ProyekEntities(nama_proyek, manager_proyek, anggaran, durasi, waktu_berjalan, persentase))
        return data
            

