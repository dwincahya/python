# Program ini digunakan untuk menghitung Indeks Massa Tubuh (BMI)
import math


# Fungsi hitung_bmi menerima berat (dalam kilogram) dan tinggi (dalam meter) sebagai input
def hitung_bmi(berat, tinggi):
    # Tambahkan kode di sini
    bmi = berat / math.sqrt(tinggi)
    if bmi < 18.5:
        return print("Kekurangan berat badan")
    elif bmi >= 18.5 and bmi <= 24.9:
        return print("Normal")
    elif bmi >= 25 and bmi <= 29.9:
        return print("Kelebihan berat badan")
    else:
        return print("Kegemukan (Obesitas)")


# Gunakan fungsi hitung_bmi untuk menghitung BMI dari berat dan tinggi berikut
berat = 70
tinggi = 1.75
# Panggil fungsi hitung_bmi untuk menghitung BMI
hitung_bmi(berat, tinggi)
