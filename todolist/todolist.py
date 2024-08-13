# Program To-Do List Sederhana

def tampilkan_todo(todo_list):
    print("\nDaftar To-Do:")
    if not todo_list:
        print("Tidak ada tugas dalam daftar.")
    else:
        for idx, tugas in enumerate(todo_list, start=1):
            print(f"{idx}. {tugas}")
    print("\n")

def tambah_todo(todo_list):
    tugas_baru = input("Masukkan tugas baru: ")
    todo_list.append(tugas_baru)
    print(f"Tugas '{tugas_baru}' telah ditambahkan.")

def hapus_todo(todo_list):
    tampilkan_todo(todo_list)
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor_tugas <= len(todo_list):
            tugas_hapus = todo_list.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_hapus}' telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def todo_list_program():
    todo_list = []

    while True:
        print("To-Do List")
        print("1. Tampilkan To-Do List")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tampilkan_todo(todo_list)
        elif pilihan == '2':
            tambah_todo(todo_list)
        elif pilihan == '3':
            hapus_todo(todo_list)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    todo_list_program()
