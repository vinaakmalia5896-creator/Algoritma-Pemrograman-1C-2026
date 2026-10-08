nomor_acak = 7
print('tebak nomor acak dari 1-10')
tebakan = int(input('tebakan anda (bil bulat): '))
if tebakan == nomor_acak:
    print('selamat! tebakan anda benar')
    print('tapi tidak ada hadiah untuk anda: ')
elif tebakan <nomor_acak:
    print('tebakan anda terlalu kecil')
else:
    print('tebakan anda terlalu besar')
    print('selesai')


    a=int(input('masukan umur: '))
    if a <= 15 :
        print('muda')
    elif a <=20 :
        print('remaja')
    else:
        print('tua')


# ganjil genap
nilai = int(input('masukan angka: '))
if nilai%2:
    print('bilangan ini ganjil')
else:
    print('bilangan ini genap')

nilai = int(input('masukan nilai: '))
if nilai >= 75:
    print('lulus')
else:
    print('tidak lulus')
