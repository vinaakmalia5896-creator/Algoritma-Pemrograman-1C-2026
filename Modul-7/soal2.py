playlists = {}

while True:
    print("\n=== PENGELOLA PLAYLIST MUSIK ===")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist & Lagunya")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama_pl = input("Masukkan nama playlist baru: ")
        if nama_pl in playlists:
            print("Playlist sudah ada!")
        else:
            playlists[nama_pl] = {}
            print(f"Playlist '{nama_pl}' berhasil dibuat.")

    elif pilihan == "2":
        nama_pl = input("Masukkan nama playlist tujuan: ")
        try:
            target_pl = playlists[nama_pl]
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            target_pl[judul] = penyanyi
            print(f"Lagu '{judul}' - {penyanyi} ditambahkan ke '{nama_pl}'.")
        except KeyError:
            print(f"Error: Playlist '{nama_pl}' tidak ditemukan!")

    elif pilihan == "3":
        if not playlists:
            print("Belum ada playlist yang dibuat.")
        else:
            for nama_pl, lagu_dict in playlists.items():
                print(f"\nPlaylist: {nama_pl}")
                if not lagu_dict:
                    print("  (Kosong)")
                else:
                    for judul, penyanyi in lagu_dict.items():
                        print(f"  - {judul} ({penyanyi})")

    elif pilihan == "4":
        cari = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False
        for nama_pl, lagu_dict in playlists.items():
            if cari in lagu_dict:
                print(f"Ditemukan di playlist '{nama_pl}': {cari} - {lagu_dict[cari]}")
                ditemukan = True
        if not ditemukan:
            print(f"Lagu '{cari}' tidak ditemukan di playlist mana pun.")

    elif pilihan == "5":
        nama_pl = input("Masukkan nama playlist: ")
        try:
            target_pl = playlists[nama_pl]
            judul = input("Masukkan judul lagu yang akan dihapus: ")
            del target_pl[judul]
            print(f"Lagu '{judul}' berhasil dihapus dari '{nama_pl}'.")
        except KeyError:
            print("Error: Playlist atau judul lagu tidak ditemukan!")

    elif pilihan == "6":
        nama_pl = input("Masukkan nama playlist yang akan dihapus: ")
        try:
            del playlists[nama_pl]
            print(f"Playlist '{nama_pl}' berhasil dihapus.")
        except KeyError:
            print(f"Error: Playlist '{nama_pl}' tidak ditemukan!")

    elif pilihan == "7":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")