

n = int(input("Masukkan tinggi setengah menara (2 - 15): "))

if 2 <= n <= 15:
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        naik = "".join(str(j % 10) for j in range(1, i + 1))
        turun = "".join(str(j % 10) for j in range(i - 1, 0, -1))
        
        print(spasi + naik + turun)


    for i in range(n - 1, 0, -1):
        spasi = " " * (n - i)
        naik = "".join(str(j % 10) for j in range(1, i + 1))
        turun = "".join(str(j % 10) for j in range(i - 1, 0, -1))
        
        print(spasi + naik + turun)
else:
    print("Tinggi setengah menara tidak valid! Harap masukkan angka antara 2 sampai 15.")