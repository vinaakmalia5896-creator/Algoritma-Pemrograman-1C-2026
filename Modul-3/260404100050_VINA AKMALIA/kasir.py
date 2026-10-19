# 

jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

print("=== PROGRAM KASIR TERMINAL BUS ===")
print("Masukkan jarak penumpang (masukkan 0 untuk berhenti)")

while True:
    jarak = float(input("masukkan jarak (km): "))
    
    if jarak == 0:
        break
    elif jarak < 0:
        print("jarak tidak valid! masukkan angka positif.")
        continue
        
    jumlah_penumpang += 1
    total_jarak += jarak
    
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
        
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
        
        
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print(f" -> Penumpang ke-{jumlah_penumpang} mendapat diskon 50%!")
        
    total_pendapatan += tarif

if jumlah_penumpang > 0:
    rata_rata_jarak = total_jarak / jumlah_penumpang
    print("\n=== LAPORAN AKHIR ===")
    print(f"Jumlah Penumpang     : {jumlah_penumpang}")
    print(f"Total Pendapatan     : Rp{total_pendapatan:,.0f}")
    print(f"Jarak Terjauh        : {jarak_terjauh} km")
    print(f"Rata-rata Jarak      : {rata_rata_jarak:.2f} km")
else:
    print("Tidak ada data penumpang yang diproses.")