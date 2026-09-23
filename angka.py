#Logika Urutan Angka

#Start
A = int(input("Masukkan Nilai A: "))
B = int(input("Masukkan Nilai B: "))
C = int(input("Masukkan Nilai C: "))

#Validasi Jika Semua angka identik
if (A==B==C):
    print("Semua Angka Identik")
#Validasi Jika Terdapat Angka Duplikat
elif A == B or B == C or C == A:
    print("Terdapat Angka Duplikat")

#Cek Variabel B
elif B < A and B < C:
    print("B Adalah Nilai Terkecil")

elif B < C and B < A or A > C and A > B or C > A and C > B:
    print("Nilai B Berada di Antara A dan C")

elif B > A and B > C:
    print("B Adalah Nilai Terbesar")

#End
