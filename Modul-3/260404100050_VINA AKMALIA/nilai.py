# 

jumlah_mahasiswa = 10
data_mahasiswa = []

kategori_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
total_nilai_akhir = 0
nilai_tertinggi = -1
nilai_terendah = 101
mhs_tertinggi = ""
mhs_terendah = ""

print("=== PROGRAM PENGELOLAAN NILAI MAHASISWA ===")

for i in range(1, jumlah_mahasiswa + 1):
    print(f"\n--- Mahasiswa ke-{i} ---")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))
    
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    total_nilai_akhir += nilai_akhir
    
    if nilai_akhir >= 85:
        kategori = 'A'
    elif nilai_akhir >= 75:
        kategori = 'B'
    elif nilai_akhir >= 65:
        kategori = 'C'
    elif nilai_akhir >= 50:
        kategori = 'D'
    else:
        kategori = 'E'
        
    kategori_count[kategori] += 1
    
    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        mhs_tertinggi = nama
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        mhs_terendah = nama
        
    data_mahasiswa.append({
        'nama': nama, 
        'tugas': tugas, 
        'uts': uts, 
        'uas': uas,
        'akhir': nilai_akhir, 
        'kategori': kategori
    })

print("\n" + "="*30 + " REKAPITULASI NILAI MAHASISWA " + "="*30)
for mhs in data_mahasiswa:
    print(f"Nama: {mhs['nama']:<10} | Tugas: {mhs['tugas']:>5} | UTS: {mhs['uts']:>5} | UAS: {mhs['uas']:>5} | Akhir: {mhs['akhir']:>6.2f} | Kategori: {mhs['kategori']}")

print("\n" + "-"*65)
print("STATISTIK KELAS:")
print(f"- Jumlah Mahasiswa per Kategori :")
for kat, jml in kategori_count.items():
    print(f"  Kategori {kat} : {jml} orang")
print(f"- Nilai Tertinggi               : {nilai_tertinggi:.2f} (oleh {mhs_tertinggi})")
print(f"- Nilai Terendah                : {nilai_terendah:.2f} (oleh {mhs_terendah})")
print(f"- Rata-rata Nilai Akhir Kelas   : {total_nilai_akhir / jumlah_mahasiswa:.2f}")                                  