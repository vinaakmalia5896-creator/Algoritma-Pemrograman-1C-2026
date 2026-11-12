def evaluasi_kelayakan(status, ram):
    ram_int = int(ram)
    if status == 'normal' and ram_int >= 8:
        return 'Layak'
    else:
        return 'Tidak Layak'

inventaris_pc = []
jumlah_input = int(input("Masukkan jumlah PC yang ingin didata: "))

for i in range(jumlah_input):
    print(f"\n--- Data PC Ke-{i+1} ---")
    nama_pc = input("Masukkan Nama PC: ")
    status_pc = input("Masukkan Status (Normal/Rusak): ")
    ram_pc = input("Masukkan Kapasitas RAM (GB): ")
    
    inventaris_pc.append([nama_pc, status_pc, ram_pc])

print("\n=== HASIL EVALUASI INVENTARIS PC ===")
for pc in inventaris_pc:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]  

    try:
        kelayakan = evaluasi_kelayakan(status, ram)
    except Exception :
        kelayakan = 'format ram kacau'

    hasil_cetak = '"{ "PC": "' + nama + '", "Status": "' + kelayakan + '" }"'
    print(hasil_cetak)