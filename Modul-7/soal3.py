undangan = set()
webinar_a = set()
webinar_b = set()

n_undangan = int(input("Masukkan jumlah orang yang diundang: "))
for i in range(n_undangan):
    nama = input(f"Nama undangan ke-{i+1}: ")
    undangan.add(nama)

n_a = int(input("\nMasukkan jumlah peserta hadir Webinar A: "))
for i in range(n_a):
    nama = input(f"Nama peserta Webinar A ke-{i+1}: ")
    webinar_a.add(nama)

n_b = int(input("\nMasukkan jumlah peserta hadir Webinar B: "))
for i in range(n_b):
    nama = input(f"Nama peserta Webinar B ke-{i+1}: ")
    webinar_b.add(nama)

semua_peserta = webinar_a.union(webinar_b)
hadir_keduanya = webinar_a.intersection(webinar_b)
hanya_satu = webinar_a.symmetric_difference(webinar_b)
tidak_hadir = undangan.difference(semua_peserta)

print("\n=== HASIL ANALISIS KEHADIRAN WEBINAR ===")
print("1. Semua peserta dari kedua webinar      :", semua_peserta)
print("2. Peserta yang hadir di keduanya        :", hadir_keduanya)
print("3. Peserta hanya hadir di salah satu     :", hanya_satu)
print("4. Nama undangan yang tidak hadir        :", tidak_hadir)