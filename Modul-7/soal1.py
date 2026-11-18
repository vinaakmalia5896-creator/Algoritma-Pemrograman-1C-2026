todo_list = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Statistik Tugas (Selesai & Belum)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo_list:
            print("Tugas sudah ada dalam daftar.")
        else:
            todo_list[tugas] = "Belum Selesai"
            print(f"Tugas '{tugas}' berhasil ditambahkan.")

    elif pilihan == "2":
        if not todo_list:
            print("Daftar tugas masih kosong.")
        else:
            print("\n--- Daftar Tugas ---")
            for tugas, status in todo_list.items():
                print(f"- {tugas} : [{status}]")

    elif pilihan == "3":
        tugas = input("Masukkan nama tugas yang selesai: ")
        try:
            if todo_list[tugas] == "Selesai":
                print("Tugas tersebut memang sudah selesai.")
            else:
                todo_list[tugas] = "Selesai"
                print(f"Tugas '{tugas}' ditandai Selesai.")
        except KeyError:
            print(f"Error: Tugas '{tugas}' tidak ditemukan!")

    elif pilihan == "4":
        tugas = input("Masukkan nama tugas yang ingin dihapus: ")
        try:
            del todo_list[tugas]
            print(f"Tugas '{tugas}' berhasil dihapus.")
        except KeyError:
            print(f"Error: Tugas '{tugas}' tidak ditemukan!")

    elif pilihan == "5":
        selesai = 0
        belum = 0
        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1
        print(f"\nJumlah Tugas Selesai : {selesai}")
        print(f"Jumlah Tugas Belum   : {belum}")

    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")