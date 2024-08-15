def find_integers(start, end):
    integers = []
    for num in range(start, end + 1):
        if isinstance(num, int):
            integers.append(num)
    return integers

def main():
    print("Program Pencari Bilangan Bulat")
    
    start = int(input("Masukkan angka awal: "))
    end = int(input("Masukkan angka akhir: "))
    
    integers = find_integers(start, end)

    print(f"Bilangan bulat antara {start} dan {end}:")
    print(integers)

if __name__ == "__main__":
    main()
