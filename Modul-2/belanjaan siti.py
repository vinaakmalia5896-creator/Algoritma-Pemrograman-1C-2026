total_belanjaan = int(input('masukan total belnja awal Rp: '))

if total_belanjaan % 100000 == 0 and total_belanjaan > 0:
    diskon = 1.0 
elif total_belanjaan % 50000 == 0 and total_belanjaan > 0:
    diskon = 0.5 
elif total_belanjaan % 10000 == 0 and total_belanjaan > 0:
    diskon = 0.2 
elif total_belanjaan >=200000:
    diskon = 0.1 
else:
    diskon = 0.0 # harga normal

total_bayar = total_belanjaan - (total_belanjaan * diskon) 
# status_poin = 'poin bertambah' if total_bayar > 0 else 'tidak ada poin'
if total_bayar >0:  
    status_poin = ('poin bertambah')
else:  
    status_poin = ('tidak ada poin')

print(f'total belanja awal: Rp {total_belanjaan: }')
print(f'total harga akhir setelah diskon: Rp {int(total_bayar): }')
print(f'total poin keanggotaan: {status_poin}')