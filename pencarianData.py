# Program ini digunakan untuk mencari data dalam daftar


# Fungsi cari_data menerima daftar dan data yang ingin dicari sebagai input
def cari_data(daftar, data):
    # Tambahkan kode di sini
    for nama in daftar:
        if nama == data:
            return print(nama)
    print("Data tidak ditemukan")


# Gunakan fungsi cari_data untuk mencari data dalam daftar berikut
data_mahasiswa = ["Alice", "Bob", "Charlie", "David"]
data_yang_dicari = "Bob"
# Panggil fungsi cari_data untuk mencari data_yang_dicari dalam data_mahasiswa
cari_data(data_mahasiswa, data_yang_dicari)
