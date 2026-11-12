daftar_nama = []
print("--- Input Nama Calon Anggota ---")
while True:
    nama = input("Masukkan nama calon anggota : ")
    if nama == "selesai":
        break
    daftar_nama.append(nama)

print("\n--- Evaluasi Validasi Nama ---")
for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print(f"Peringatan: Nama '{nama}' TIDAK VALID!")
    else:
        print(f"Nama '{nama}' valid.")

print("\n--- Pengecekan Penyusup ---")
penyusup = input("Masukkan nama yang dicurigai sebagai penyusup untuk dihapus: ")

if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print(f"Nama '{penyusup}' berhasil dihapus dari sistem.")
else:
    print(f"Nama '{penyusup}' tidak ditemukan dalam daftar pendaftaran. Program tetap berjalan aman.")

print("\nDaftar Pendaftaran Akhir:", daftar_nama)