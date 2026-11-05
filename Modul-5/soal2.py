def cek_palindrom(kata):
    kata_dibalik = kata[::-1]
    if kata == kata_dibalik:
        return True
    else:
        return False

input_kata = input("Masukkan kata: ")

is_palindrom = cek_palindrom(input_kata)

print(f"Hasil pengembalian fungsi: {is_palindrom}")
if is_palindrom:
    print(f"Kata '{input_kata}' merupakan PALINDROM.")
else:
    print(f"Kata '{input_kata}' BUKAN merupakan palindrom.")