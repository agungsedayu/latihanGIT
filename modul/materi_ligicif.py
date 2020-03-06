# x = 5
# y = '5'

# print(x == y)
# print(x > int(y))
# print(x >= int(y))
# print(x < int(y))
# print(x <= int(y))

# x = 5
# y = '5'
# z = 6

# print(x==int(y) and int(y)<z)
# print(x==int(y) or int(y)<z)
# print(not(x==int(y) or int(y)<z))


# nilai = 40
# if nilai > 80:
#     print('Execellent')
# elif nilai >= 60 and nilai <= 80:
#     print('Good Job')
# else:
#     print('Dont give up')

# nilai = 81

# if nilai > 80:
#     print('Execellent')
#     if nilai == 81:
#         print('Nilai ku 81')
#     elif nilai == 82:
#         print('Nilai ku 82')
#     else:
#         print('Nilai lebih dari 80')
# elif nilai >= 60 and nilai <= 80:
#     print('Good Job')
# else:
#     print('Dont give up')


# jomblo = True

# if (jomblo) :
#    print('Masih jomblo!')
# else :
#    print('Udah taken!')


######################################

# LATIHAN

nilai = input('Masukkan Angka: ')
if int(nilai) % 2 == 1:
    print('Angka ' + nilai + ' tergolong bilangan GANJIL')
else :
    print('Angka {} tergolong bilangan GENAP'.format(nilai))

# SOAL 2

# massa = float(input('Masukkan Massa(kg): '))
# tinggi = int(input('Masukkan Tinggi(cm): '))
# IMT = massa/(tinggi/100)

# print('Massa '+ str(massa) + 'kg & tinggi ' + str(tinggi/100) + 'm')
