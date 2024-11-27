# Program ini digunakan untuk menghitung harga setelah diskon


# Fungsi hitung_diskon menerima harga awal dan persentase diskon sebagai input
def hitung_diskon(harga_awal, persentase_diskon):
    # Tambahkan kode di sini
    print(harga_awal - (harga_awal * persentase_diskon / 100))


# Gunakan fungsi hitung_diskon untuk menghitung harga setelah diskon
harga_awal = 100
persentase_diskon = 20
# Panggil fungsi hitung_diskon untuk menghitung harga setelah diskon
hitung_diskon(harga_awal, persentase_diskon)
