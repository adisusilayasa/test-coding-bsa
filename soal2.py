"""
Buat aplikasi penjumlahan diagonal array 3 x 3
Contoh
11 2 4
4 5 6
10 8 12

Jumlahkan diagonal kekanan, A = 11 + 5 + 12 = 28
Jumlahkan diagonal kekiri, B = 4 + 5 + 10 = 19
Jumlahkan kedua hasil diagonal A + B = 28 + 19 = 47


Note:
Source code bisa di simpan dalam bentuk file extension sesuai dengan bahasa pemrograman yang digunakan ato dalam file .txt.
"""

# kiri : 02 11 20
# kanan 00 11 22

# challenge persingkat code(lebih efisien)
# pake satu looping


def penjumlah1(arr):
    loop = 0
    d_kanan = 0
    d_kiri = 0
    temp_kiri = 2

    while loop != 3:
        d_kiri += arr[loop][temp_kiri]
        d_kanan += arr[loop][loop]
        loop += 1
        temp_kiri -= 1
    keduanya = d_kanan + d_kiri
    return d_kanan, d_kiri, keduanya
