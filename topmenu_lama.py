namafile = input('Nama File (CSV) : ')
namafile += '.csv'
file = open(namafile)
isi = file.readlines()
file.close()

# kategori = GO FOOD, GRABFOOD, DINE IN, TAKE AWAY
gofood = []
grabfood = []
dinein = []
takeaway = []

for row in isi[1:]:
    if "GO FOOD" in row:
        gofood.append(row)
    elif "GRABFOOD" in row:
        grabfood.append(row)
    elif "DINE IN" in row:
        dinein.append(row)
    elif "TAKE AWAY" in row:
        takeaway.append(row)


def pisahin(kategori):
    # Item name, Barang yang terjual, Total pendapatan
    # ALA CARTE
    "Ayam Crispy"
    barangYangTerjual_1001000 = totalPendapatan_1001000 = 0

    "Ayam Crispy Geprek"
    barangYangTerjual_1001100 = totalPendapatan_1001100 = 0

    "Ayam Crisbar"
    barangYangTerjual_1001110 = totalPendapatan_1001110 = 0

    "Ayam Matah"
    barangYangTerjual_1001120 = totalPendapatan_1001120 = 0

    "Ayam Mamah"
    barangYangTerjual_1001130 = totalPendapatan_1001130 = 0

    "Ayam Tomat"
    barangYangTerjual_1001140 = totalPendapatan_1001140 = 0

    "Ayam Keju"
    barangYangTerjual_1001150 = totalPendapatan_1001150 = 0

    "Ayam Manis"
    barangYangTerjual_1001160 = totalPendapatan_1001160 = 0

    "Ayam Goang"
    barangYangTerjual_1001170 = totalPendapatan_1001170 = 0

    # PAKET
    "Paket Ayam Crispy"
    barangYangTerjual_paketAyamCrispy = totalPendapatan_paketAyamCrispy = 0

    "Paket Ayam Crisbar"
    barangYangTerjual_101111 = totalPendapatan_101111 = 0

    "Paket Ayam Matah"
    barangYangTerjual_101112 = totalPendapatan_101112 = 0

    "Paket Ayam Mamah"
    barangYangTerjual_101113 = totalPendapatan_101113 = 0

    "Paket Ayam Tomat"
    barangYangTerjual_101114 = totalPendapatan_101114 = 0

    "Paket Ayam Keju"
    barangYangTerjual_101115 = totalPendapatan_101115 = 0

    "Paket Ayam Manis"
    barangYangTerjual_101116 = totalPendapatan_101116 = 0

    "Paket Ayam Goang"
    barangYangTerjual_101117 = totalPendapatan_101117 = 0

    "Paket 4 Chiken Skin + Minum"
    barangYangTerjual_102001 = totalPendapatan_102001 = 0

    "Paket Side Dish"
    barangYangTerjual_102002 = totalPendapatan_102002 = 0

    "Raksasa Crisbar"
    barangYangTerjual_102110 = totalPendapatan_102110 = 0

    "Raksasa Crispy"
    barangYangTerjual_102111 = totalPendapatan_102111 = 0

    "Raksasa Manis"
    barangYangTerjual_102112 = totalPendapatan_102112 = 0

    "Raksasa Keju"
    barangYangTerjual_102113 = totalPendapatan_102113 = 0

    "3 Ayam Crispy + 3 Nasi + 3 Es Teh"
    barangYangTerjual_102118 = totalPendapatan_102118 = 0

    "4 Ayam Crispy Original/Geprek Ala Carte"
    barangYangTerjual_1031000 = totalPendapatan_1031000 = 0

    "4 Ayam Crisbar Original/Geprek Ala Carte"
    barangYangTerjual_1031010 = totalPendapatan_1031010 = 0

    "2 Ayam Crisbar + 3 Ayam Sambal Mix"
    barangYangTerjual_1031020 = totalPendapatan_1031020 = 0

    "3 Ayam Crispy + 3 Nasi + 3 Es Teh"
    barangYangTerjual_1031109 = totalPendapatan_1031109 = 0

    "3 Ayam Crisbar + 3 Nasi + Minum"
    barangYangTerjual_103111 = totalPendapatan_103111 = 0

    "Crispy + Minum + Gratis 2 Kulit"
    barangYangTerjual_106110 = totalPendapatan_106110 = 0

    "Crisbar + Minum + Gratis 2 Kulit"
    barangYangTerjual_106111 = totalPendapatan_106111 = 0

    "Crisbar + Minum + Gratis Tahu dan Tempe"
    barangYangTerjual_106112 = totalPendapatan_106112 = 0

    "P.Crisbar + P.Keju + 2 Minum + Gratis 2 Tempe 4 Kulit"
    barangYangTerjual_106113 = totalPendapatan_106113 = 0

    "Crisbar + Minum + 1 Porsi Kol Crispy"
    barangYangTerjual_106114 = totalPendapatan_106114 = 0

    "LTO"
    barangYangTerjual_109 = totalPendapatan_109 = 0

    # SIDE DISH
    "Nasi"
    barangYangTerjual_7000000 = totalPendapatan_7000000 = 0

    "Tempe Crispy"
    barangYangTerjual_7000001 = totalPendapatan_7000001 = 0

    "Tahu Crispy"
    barangYangTerjual_7000002 = totalPendapatan_7000002 = 0

    "Terong Crispy"
    barangYangTerjual_7000003 = totalPendapatan_7000003 = 0

    "Telur Sayur"
    barangYangTerjual_7000004 = totalPendapatan_7000004 = 0

    "Chiken Skin"
    barangYangTerjual_7000005 = totalPendapatan_7000005 = 0

    "Kerupuk"
    barangYangTerjual_7000008 = totalPendapatan_7000008 = 0

    "Pudding Milo Dino"
    barangYangTerjual_7000009 = totalPendapatan_7000009 = 0

    "3 Kol Crispy"
    barangYangTerjual_7000010 = totalPendapatan_7000010 = 0

    # MINUMAN
    "Lemonade"
    barangYangTerjual_8000005 = totalPendapatan_8000005 = 0

    "Lemon Tea"
    barangYangTerjual_8000006 = totalPendapatan_8000006 = 0

    "Milo"
    barangYangTerjual_8000007 = totalPendapatan_8000007 = 0

    "Orange"
    barangYangTerjual_8000008 = totalPendapatan_8000008 = 0

    "Es Teh Manis"
    barangYangTerjual_8000009 = totalPendapatan_8000009 = 0

    for baris in kategori:

        # Selesai variabel
        baris = baris.split(',')
        sku = baris[1]
        barangYangTerjual = baris[3][:-4]
        totalPendapatan = baris[-5][:-3]

        if "1001000" in sku:
            barangYangTerjual_1001000 += int(barangYangTerjual)
            totalPendapatan_1001000 += int(totalPendapatan)

        elif "1001100" in sku:
            barangYangTerjual_1001100 += int(barangYangTerjual)
            totalPendapatan_1001100 += int(totalPendapatan)

        elif "1001110" in sku:
            barangYangTerjual_1001110 += int(barangYangTerjual)
            totalPendapatan_1001110 += int(totalPendapatan)

        elif "1001120" in sku:
            barangYangTerjual_1001120 += int(barangYangTerjual)
            totalPendapatan_1001120 += int(totalPendapatan)

        elif "1001130" in sku:
            barangYangTerjual_1001130 += int(barangYangTerjual)
            totalPendapatan_1001130 += int(totalPendapatan)

        elif "1001140" in sku:
            barangYangTerjual_1001140 += int(barangYangTerjual)
            totalPendapatan_1001140 += int(totalPendapatan)

        elif "1001150" in sku:
            barangYangTerjual_1001150 += int(barangYangTerjual)
            totalPendapatan_1001150 += int(totalPendapatan)

        elif "1001160" in sku:
            barangYangTerjual_1001160 += int(barangYangTerjual)
            totalPendapatan_1001160 += int(totalPendapatan)

        elif "1001170" in sku:
            barangYangTerjual_1001170 += int(barangYangTerjual)
            totalPendapatan_1001170 += int(totalPendapatan)

        elif ("101100" in sku) or ("101110" in sku):
            barangYangTerjual_paketAyamCrispy += int(barangYangTerjual)
            totalPendapatan_paketAyamCrispy += int(totalPendapatan)

        elif "101111" in sku:
            barangYangTerjual_101111 += int(barangYangTerjual)
            totalPendapatan_101111 += int(totalPendapatan)

        elif "101112" in sku:
            barangYangTerjual_101112 += int(barangYangTerjual)
            totalPendapatan_101112 += int(totalPendapatan)

        elif "101113" in sku:
            barangYangTerjual_101113 += int(barangYangTerjual)
            totalPendapatan_101113 += int(totalPendapatan)

        elif "101114" in sku:
            barangYangTerjual_101114 += int(barangYangTerjual)
            totalPendapatan_101114 += int(totalPendapatan)

        elif "101115" in sku:
            barangYangTerjual_101115 += int(barangYangTerjual)
            totalPendapatan_101115 += int(totalPendapatan)

        elif "101116" in sku:
            barangYangTerjual_101116 += int(barangYangTerjual)
            totalPendapatan_101116 += int(totalPendapatan)

        elif "101117" in sku:
            barangYangTerjual_101117 += int(barangYangTerjual)
            totalPendapatan_101117 += int(totalPendapatan)

        elif "102001" in sku:
            barangYangTerjual_102001 += int(barangYangTerjual)
            totalPendapatan_102001 += int(totalPendapatan)

        elif "102002" in sku:
            barangYangTerjual_102002 += int(barangYangTerjual)
            totalPendapatan_102002 += int(totalPendapatan)

        elif "102110" in sku:
            barangYangTerjual_102110 += int(barangYangTerjual)
            totalPendapatan_102110 += int(totalPendapatan)

        elif "102111" in sku:
            barangYangTerjual_102111 += int(barangYangTerjual)
            totalPendapatan_102111 += int(totalPendapatan)

        elif "102112" in sku:
            barangYangTerjual_102112 += int(barangYangTerjual)
            totalPendapatan_102112 += int(totalPendapatan)

        elif "102113" in sku:
            barangYangTerjual_102113 += int(barangYangTerjual)
            totalPendapatan_102113 += int(totalPendapatan)

        elif "102118" in sku:
            barangYangTerjual_102118 += int(barangYangTerjual)
            totalPendapatan_102118 += int(totalPendapatan)

        elif "1031000" in sku:
            barangYangTerjual_1031000 += int(barangYangTerjual)
            totalPendapatan_1031000 += int(totalPendapatan)

        elif "1031010" in sku:
            barangYangTerjual_1031010 += int(barangYangTerjual)
            totalPendapatan_1031010 += int(totalPendapatan)

        elif "1031020" in sku:
            barangYangTerjual_1031020 += int(barangYangTerjual)
            totalPendapatan_1031020 += int(totalPendapatan)

        elif "1031109" in sku:
            barangYangTerjual_1031109 += int(barangYangTerjual)
            totalPendapatan_1031109 += int(totalPendapatan)

        elif "103111" in sku:
            barangYangTerjual_103111 += int(barangYangTerjual)
            totalPendapatan_103111 += int(totalPendapatan)

        elif "106110" in sku:
            barangYangTerjual_106110 += int(barangYangTerjual)
            totalPendapatan_106110 += int(totalPendapatan)

        elif "106111" in sku:
            barangYangTerjual_106111 += int(barangYangTerjual)
            totalPendapatan_106111 += int(totalPendapatan)

        elif "106112" in sku:
            barangYangTerjual_106112 += int(barangYangTerjual)
            totalPendapatan_106112 += int(totalPendapatan)

        elif "106113" in sku:
            barangYangTerjual_106113 += int(barangYangTerjual)
            totalPendapatan_106113 += int(totalPendapatan)

        elif "106114" in sku:
            barangYangTerjual_106114 += int(barangYangTerjual)
            totalPendapatan_106114 += int(totalPendapatan)

        elif "109" in sku:
            barangYangTerjual_109 += int(barangYangTerjual)
            totalPendapatan_109 += int(totalPendapatan)

        elif "7000000" in sku:
            barangYangTerjual_7000000 += int(barangYangTerjual)
            totalPendapatan_7000000 += int(totalPendapatan)

        elif "7000001" in sku:
            barangYangTerjual_7000001 += int(barangYangTerjual)
            totalPendapatan_7000001 += int(totalPendapatan)

        elif "7000002" in sku:
            barangYangTerjual_7000002 += int(barangYangTerjual)
            totalPendapatan_7000002 += int(totalPendapatan)

        elif "7000003" in sku:
            barangYangTerjual_7000003 += int(barangYangTerjual)
            totalPendapatan_7000003 += int(totalPendapatan)

        elif "7000004" in sku:
            barangYangTerjual_7000004 += int(barangYangTerjual)
            totalPendapatan_7000004 += int(totalPendapatan)

        elif "7000005" in sku:
            barangYangTerjual_7000005 += int(barangYangTerjual)
            totalPendapatan_7000005 += int(totalPendapatan)

        elif "7000008" in sku:
            barangYangTerjual_7000008 += int(barangYangTerjual)
            totalPendapatan_7000008 += int(totalPendapatan)

        elif "7000009" in sku:
            barangYangTerjual_7000009 += int(barangYangTerjual)
            totalPendapatan_7000009 += int(totalPendapatan)

        elif "7000010" in sku:
            barangYangTerjual_7000010 += int(barangYangTerjual)
            totalPendapatan_7000010 += int(totalPendapatan)

        elif "8000005" in sku:
            barangYangTerjual_8000005 += int(barangYangTerjual)
            totalPendapatan_8000005 += int(totalPendapatan)

        elif "8000006" in sku:
            barangYangTerjual_8000006 += int(barangYangTerjual)
            totalPendapatan_8000006 += int(totalPendapatan)

        elif "8000007" in sku:
            barangYangTerjual_8000007 += int(barangYangTerjual)
            totalPendapatan_8000007 += int(totalPendapatan)

        elif "8000008" in sku:
            barangYangTerjual_8000008 += int(barangYangTerjual)
            totalPendapatan_8000008 += int(totalPendapatan)

        elif "8000009" in sku:
            barangYangTerjual_8000009 += int(barangYangTerjual)
            totalPendapatan_8000009 += int(totalPendapatan)

    nama_alacarte = [
        ("Ayam Crispy", barangYangTerjual_1001000, totalPendapatan_1001000),
        ("Ayam Crispy Geprek", barangYangTerjual_1001100, totalPendapatan_1001100),
        ("Ayam Crisbar", barangYangTerjual_1001110, totalPendapatan_1001110),
        ("Ayam Matah", barangYangTerjual_1001120, totalPendapatan_1001120),
        ("Ayam Mamah", barangYangTerjual_1001130, totalPendapatan_1001130),
        ("Ayam Tomat", barangYangTerjual_1001140, totalPendapatan_1001140),
        ("Ayam Keju", barangYangTerjual_1001150, totalPendapatan_1001150),
        ("Ayam Manis", barangYangTerjual_1001160, totalPendapatan_1001160),
        ("Ayam Goang", barangYangTerjual_1001170, totalPendapatan_1001170),
    ]

    nama_paket = [
        ("Paket Ayam Crispy", barangYangTerjual_paketAyamCrispy,
         totalPendapatan_paketAyamCrispy),
        ("Paket Ayam Crisbar", barangYangTerjual_101111, totalPendapatan_101111),
        ("Paket Ayam Matah", barangYangTerjual_101112, totalPendapatan_101112),
        ("Paket Ayam Mamah", barangYangTerjual_101113, totalPendapatan_101113),
        ("Paket Ayam Tomat", barangYangTerjual_101114, totalPendapatan_101114),
        ("Paket Ayam Keju", barangYangTerjual_101115, totalPendapatan_101115),
        ("Paket Ayam Manis", barangYangTerjual_101116, totalPendapatan_101116),
        ("Paket Ayam Goang", barangYangTerjual_101117, totalPendapatan_101117),
        ("Paket 4 Chiken Skin + Minum",
         barangYangTerjual_102001, totalPendapatan_102001),
        ("Paket Side Dish", barangYangTerjual_102002, totalPendapatan_102002),
        ("Raksasa Crisbar", barangYangTerjual_102110, totalPendapatan_102110),
        ("Raksasa Crispy", barangYangTerjual_102111, totalPendapatan_102111),
        ("Raksasa Manis", barangYangTerjual_102112, totalPendapatan_102112),
        ("Raksasa Keju", barangYangTerjual_102113, totalPendapatan_102113),
        ("3 Ayam Crispy + 3 Nasi + 3 Es Teh",
         barangYangTerjual_102118, totalPendapatan_102118),
        ("4 Ayam Crispy Original/Geprek Ala Carte",
         barangYangTerjual_1031000, totalPendapatan_1031000),
        ("4 Ayam Crisbar Original/Geprek Ala Carte",
         barangYangTerjual_1031010, totalPendapatan_1031010),
        ("2 Ayam Crisbar + 3 Ayam Sambal Mix",
         barangYangTerjual_1031020, totalPendapatan_1031020),
        ("3 Ayam Crispy + 3 Nasi + 3 Es Teh",
         barangYangTerjual_1031109, totalPendapatan_1031109),
        ("3 Ayam Crisbar + 3 Nasi + Minum",
         barangYangTerjual_103111, totalPendapatan_103111),
        ("Crispy + Minum + Gratis 2 Kulit",
         barangYangTerjual_106110, totalPendapatan_106110),
        ("Crisbar + Minum + Gratis 2 Kulit",
         barangYangTerjual_106111, totalPendapatan_106111),
        ("Crisbar + Minum + Gratis Tahu dan Tempe",
         barangYangTerjual_106112, totalPendapatan_106112),
        ("P.Crisbar + P.Keju + 2 Minum + Gratis 2 Tempe 4 Kulit",
         barangYangTerjual_106113, totalPendapatan_106113),
        ("Crisbar + Minum + 1 Porsi Kol Crispy",
         barangYangTerjual_106114, totalPendapatan_106114),
        ("LTO", barangYangTerjual_109, totalPendapatan_109)
    ]

    nama_sidedish = [
        ("Nasi", barangYangTerjual_7000000, totalPendapatan_7000000),
        ("Tempe Crispy", barangYangTerjual_7000001, totalPendapatan_7000001),
        ("Tahu Crispy", barangYangTerjual_7000002, totalPendapatan_7000002),
        ("Terong Crispy", barangYangTerjual_7000003, totalPendapatan_7000003),
        ("Telur Sayur", barangYangTerjual_7000004, totalPendapatan_7000004),
        ("Chiken Skin", barangYangTerjual_7000005, totalPendapatan_7000005),
        ("Kerupuk", barangYangTerjual_7000008, totalPendapatan_7000008),
        ("Pudding Milo Dino", barangYangTerjual_7000009, totalPendapatan_7000009),
        ("3 Kol Crispy", barangYangTerjual_7000010, totalPendapatan_7000010)
    ]

    nama_minum = [
        ("Lemonade", barangYangTerjual_8000005, totalPendapatan_8000005),
        ("Lemon Tea", barangYangTerjual_8000006, totalPendapatan_8000006),
        ("Milo", barangYangTerjual_8000007, totalPendapatan_8000007),
        ("Orange", barangYangTerjual_8000008, totalPendapatan_8000008),
        ("Es Teh Manis", barangYangTerjual_8000009, totalPendapatan_8000009),
    ]
    return nama_alacarte, nama_paket, nama_sidedish, nama_minum


