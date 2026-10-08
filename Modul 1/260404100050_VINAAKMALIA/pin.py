pin = int(input('masukan 3 digit kode pin: '))
jam = int(input('masukan jam kedatangan (0-23): '))

d1 = pin //100
d2 = (pin // 10) % 10
d3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        pesan_akses = 'garasi pagi terbuka'
    else:
        pesan_akses = 'garasi malam terbuka'
elif pin % 2 == 0:
    if (d1 + d3) == d2:
        pesan_akses ='garasi VIP terbuka khusus bos'
    else:
        pesan_akses = 'kode genap ditolak, alarm berbuyi!'
else:
    pesan_akses = 'akses di tolak sepenuhnya'

status_cctv = 'mode malam merekam' if jam > 18 else 'mode siang stanby' 


print(f'digit pin -> pertama: {d1}, kedua: {d2}, ketiga: {d3}')
print(f'pesan status akses pintu garasi: {pesan_akses}')
print(f'status kamera cctv markas: {status_cctv}')