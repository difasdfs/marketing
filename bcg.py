namaFile = input("Nama File (CSV) : ")
namaFile += ".csv"

file = open(namaFile)
baris = file.readlines()
file.close()

"""PAKET!"""
# Paket Ayam Crispy
totalPenjualan_101100_or_101110 = 0
grossProfit_101100_or_101110 = 0

# Paket Ayam Crisbar
totalPenjualan_101111 = 0
grossProfit_101111 = 0

# Paket Ayam Matah
totalPenjualan_101112 = 0
grossProfit_101112 = 0

# Paket Ayam Mamah
totalPenjualan_101113 = 0
grossProfit_101113 = 0

# Paket Ayam Tomat
totalPenjualan_101114 = 0
grossProfit_101114 = 0

# Paket Ayam Keju
totalPenjualan_101115 = 0
grossProfit_101115 = 0

# Paket Ayam Manis
totalPenjualan_101116 = 0
grossProfit_101116 = 0

# Paket Ayam Goang
totalPenjualan_101117 = 0
grossProfit_101117 = 0

# Paket Crisbee Gravy
totalPenjualan_101120 = 0
grossProfit_101120 = 0

# Paket 4 Chiken Skin
totalPenjualan_102001 = 0
grossProfit_102001 = 0

# Paket Side Dish
totalPenjualan_102002 = 0
grossProfit_102002 = 0

# Raksasa Crisbar
totalPenjualan_102110 = 0
grossProfit_102110 = 0

# Raksasa Crispy
totalPenjualan_102111 = 0
grossProfit_102111 = 0

# Raksasa Manis
totalPenjualan_102112 = 0
grossProfit_102112 = 0

# Raksasa Keju
totalPenjualan_102113 = 0
grossProfit_102113 = 0

# 4 Ayam Crispy Original/Geprek Ala Carte
totalPenjualan_103100 = 0
grossProfit_103100 = 0

# 4 Ayam Crisbar Original/Geprek Ala Carte
totalPenjualan_103101 = 0
grossProfit_103101 = 0

# 3 Ayam Crispy + 3 Nasi + 3 Minum
totalPenjualan_103110 = 0
grossProfit_103110 = 0

# 3 Ayam Crisbar + 3 Nasi + 3 Minum
totalPenjualan_103111 = 0
grossProfit_103111 = 0

# Crispy + Minum + Gratis 2 Kulit
totalPenjualan_106110 = 0
grossProfit_106110 = 0

# Crisbar + Minum + Gratis 2 Kulit
totalPenjualan_106111 = 0
grossProfit_106111 = 0

# Crisbar + Minum + Gratis Tahu dan Tempe
totalPenjualan_106112 = 0
grossProfit_106112 = 0

# P.Crisbar + P.Keju + 2 Minum + Gratis 2 Tempe 4 Kulit
totalPenjualan_106113 = 0
grossProfit_106113 = 0

# LTO
totalPenjualan_109 = 0
grossProfit_109 = 0

"""SIDE DISH"""
# Nasi
totalPenjualan_7000000 = 0
grossProfit_7000000 = 0

# Tempe Crispy
totalPenjualan_7000001 = 0
grossProfit_7000001 = 0

# Tahu Crispy
totalPenjualan_7000002 = 0
grossProfit_7000002 = 0

# Terong Crispy
totalPenjualan_7000003 = 0
grossProfit_7000003 = 0

# Telur Sayur
totalPenjualan_7000004 = 0
grossProfit_7000004 = 0

# Chiken Skin
totalPenjualan_7000005 = 0
grossProfit_7000005 = 0

# Kerupuk
totalPenjualan_7000008 = 0
grossProfit_7000008 = 0

# Perkedel
totalPenjualan_7000009 = 0
grossProfit_7000009 = 0

# Kol Crispy
totalPenjualan_7000010 = 0
grossProfit_7000010 = 0

