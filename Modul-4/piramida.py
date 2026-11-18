
n = int(input("Masukkan sebuah bilangan bulat positif (n): "))

print(f"\n--- Pola Dua Piramida Angka (n = {n}) ---")

for i in range(1, n + 1):
  pira1 = ""
  for j in range(1, i + 1):
     pira1 += str(j) + " "
    

  spasi = "  " * (n - i) * 2

  pira2 = ""
  for j in range(i, 0, -1):
    pira2 += str(j) + " "

  print(pira1 + spasi + pira2)

