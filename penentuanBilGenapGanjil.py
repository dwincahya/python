# Program ini digunakan untuk menentukan apakah suatu bilangan adalah genap atau ganjil


# Fungsi cek_genap_ganjil menerima sebuah bilangan sebagai input dan mengembalikan hasil
def cek_genap_ganjil(bilangan):
    # Tambahkan kode di sini
    if bilangan % 2 == 0:
        return print("Bilangan Genap")
    return print("Bilangan ganjil")


# Gunakan fungsi cek_genap_ganjil untuk menentukan apakah bilangan berikut adalah genap atau ganjil
bilangan = 10
# Panggil fungsi cek_genap_ganjil untuk menentukan apakah bilangan adalah genap atau ganjil
cek_genap_ganjil(bilangan)