for isi in baris:
    kolom = isi.split(',')
    namaItem = kolom[0]
    sku = kolom[1]
    grossProfit = kolom[10][:-3]
    totalPenjualan = kolom[4][:-3]

    # Paket Ayam Crispy
    if (sku[:-2] == "101100") or (sku[:-2] == "101110"):
        #print(str(i) + ". " + namaItem + ", " + sku + ", " + totalPenjualan)
        totalPenjualan_101100_or_101110 += int(totalPenjualan)
        grossProfit_101100_or_101110 += int(grossProfit)

    # Paket Ayam Crisbar
    elif (sku[:-2] == "101111"):
        #print(str(i) + ". " + namaItem + ", " + sku + ", " + totalPenjualan)
        totalPenjualan_101111 += int(totalPenjualan)
        grossProfit_101111 += int(grossProfit)

    # Paket Ayam Matah
    elif (sku[:-2] == "101112"):
        totalPenjualan_101112 += int(totalPenjualan)
        grossProfit_101112 += int(grossProfit)

    # Paket Ayam Mamah
    elif (sku[:-2] == "101113"):
        totalPenjualan_101113 += int(totalPenjualan)
        grossProfit_101113 += int(grossProfit)

    # Paket Ayam Tomat
    elif (sku[:-2] == "101114"):
        totalPenjualan_101114 += int(totalPenjualan)
        grossProfit_101114 += int(grossProfit)

     # Paket Ayam Keju
    elif (sku[:-2] == "101115"):
        totalPenjualan_101115 += int(totalPenjualan)
        grossProfit_101115 += int(grossProfit)

    # Paket Ayam Manis
    elif (sku[:-2] == "101116"):
        totalPenjualan_101116 += int(totalPenjualan)
        grossProfit_101116 += int(grossProfit)

    # Paket Ayam Goang
    elif (sku[:-2] == "101117"):
        totalPenjualan_101117 += int(totalPenjualan)
        grossProfit_101117 += int(grossProfit)

    # Paket Crisbee Gravy
    elif (sku[:-2] == '101120'):
        totalPenjualan_101120 += int(totalPenjualan)
        grossProfit_101120 += int(grossProfit)

    # Paket 4 Chiken Skin
    elif (sku[:-2] == "102001"):
        totalPenjualan_102001 += int(totalPenjualan)
        grossProfit_102001 += int(grossProfit)

    # Paket Side Dish
    elif (sku[:-2] == "102002"):
        totalPenjualan_102002 += int(totalPenjualan)
        grossProfit_102002 += int(grossProfit)

    # Raksasa Crisbar
    elif (sku[:-2] == "102110"):
        totalPenjualan_102110 += int(totalPenjualan)
        grossProfit_102110 += int(grossProfit)

    # Raksasa Crispy
    elif (sku[:-2] == "102111"):
        totalPenjualan_102111 += int(totalPenjualan)
        grossProfit_102111 += int(grossProfit)

    # Raksasa Manis
    elif (sku[:-2] == "102112"):
        totalPenjualan_102112 += int(totalPenjualan)
        grossProfit_102112 += int(grossProfit)

    # Raksasa Keju
    elif (sku[:-2] == "102113"):
        totalPenjualan_102113 += int(totalPenjualan)
        grossProfit_102113 += int(grossProfit)

    # 4 Ayam Crispy Original/Geprek Ala Carte
    elif (sku[:-2] == "103100"):
        totalPenjualan_103100 += int(totalPenjualan)
        grossProfit_103100 += int(grossProfit)

    # 4 Ayam Crisbar Original/Geprek Ala Carte
    elif (sku[:-2] == "103101"):
        totalPenjualan_103101 += int(totalPenjualan)
        grossProfit_103101 += int(grossProfit)

    # 3 Ayam Crispy + 3 Nasi + 3 Minum
    elif (sku[:-2] == "103110"):
        totalPenjualan_103110 += int(totalPenjualan)
        grossProfit_103110 += int(grossProfit)

    # 3 Ayam Crisbar + 3 Nasi + 3 Minum
    elif (sku[:-2] == "103111"):
        totalPenjualan_103111 += int(totalPenjualan)
        grossProfit_103111 += int(grossProfit)

    # Crispy + Minum + Gratis 2 Kulit
    elif (sku[:-2] == "106110"):
        totalPenjualan_106110 += int(totalPenjualan)
        grossProfit_106110 += int(grossProfit)

    # Crisbar + Minum + Gratis 2 Kulit
    elif (sku[:-2] == "106111"):
        totalPenjualan_106111 += int(totalPenjualan)
        grossProfit_106111 += int(grossProfit)

    # Crisbar + Minum + Gratis Tahu dan Tempe
    elif (sku[:-2] == "106112"):
        totalPenjualan_106112 += int(totalPenjualan)
        grossProfit_106112 += int(grossProfit)

    # P.Crisbar + P.Keju + 2 Minum + Gratis 2 Tempe 4 Kulit
    elif (sku[:-2] == "106113"):
        totalPenjualan_106113 += int(totalPenjualan)
        grossProfit_106113 += int(grossProfit)

    # LOT
    elif (sku[:3] == "109"):
        totalPenjualan_109 += int(totalPenjualan)
        grossProfit_109 += int(grossProfit)

    # Nasi
    elif (sku[:-1] == "7000000"):
        totalPenjualan_7000000 += int(totalPenjualan)
        grossProfit_7000000 += int(grossProfit)

    # Tempe Crispy
    elif (sku[:-1] == "7000001"):
        totalPenjualan_7000001 += int(totalPenjualan)
        grossProfit_7000001 += int(grossProfit)

    # Tahu Crispy
    elif (sku[:-1] == "7000002"):
        totalPenjualan_7000002 += int(totalPenjualan)
        grossProfit_7000002 += int(grossProfit)

    # Terong Crispy
    elif (sku[:-1] == "7000003"):
        totalPenjualan_7000003 += int(totalPenjualan)
        grossProfit_7000003 += int(grossProfit)

    # Telur Sayur
    elif (sku[:-1] == "7000004"):
        totalPenjualan_7000004 += int(totalPenjualan)
        grossProfit_7000004 += int(grossProfit)

    # Chiken Skin
    elif (sku[:-1] == "7000005"):
        totalPenjualan_7000005 += int(totalPenjualan)
        grossProfit_7000005 += int(grossProfit)

    # Kerupuk
    elif (sku[:-1] == "7000008"):
        totalPenjualan_7000008 += int(totalPenjualan)
        grossProfit_7000008 += int(grossProfit)

    # Perkedel
    elif (sku[:-1] == "7000009"):
        totalPenjualan_7000009 += int(totalPenjualan)
        grossProfit_7000009 += int(grossProfit)

    # 3 Kol Crispy
    elif (sku[:-1] == "7000010"):
        totalPenjualan_7000010 += int(totalPenjualan)
        grossProfit_7000010 += int(grossProfit)


