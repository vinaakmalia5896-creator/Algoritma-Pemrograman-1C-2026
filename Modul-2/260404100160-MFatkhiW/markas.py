pin = int(input("Masukkan PIN (tiga digit): "))
jam = int(input("Masukkan jam (0-23): "))
digit_pertama = pin // 100
digit_kedua = (pin // 10) % 10
digit_ketiga = pin % 10
print("---- Rincian PIN Garasi ----")
print("PIN:", pin)
print("Digit pertama:", digit_pertama)
print("Digit kedua:", digit_kedua)
print("Digit ketiga:", digit_ketiga)

if pin % 5 == 0:
    if jam < 12:
        status = "Garasi pagi terbuka"
    else:
        status = "Garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if digit_pertama + digit_ketiga == digit_kedua:
        status = "Garasi VIP terbuka khusus Bos"
    else:
        status = "Kode genap ditolak, alarm berbunyi"
else:
    status = "Akses ditolak sepenuhnya"

print("Status garasi:", status)
status_cctv = "Mode malam merekam" if jam > 18 else "Mode siang standby"
print(status_cctv)