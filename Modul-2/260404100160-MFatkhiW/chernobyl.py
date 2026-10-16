suhu = float(input("Masukkan suhu reaktor dalam derajat Celsius: "))
tekanan = float(input("Masukkan tekanan dalam Bar: "))
print("---- Rincian Kondisi Reaktor ----")
print("Suhu:", suhu, "°C")
print("Tekanan:", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        kondisi = "Meltdown! Segera evakuasi!"
    elif tekanan <= 50:
        kondisi = "Bahaya Suhu! Segera turunkan daya!"
elif suhu > 500 and suhu <= 1000:
    if tekanan > 30:
        kondisi = "Tekanan tidak stabi!"
    else:
        kondisi = "Operasi reaktor normal."
elif suhu <= 500:
    kondisi = "Reaktor belum cukup panas."
print("Kondisi:", kondisi)

pompa = "Pompa maksimal" if suhu > 800 else "Pompa normal"
print("Status Pompa:", pompa)