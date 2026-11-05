def hitung_nilai_mahasiswa(nama, nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (0.30 * nilai_tugas) + (0.30 * nilai_uts) + (0.40 * nilai_uas)
    
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
        
    if grade in ["A", "B", "C"]:
        status = "Lulus"
    else:
        status = "Tidak Lulus"
        
    print()
    print(f"Nama Mahasiswa : {nama}")
    print(f"Nilai Tugas    : {nilai_tugas}")
    print(f"Nilai UTS      : {nilai_uts}")
    print(f"Nilai UAS      : {nilai_uas}")
    print(f"Nilai Akhir    : {nilai_akhir:.2f}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")

nama = input("Masukkan nama mahasiswa : ")
tugas = float(input("Masukkan nilai Tugas    : "))
uts = float(input("Masukkan nilai UTS      : "))
uas = float(input("Masukkan nilai UAS      : "))

hitung_nilai_mahasiswa(nama, tugas, uts, uas)