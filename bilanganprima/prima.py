def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    print("Program Pencari Bilangan Prima")
    
    start = int(input("Masukkan angka awal: "))
    end = int(input("Masukkan angka akhir: "))
    
    primes = find_primes(start, end)
    
    if primes:
        print(f"Bilangan prima antara {start} dan {end}:")
        print(primes)
    else:
        print(f"Tidak ada bilangan prima antara {start} dan {end}.")

if __name__ == "__main__":
    main()
