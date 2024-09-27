import math

def main():
    try:
        angka = float(input("Masukkan Angka: "))

        # Menghitung akar kuadrat dari angka
        akar_kuadrat = math.sqrt(angka)
        print(f"Akar kuadrat dari {angka} adalah: {akar_kuadrat:.2f}")

        # Menghitung nilai sinus dari angka (dalam radian)
        nilai_sinus = math.sin(angka)
        print(f"Nilai Sinus dari {angka} adalah: {nilai_sinus:.2f}")

    except ValueError:
        print("Input yang Anda masukkan bukan Angka.")

if __name__ == "__main__":
    main()
    