# Program ini digunakan untuk menentukan apakah sebuah kata adalah palindrom


# Fungsi cek_palindrom menerima sebuah kata sebagai input dan mengembalikan hasil
def cek_palindrom(kata):
    # Tambahkan kode di sini
    reverse = kata[::-1]
    if kata != reverse:
        return print("Tidak palindrom :\n", kata, "\n", reverse)
    print("Kata palindrom :", kata, reverse)


# Gunakan fungsi cek_palindrom untuk menentukan apakah kata berikut adalah palindrom
kata = "malam"
# Panggil fungsi cek_palindrom untuk menentukan apakah kata adalah palindrom
cek_palindrom(kata)