# Minuman
# Variabel
totalPenjualan_lemontea = 0
totalPenjualan_milo = 0
totalPenjualan_orange = 0
totalPenjualan_esteh = 0

for isi in baris[7:]:
    kolom = isi.split(',')
    namaItem = kolom[0]
    sku = kolom[1]
    barangTerjual = kolom[3][:-4]

    syarat = (sku[0] not in ['9', '7']) and (
        sku[-2] != '0') and (sku[:4] != '1091')

    if syarat:
        # Lemonade/Lemontea
        if sku[-2] == '5' or sku[-2] == '6':
            totalPenjualan_lemontea += int(barangTerjual)

        # Milo
        elif sku[-2] == '7':
            totalPenjualan_milo += int(barangTerjual)

        # Orange
        elif sku[-2] == '8':
            totalPenjualan_orange += int(barangTerjual)

        # Es Teh
        elif sku[-2] == '9':
            totalPenjualan_esteh += int(barangTerjual)

varMinuman = [totalPenjualan_lemontea, totalPenjualan_milo,
              totalPenjualan_orange, totalPenjualan_esteh]
namaMinuman = ('Lemontea/Lemonade', 'Milo', 'Orange', 'Es Teh')


# DESSERT

# Sigulmer
totalPenjualan_sigulmer = 0
grossProfit_sigulmer = 0

