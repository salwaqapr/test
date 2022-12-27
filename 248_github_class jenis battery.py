class battery:
    '''dasar kelas untuk battery'''
    jumlah_battery = 0

    def __init__(self, nama, jenis):
        self.nama=nama
        self.jenis=jenis
        battery.jumlah_battery += 1

    def tampilkan_jumlah(self):
        print("total battery : ", battery.jumlah_battery)

    def tampilkan_data(self):
        print("nama :", self.nama)
        print("jenis :", self.jenis)

# membuat object dari kelas battery
battery1 = battery("Zinc karbon", "primer")
battery2 = battery("alkaline", "primer")
battery3 = battery("lithium", "primer")
battery4 = battery("silver oxide", "primer")
battery5 = battery("Ni-cd", "sekunder")
battery6 = battery("Ni-MH", "sekunder")

battery1.tampilkan_data()
battery2.tampilkan_data()
battery3.tampilkan_data()
battery4.tampilkan_data()
battery5.tampilkan_data()
battery6.tampilkan_data()
print ("total battery : ", battery.jumlah_battery)


