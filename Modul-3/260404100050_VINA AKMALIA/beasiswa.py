# 

kuota_penuh = 3
jumlah_terima_penuh = 0
total_proses = 0

print("=== PROGRAM SELEKSI BEASISWA ===")

while total_proses < 10 and jumlah_terima_penuh < kuota_penuh:
    print(f"\nSeleksi Mahasiswa ke-{total_proses + 1}")
    nama = input("Masukkan Nama: ")
    ipk = float(input("Masukkan IPK: "))
    
    if ipk < 3.00:
        print(f"-> {nama} tidak memenuhi syarat (IPK < 3.00). Dilewati.")
        total_proses += 1
        continue
        
    penghasilan = float(input("Masukkan Penghasilan Orang Tua per Bulan (Rp): "))
    
    if penghasilan <= 3000000:
        print(f"-> {nama} MENDAPATKAN BEASISWA PENUH.")
        jumlah_terima_penuh += 1
    elif penghasilan <= 5000000:
        print(f"-> {nama} MENDAPATKAN BEASISWA SEBAGIAN.")
    else:
        print(f"-> {nama} tidak mendapatkan beasiswa.")
        
    total_proses += 1

print("\n=== SELEKSI SELESAI ===")
if jumlah_terima_penuh >= kuota_penuh:
    print("Kuota beasiswa penuh (3 orang penerima beasiswa penuh telah tercapai). Proses seleksi dihentikan.")
else:
    print("Seluruh kuota mahasiswa telah selesai diperiksa.")