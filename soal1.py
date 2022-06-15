"""Soal Coding Interview
Buat sebuah program / function untuk mengecek apakah sebuah kata, frasa dapat dibaca dengan sama, baik dari depan maupun belakang. 
Input : berupa kata
Output : True jika bisa dibaca dengan sama, False bila tidak
Contoh : 

Input
Output
katak
true
basi
false
isi
true

"""

# tambahan coba potong stengah for loop, tambah fungsi rekursif
# buat 3 file, main, soal 1, soal 2


def palindrom(kata):
    check = 0
    setengah = int(len(kata)/2 + 1)
    temp = len(kata)-1

    for i in range(setengah):
        if kata[i] == kata[temp]:
            check += 1
        temp -= 1

    if check == setengah:
        return True

    return False
