total_belanja = int(input("Masukkan total belanja: "))
print("---- Rincian Belanja ----")
print("Total belanja sebelum diskon:", int(total_belanja))

if total_belanja % 100000 == 0:
    diskon = total_belanja * 100/100
    total_setelah_diskon = total_belanja - diskon
elif total_belanja % 50000 == 0:
    diskon = total_belanja * 50/100
    total_setelah_diskon = total_belanja - diskon
elif total_belanja % 10000 == 0:
    diskon = total_belanja * 20/100
    total_setelah_diskon = total_belanja - diskon
elif total_belanja >= 200000:
    diskon = total_belanja * 10/100
    total_setelah_diskon = total_belanja - diskon
else:
    diskon = 0
    total_setelah_diskon = total_belanja
print("Diskon yang diberikan:", int(diskon), "(", int(diskon / total_belanja * 100), "% )")
print("Total harga akhir setelah diskon:", int(total_setelah_diskon))

point = "Point bertambah" if total_setelah_diskon > 0 else "Tidak ada point"
print("Point:", point)