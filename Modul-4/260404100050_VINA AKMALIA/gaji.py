
GAJI_POKOK_PER_HARI = 100000
TAMBAHAN_SHIFT_MALAM = 50000

total_gaji_mingguan = 0

print("=== PROGRAM PENGHITUNGAN GAJI MINGGUAN KARYAWAN ===")

for hari in range(1, 8):
  print(f"\nHari ke-{hari}")

  while True:
    jam_lembur = int(input("Masukkan jam lembur (0-8 jam): "))
    if 0 <= jam_lembur <= 8:
      break
    else:
      print("Jumlah lembur melebihi batas atau tidak valid! Silakan masukkan ulang.")

  shift_malam = input("Apakah bekerja pada shift malam? (y/t): ")

  upah_lembur = 0
  if 1 <= jam_lembur <= 3:
    upah_lembur = jam_lembur * 25000
  elif jam_lembur == 4:
    upah_lembur = 100000
  elif jam_lembur == 6:
    upah_lembur = 200000
  elif jam_lembur == 8:
    upah_lembur = 300000

  tambah_shift = 0
  if shift_malam == "y" or shift_malam == "Y":
    tambah_shift = TAMBAHAN_SHIFT_MALAM

  gaji_harian = GAJI_POKOK_PER_HARI + upah_lembur + tambah_shift
  total_gaji_mingguan += gaji_harian

print("\n========================================")
print(f"Total Gaji Mingguan Karyawan: Rp {total_gaji_mingguan:,}")
print("========================================")