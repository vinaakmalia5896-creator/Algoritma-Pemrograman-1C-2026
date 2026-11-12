asisten_awal = []
print("--- Input Asisten Awal ---")
while True:
    nama = input("Masukkan nama asisten: ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal_tuple = tuple(asisten_awal)

asisten_tambahan = input("\nMasukkan 1 nama asisten tambahan: ")
asisten_akhir_tuple = asisten_awal_tuple + (asisten_tambahan,)

hari_tugas = []
print("\n--- Input Hari Tugas ---")
while True:
    hari = input("Masukkan nama hari : ")
    if hari == "cukup":
        break
    hari_tugas.append(hari)

hari_tugas_tuple = tuple(hari_tugas)

print("\n--- Input Pengecualian Shift ---")
asisten_pengecualian = input("Masukkan nama asisten yang ada pengecualian: ")
hari_pengecualian = input("Masukkan hari pengecualian untuk asisten tersebut: ")

print("\n=== JADWAL SHIFT YANG BERHASIL DIBUAT ===")
for asisten in asisten_akhir_tuple:
    for hari in hari_tugas_tuple:
        if asisten == asisten_pengecualian and hari == hari_pengecualian:
            continue
        print(f"Asisten: {asisten} | Hari: {hari}")