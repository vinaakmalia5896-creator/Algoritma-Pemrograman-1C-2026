def jumlah_pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return jumlah_pelanggan(n - 1) + jumlah_pelanggan(n - 2)

n = int(input("Masukkan hari ke-N: "))

if n <= 0:
    print("Masukkan hari dalam bentuk bilangan bulat positif (> 0)!")
else:
    print("\nDeretan Fibonacci jumlah pelanggan:")
    for i in range(1, n + 1):
        if i == n:
            print(jumlah_pelanggan(i))
        else:
            print(jumlah_pelanggan(i), end=", ")
        
    total = jumlah_pelanggan(n)
    print(f"\nJumlah pelanggan Bu Lastri pada hari ke-{n} adalah: {total} orang")