# Pudding Milo Dino
totalPenjualan_pudding_milo_dino = 0
grossProfit_pudding_milo_dino = 0

for isi in baris[1:]:
    isi = isi.split(',')
    sku = isi[1]
    totalPenjualan = int(isi[4][:-3])
    grossProfit = int(isi[10][:-3])

    # Sigulmer
    if (sku[:-1] == '5000001'):
        totalPenjualan_sigulmer += totalPenjualan
        grossProfit_sigulmer += grossProfit

    # Pudding Milo Dino
    elif (sku[:-1] == "5000002"):
        totalPenjualan_pudding_milo_dino += totalPenjualan
        grossProfit_pudding_milo_dino += grossProfit


# buat bcg minuman
namaFilePaket = "minuman - " + namaFile
tulis_file = open(namaFilePaket, "w")
tulis_file.write("nama minuman,barang terjual\n")

for i in range(len(namaMinuman)):
    tulis_file.write(namaMinuman[i] + "," + str(varMinuman[i]) + "\n")

tulis_file.close()

# Tuple Paket

totalPenjualanPaket = (
    totalPenjualan_101100_or_101110,
    totalPenjualan_101111,
    totalPenjualan_101112,
    totalPenjualan_101113,
    totalPenjualan_101114,
    totalPenjualan_101115,
    totalPenjualan_101116,
    totalPenjualan_101117,
    totalPenjualan_101120,
    totalPenjualan_102001,
    totalPenjualan_102002,
    totalPenjualan_102110,
    totalPenjualan_102111,
    totalPenjualan_102112,
    totalPenjualan_102113,
    totalPenjualan_103100,
    totalPenjualan_103101,
    totalPenjualan_103110,
    totalPenjualan_103111,
    totalPenjualan_106110,
    totalPenjualan_106111,
    totalPenjualan_106112,
    totalPenjualan_106113,
    totalPenjualan_109
)

jumlah_totalPenjualanPaket = sum(totalPenjualanPaket)

totalGrossProfitPaket = (
    grossProfit_101100_or_101110,
    grossProfit_101111,
    grossProfit_101112,
    grossProfit_101113,
    grossProfit_101114,
    grossProfit_101115,
    grossProfit_101116,
    grossProfit_101117,
    grossProfit_101120,
    grossProfit_102001,
    grossProfit_102002,
    grossProfit_102110,
    grossProfit_102111,
    grossProfit_102112,
    grossProfit_102113,
    grossProfit_103100,
    grossProfit_103101,
    grossProfit_103110,
    grossProfit_103111,
    grossProfit_106110,
    grossProfit_106111,
    grossProfit_106112,
    grossProfit_106113,
    grossProfit_109
)

namaPaket = (
    "Paket Ayam Crispy",
    "Paket Ayam Crisbar",
    "Paket Ayam Matah",
    "Paket Ayam Mamah",
    "Paket Ayam Tomat",
    "Paket Ayam Keju",
    "Paket Ayam Manis",
    "Paket Ayam Goang",
    "Paket Crisbee Gravy",  
    "Paket 4 Chiken Skin",
    "Paket Side Dish",
    "Raksasa Crisbar",
    "Raksasa Crispy",
    "Raksasa Manis",
    "Raksasa Keju",
    "4 Ayam Crispy Original/Geprek Ala Carte",
    "4 Ayam Crisbar Original/Geprek Ala Carte",
    "3 Ayam Crispy + 3 Nasi + 3 Minum",
    "3 Ayam Crisbar + 3 Nasi + 3 Minum",
    "Crispy + Minum + Gratis 2 Kulit",
    "Crisbar + Minum + Gratis 2 Kulit",
    "Crisbar + Minum + Gratis Tahu dan Tempe",
    "P.Crisbar + P.Keju + 2 Minum + Gratis 2 Tempe 4 Kulit",
    "LTO"
)