alacarte_gofood, paket_gofood, sidedish_gofood, minuman_gofood = pisahin(
    gofood)
alacarte_grabfood, paket_grabfood, sidedish_grabfood, minuman_grabfood = pisahin(
    grabfood)
alacarte_dinein, paket_dinein, sidedish_dinein, minuman_dinein = pisahin(
    dinein)
alacarte_takeaway, paket_takeaway, sidedish_takeaway, minuman_takeaway = pisahin(
    takeaway)

header = 'Item Name, Jenis, Barang yang terjual, Total pendapatan\n'
jenis = ("Ala Carte", "Paket", "Side Dish", "Minuman")

# GO FOOD
file = open('ala carte - gofood.csv', 'w')
file.write(header)
for row in alacarte_gofood:
    file.write(row[0] + ',' + jenis[0] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in paket_gofood:
    file.write(row[0] + ',' + jenis[1] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in sidedish_gofood:
    file.write(row[0] + ',' + jenis[2] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in minuman_gofood:
    file.write(row[0] + ',' + jenis[3] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
file.close()

# GRABFOOD
file = open('ala carte - grabfood.csv', 'w')
file.write(header)
for row in alacarte_grabfood:
    file.write(row[0] + ',' + jenis[0] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in paket_grabfood:
    file.write(row[0] + ',' + jenis[1] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in sidedish_grabfood:
    file.write(row[0] + ',' + jenis[2] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in minuman_grabfood:
    file.write(row[0] + ',' + jenis[3] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
file.close()

# DINE IN
file = open('ala carte - dinein.csv', 'w')
file.write(header)
for row in alacarte_dinein:
    file.write(row[0] + ',' + jenis[0] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in paket_dinein:
    file.write(row[0] + ',' + jenis[1] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in sidedish_dinein:
    file.write(row[0] + ',' + jenis[2] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in minuman_dinein:
    file.write(row[0] + ',' + jenis[3] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
file.close()

# TAKE AWAY
file = open('ala carte - takeaway.csv', 'w')
file.write(header)
for row in alacarte_takeaway:
    file.write(row[0] + ',' + jenis[0] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in paket_takeaway:
    file.write(row[0] + ',' + jenis[1] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in sidedish_takeaway:
    file.write(row[0] + ',' + jenis[2] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
for row in minuman_takeaway:
    file.write(row[0] + ',' + jenis[3] + ',' +
               str(row[1]) + ',' + str(row[2]) + '\n')
file.close()
