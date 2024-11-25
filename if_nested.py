
nilai = float(input("Masukkan nilai ujian: "))
if nilai >= 60:
    print("Anda lulus!")
    if nilai >= 80:
        print("Dan Anda mendapatkan nilai A")
    elif nilai >= 70:
        print("Dan Anda mendapatkan nilai B")
    else:
        print("Dan Anda mendapatkan nilai C")
else:
    print("Anda tidak lulus. Mohon coba lagi.")