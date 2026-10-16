password_brankas = int(input("Masukkan password brankas (tiga digit): "))

digit_pertama = password_brankas // 100
digit_kedua = (password_brankas // 10) % 10
digit_ketiga = password_brankas % 10
print("---- Rincian Password Brankas ----")
print("Password brankas:", password_brankas)
print("Digit pertama:", digit_pertama)
print("Digit kedua:", digit_kedua)
print("Digit ketiga:", digit_ketiga)

nilai_pelacak_awal = digit_pertama * digit_ketiga
nilai_pelacak = nilai_pelacak_awal
print ("Nilai pelacak awal:", nilai_pelacak_awal)

if digit_kedua % 2 != 0:
    nilai_pelacak += 25
else:
    nilai_pelacak -= digit_kedua
nilai_pelacak_perubahan_1 = nilai_pelacak
print("Nilai pelacak perubahan tahap 1:", nilai_pelacak_perubahan_1)

if nilai_pelacak % 3 == 0:
    nilai_pelacak //= 3
else:
    nilai_pelacak *= 2
nilai_akhir = nilai_pelacak
print("Nilai pelacak perubahan tahap 2 (nilai akhir):", nilai_akhir)

if nilai_pelacak > 50:
    status_password = "Password terdeteksi sebagai kategori A"
elif nilai_pelacak > 20:
    status_password = "Password terdeteksi sebagai kategori B"
else:
    status_password = "Password ditolak"
print("Kategori password:", status_password)

if nilai_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print("Siklus password:", siklus)