suhu = float(input('masukan suhu reaktor (celcius): '))
tekanan = float(input('masukan tekanan gas (bar): '))

if suhu > 1000:
    if tekanan > 50:
        pesan_bahaya = 'meltdwon! segera evakuasi!'
    else:
        pesan_bahaya = 'bahaya suhu: segera turunkan daya!'
elif suhu > 500:
    if tekanan > 30:
        pesan_bahaya = 'tekanan tidak stabil'
    else:
        pesan_bahaya = 'operasi reaktor normal'
else:
    pesan_bahaya = 'reaktor belum cukup panas'

status_pompa = 'pompa maksimal' if suhu >= 800 else 'pompa normal'

print(f'suhu yang diimputkan: {suhu} celcius')   
print(f'tekanan yang diimputkan: {tekanan} bar')
print(f'pesan status bahaya reaktor: {pesan_bahaya}')
print(f'status operasional pompa air: {status_pompa}')    