persenPenjualanPaket = []
for isi in totalPenjualanPaket:
    persenPenjualanPaket.append(isi/jumlah_totalPenjualanPaket)

# Tuple Side Dish
totalPenjualanSideDish = (
    totalPenjualan_7000000,
    totalPenjualan_7000001,
    totalPenjualan_7000002,
    totalPenjualan_7000003,
    totalPenjualan_7000004,
    totalPenjualan_7000005,
    totalPenjualan_7000008,
    totalPenjualan_7000009,
    totalPenjualan_7000010
)

jumlah_totalPenjualanSideDish = sum(totalPenjualanSideDish)

totalGrossProfitSideDish = (
    grossProfit_7000000,
    grossProfit_7000001,
    grossProfit_7000002,
    grossProfit_7000003,
    grossProfit_7000004,
    grossProfit_7000005,
    grossProfit_7000008,
    grossProfit_7000009,
    grossProfit_7000010
)

namaSideDish = (
    "Nasi",
    "Tempe Crispy",
    "Tahu Crispy",
    "Terong Crispy",
    "Telur Sayur",
    "Chiken Skin",
    "Kerupuk",
    "Perkedel",
    "Kol Crispy"
)

persenPenjualanSideDish = []
for isi in totalPenjualanSideDish:
    persenPenjualanSideDish.append(isi/jumlah_totalPenjualanSideDish)

# buat bcg paket
namaFilePaket = "Paket - " + namaFile
tulis_file = open(namaFilePaket, "w")
tulis_file.write("nama paket;gross profit;total penjualan;persen penjualan\n")

for i in range(len(totalPenjualanPaket)):
    persenan = str(persenPenjualanPaket[i]*100).split('.')
    persenan = persenan[0] + ',' + persenan[1][:2]
    tulis_file.write(namaPaket[i] + ";" + str(totalGrossProfitPaket[i]) +
                     ";" + str(totalPenjualanPaket[i]) + ";" + persenan + "\n")

tulis_file.close()

# buat bcg side dish
namaFileSideDish = "Side Dish - " + namaFile
tulis_file = open(namaFileSideDish, "w")
tulis_file.write(
    "nama side dish;gross profit;total penjualan;persen penjualan\n")

for i in range(len(totalPenjualanSideDish)):
    persenan = str(persenPenjualanSideDish[i]*100).split('.')
    persenan = persenan[0] + ',' + persenan[1][:2]
    tulis_file.write(namaSideDish[i] + ";" + str(totalGrossProfitSideDish[i]) +
                     ";" + str(totalPenjualanSideDish[i]) + ";" + persenan + "\n")

tulis_file.close()

# Buat BCG Dessert

totalPenjualanDessert = (
	totalPenjualan_sigulmer,
	totalPenjualan_pudding_milo_dino
)

jumlah_totalPenjualanDessert = sum(totalPenjualanDessert)

totalGrossProfitDessert = (
	grossProfit_sigulmer,
	grossProfit_pudding_milo_dino
)

namaDessert = (
	"Sigulmer",
	"Pudding Milo Dino",
)

persenPejualanDessert = []
for isi in totalPenjualanDessert:
	persenPejualanDessert.append(isi/jumlah_totalPenjualanDessert)

namaFileDessert = "Dessert - " + namaFile
tulis_file = open(namaFileDessert, 'w')
tulis_file.write("Nama Dessert; Gross Profit; Total Penjualan; Persen Penjualan\n")

for i in range(len(totalPenjualanDessert)):
    persenan = str(persenPejualanDessert[i]*100).split('.')
    persenan = persenan[0] + ',' + persenan[1][:2]
    tulis_file.write(namaDessert[i] + ";" + str(totalGrossProfitDessert[i]) + ";" + str(totalPenjualanDessert[i]) + ";" + persenan + "\n")

tulis_file.close()