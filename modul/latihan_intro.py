# SOAL 1

# import math
# x=4
# y=3
# z=2
# print('W = '+ str(math.pow(((x+y*z)/(x*y)),z)))

# SOAL 2

# import math
# angka = int(input('Masukkan Angka: '))
# print('kuadrat dari ' + str(angka) + ' adalah ' + str(math.pow(angka , 2 )))

# SOAL 3

# soal = int(input('Masukkan hari: '))
# tahun = soal // 360
# bulan = (soal % 360) // 30
# minggu = ((soal % 360) % 30) // 7
# hari = ((soal % 360) % 30) % 7
# print('485 hari = '+str(tahun)+' tahun '+str(bulan)+' bulan '+str(minggu)+' minggu ' + str(hari) + ' hari ')

# SOAL 4
# Andi x + Budi x = 49
# Rasio Andi & Budi = 0,4 = 2/5
# x = 7
# umurAndi = x*2
# umurBudi = x*5
# print('Usia Andi 2 tahun lagi adalah '+ str(umurAndi+2))
# print('Usia Budi 2 tahun lagi adalah '+ str(umurBudi+2))

# CARA 2
# total = int(input('Total umur: '))
# rasio = float(input('Rasio umur: '))
# umurbudi = (total*10) / (10 + (rasio * 10))
# umurandi = total - umurbudi
# print('Umur Andi {}'.format(umurandi +2))
# print('Umur Budi {}'.format(umurbudi + 2))

# SOAL 5

# text = input('kata: ')
# print(text.count('a'))

# CARA 2
# word = input('Kata: ')
# cari = input('Huruf yang dicari: ')
# print(int(len(word.split(cari)))-1)

# SOAL 6

# Mobil A dan B start jam 9
# Mobil A dan B memiliki waktu tempuh yang sama
# Rasio kecepatan A & B = 3/2, berarti rasio jarak A & B = 2/3
# A = 60
# B = 2/3*A
# Jarak = 120
# JarakA = 3/5*120
# JarakB = 2/5*120
# waktutempuhjamA = JarakA//A
# waktutempuhmenitA = JarakA%A
# print('Jam tabrakan mobil A & B adalah jam ' + str(waktutempuhjamA+9) + ' lewat ' + str(waktutempuhmenitA) + ' menit')

# CARA 2
# import math

# jarak_dalam_km = int(input("Jarak antara kendaraan?: "))
# kecepatan_a_km_per_h = int(input("Kecepatan kendaraan a?: "))
# kecepatan_b_km_per_h = int(input("Kecepatan kendaraan b?: "))
# jam_berangkat = int(input('Jam Berangkat?: '))
# menit_berangkat = int(input('Menit Berangkat?: '))

# waktu_tabrakan_dalam_menit = (
#     jarak_dalam_km/(kecepatan_a_km_per_h + kecepatan_b_km_per_h))*60
# print(str(waktu_tabrakan_dalam_menit) + ' menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

# print('Waktu A & B bertabrakan adalah jam {}.{} WIB'.format(int(jam), int(menit)))
# #jam 10.12 WIB


########################

# GITHUB

# SOAL 1

# x = int(input('Masukkan input: '))
# digit1 = x//100
# digit2 = x%100
# print('Output: ' + str('{}{}'.format(digit2, digit1)) )

# CARA 2
# x = int(input('Masukkan input: '))
# print(x % 100 * 100 + x // 100)

# SOAL 2

# import math
# r = int(input('Masukkan jari jari: '))
# luas = (math.pi*r**2)
# print('luasnya adalah: ' + str(luas))

# SOAl 3

# angka1 = int(input('Input 1: '))
# angka2 = int(input('Input 2: '))
# digit1 = angka1//10
# digit2 = angka2//10
# digit3 = angka1%10
# digit4 = angka2%10
# print('Output: ' + str('{}{}{}{}'.format(digit1, digit2, digit3,digit4)))

# CARA 2
# angka1 = int(input('Input 1: '))
# angka2 = int(input('Input 2: '))
# digit1 = angka1//10
# digit2 = angka2%10
# digit3 = angka1//10
# digit4 = angka2%10
# print(digit1 * 1000 + digit3 * 100 + digit2 * 10 + digit4)

# SOAL 4

# text = input('Text: ')
# remove = input('Remove: ')
# print(text.replace(remove, ''))

# SOAL 5

# kata = input('Kata: ')
# katasplit = kata.split(' ')
# print(katasplit[1] + ' ' + katasplit[0])