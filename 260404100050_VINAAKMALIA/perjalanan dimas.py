jarak_satu_arah = 100
konsumsi_bbm = 40
sisa_bensin = 1.5
harga_per_liter = 10000

total_jarak = jarak_satu_arah * 2

kebutuhan_bbm = total_jarak / konsumsi_bbm

bbm_dibeli = kebutuhan_bbm - sisa_bensin

total_biaya = bbm_dibeli * harga_per_liter

print("Total jarak perjalanan pulang-pergi: (total_jarak) km")
print("Total kebutuhan bahan bakar: (kebutuhan_bbm) liter")
print("Bahan bakar yang harus dibeli di SPBU: (bbm_dibeli) liter")
print("Total biaya yang harus dikeluarkan Rp:", int(total_biaya))