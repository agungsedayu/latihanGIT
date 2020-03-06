# ini asdas

# print('test')
# print('haiiiiii')
# print('hello world')

# nama = 'Andi'
# print(nama)

# usia = 22
# usia = 23
# print(usia)

# test = 45
# test = 'text'
# print(type(test))

# nama = input('what is your name?:')
# print(nama)

# nama = input('what is your name? ')
# print('nama saya adalah '+ nama)

# nama = input('what is your name? ')
# print(('nama saya adalah ') * 2)

# usiaAndi = 40
# usiaBudi = 20
# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaAndi ** usiaBudi)
#  yg diatas ini namanya floor division
# print(usiaAndi // usiaBudi)

# NGUBAH VARIABEL
# print('umur saya adalah ' + str(30))

# TEST
# CARA 1 inputan tetap string tp dalam prinan dijadikan int
# baru jadi INT
# nama = input('Masukkan Nama: ')
# umur = input('Masukkan Umur: ')
# print('Umur saya 5 tahun kedepan adalah: ' + str(int(umur) + 5))
# print('Umur saya jika di modulus 2 adalah: ' + str(int(umur) % 2))

# cara 2, inputan dijadikan integer terlebih dahulu
# nama = input('Masukkan Nama: ')
# umur = int(input('Masukkan Umur: '))
# print('Umur saya 5 tahun kedepan adalah: ' +str(umur+5))
# print('Umur saya jika di modulus 2 adalah: ' +str(umur%2))

# Math Module
# import math

# print(math.pi);
# print(math.fabs(-4.7));
# print(math.pow(8, 2));
# print(math.sqrt(64));

# ROUND, CEIL & FLOOR
# round itu pembulatan
# math floor maksa bulat ke atas
# math ceil maksa bulet ke bawah
# import math

# print(round(4.7));
# print(round(4.4));
# print(math.floor(4.7));
# print(math.ceil(4.4));

# 2 dibelakan untuk menentukan banyaknya decimal
# print(round(5.123435, 2))

# import dari file new
# kalau untuk beda folder tinggal tambahakan *directory.new
# import math
# import new
# print(new.value)

# STRINGS METHOD
# len = berapa karakter
# method index = untuk nyari urutan sbg contoh (a) jadi hasilnya a adalah urutan ke 1 dari kata halo dunia
# method split = pemisah kiri dan kanan dari kata atau huruf yg ditentukan contoh (a) jadinya (H, lo duni, )
# method lower = semua jadi lower case , upper = uppercase , capitalize = huruf depannya saja yg kapital
# method replace = mengganti kata

# x = 'Halo Dunia'
# print(len(x))  
# print(x.index('Dunia'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.replace('Dunia', 'Apa'))

# Strings Indexing
# 1. posisi drp pada index
# 2. mulai dari posisi ke 2 sampai akhir
# 3. reverse index
# 4. dari awal sampai posisi ke 4
# 5. menentukan posisi ke 2 dan 5
# 6. ngeprint semua
# 7. membalik kata dari posisi -1
# 8. menentkan posisi dari belakang

# text = "I'm Baron, nice to meet you";
# print(text[1]);
# print(text[-1]);
# print(text[2:]);
# print(text[:4]);
# print(text[2:5]);
# print(text[:]);
# print(text[::-1])
# print(text[-4:-1])

# TEST
# nama = input('Masukkan Nama: ')
# umur = int(input('Masukkan Umur: '))
# print('Nama saya jika dimunculkan 2x: ' + (nama. capitalize()*2))
# print('Karakter di nama saya pada posisi modulus 2 umur saya: ' + nama[umur % 2])
# print('''Karakter di nama saya pada posisi negatif modulus 2 umur saya lalu 
#          ditambah 5 hingga sebelum -1 adalah ''' + nama[-((umur % 2) + 5):-1])