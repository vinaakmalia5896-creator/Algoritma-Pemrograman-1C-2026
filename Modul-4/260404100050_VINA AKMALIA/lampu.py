#


while True:
   jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
   if jumlah_baris > 0 :
     break
   print('jumlah harus lebih dari 0! silakan coba lagi')

while True :
   jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))  
   if jumlah_lampu > 0 :
     break
   print('jumlah harus lebih dari 0! silakan coba lagi')  



for baris in range(1, jumlah_baris + 1):
  print(f"\n--- Baris {baris} ---")
  for lampu in range(1, jumlah_lampu + 1):
    if lampu % 3 == 0:
      print(f"Lampu ke-{lampu}: Mengalami gangguan")
    else:
      print(f"Lampu ke-{lampu}: Berfungsi normal")

print("\n[Peringatan] Periksa sumber listrik utama taman.")


