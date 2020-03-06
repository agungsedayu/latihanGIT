# import numpy as np

# def data():
#     matrix = np.arange(1, 4*4 + 1).reshape(4, 4)
#     print(matrix)
#     putar = input('Mau diputar ke kanan / kiri?: ')
#     banyaknya = int(input('Mau diputar berapa kali?: '))

#     if putar == 'kanan':
#         matrix = np.rot90(matrix, -(banyaknya))
#         print(matrix)
#         keluar = input('Anda mau mencoba kembali? (y/n): ')
#         if keluar == 'y':
#             data()
#         elif keluar == 'n':
#             print('Terima kasih')
#         else:
#             print('invalid input')
#     elif putar == 'kiri':
#         matrix = np.rot90(matrix, banyaknya)
#         print(matrix)
#         keluar = input('Anda mau mencoba kembali? (y/n): ')
#         if keluar == 'y':
#             data()
#         elif keluar == 'n':
#             print('Terima kasih')
#         else:
#             print('invalid input')
#     else:
#         print('Anda harus masukkan kiri atau kanan')
#         data()
# data()

# ##############################################

# testList = [[1,2,3,4], 
# [5,6,7,8], 
# [9,10,11,12], 
# [13,14,15,16]]

# cetak = ''

# inputan = input('Putar ke kanan atau ke kiri?: ')
# if inputan == 'kanan':
#     inputan2 = int(input('Ingin diputar berapa kali?: '))
#     if (inputan2%4) == 0 and (inputan2%2) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 testList = testList
#     elif (inputan2%3) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[len(testList)-1-j][i] = testList[i][j]
#     elif (inputan2%2) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[len(testList)-1-i][len(testList)-1-j] = testList[i][j]
#     else:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[j][len(testList)-1-i] = testList[i][j]

#     for i in range(len(temp)):
#         for j in range(len(temp)):
#             cetak += str(temp[i][j]) + ' '
#         cetak += '\n'
#     print(cetak)

# elif inputan == 'kiri':
#     inputan2 = int(input('Ingin diputar berapa kali?: '))
#     if (inputan2%4) == 0 and (inputan2%2) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 testList = testList
#     elif (inputan2%3) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[j][len(testList)-1-i] = testList[i][j]
#     elif (inputan2%2) == 0:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[len(testList)-1-i][len(testList)-1-j] = testList[i][j]
#     else:
#         temp = [i[:] for i in testList]
#         for i in range(len(testList)):
#             for j in range(len(testList)):
#                 temp[len(testList)-1-j][i] = testList[i][j]

#     for i in range(len(temp)):
#         for j in range(len(temp)):
#             cetak += str(temp[i][j]) + ' '
#         cetak += '\n'
#     print(cetak)
    
# else:
#     print('Pilihan tidak ada!')

# ####################################################

# import numpy as np

# def urutan():

#     ukuran = int(input('Masukkan ukuran yang Anda mau: ')) 
#     selection = int(input('Pilihan\n1. Angka urut\n2. Angka random\n'))

#     if selection == 1:
#         board = np.arange(1, ukuran*ukuran + 1).reshape(ukuran, ukuran)
#     elif selection == 2:
#         board = np.random.randint(1, 100, size=ukuran*ukuran).reshape(ukuran, ukuran)
#     print(board)

#     rotate = input('Mau diputar ke kiri / kanan?\n')
#     how_many = int(input('Mau diputar berapa kali?\n'))

#     if rotate == 'kiri':
#         board = np.rot90(board, how_many)
#         print(board)
#         ending = input('Anda mau mencoba kembali? (y/n)\n')
#         if ending == 'y':
#             urutan()
#         elif ending == 'n':
#             print('Terima kasih sudah menggunakan program ini')
#         else:
#             print('Anda harus masukkan y / n\nMohon ulangi dari awal, thanks')

#     elif rotate == 'kanan':
#         board = np.rot90(board, -how_many)
#         print(board)
#         ending = input('Anda mau mencoba kembali? (y/n)\n')
#         if ending == 'y':
#             urutan()
#         elif ending == 'n':
#             print('Terima kasih sudah menggunakan program ini')
#         else:
#             print('Anda harus masukkan y / n\nMohon ulangi dari awal, thanks')


#     else:
#         print('Anda harus masukkan kiri atau kanan\nMohon ulangi dari awal, thanks')
#         urutan()

# urutan()


###################################################

import random

# Generate_x*y_angka
def number_generate(x):
    number = []
    pilihan = int(input('Pilih\n1.Angka urut\n2.Angka random\nMasukkan pilihan: '))
    if pilihan == 1:
        for i in range(x):
            temp_number =[]
            for j in range(x):
                temp_number.append((j+1)+(i*x))
                # anggap x = 4
                # temp_number awalnya [1,2,3,4] karena j awalnya 0 sampai 3 dan i awalany 0
                # temp_number setelah itu [5,6,7,8] karena i sekarang 1 tapi j tetap 0 sampai 3
            number.append(temp_number)
    elif pilihan == 2:            
        for i in range(x):
            temp_number = []
            for j in range(x):
                temp_number.append(random.randint(1,101))
            number.append(temp_number)   
    return number
# [[1,2,3,4], [5,6,7,8], [9,10, 11, 12], [13,14,15,16]]


# Print_angka
def print_angka(angka):
    for list_dalam_list in angka:
        # list_dalam_list ini isinya diawal adalah [1,2,3,4]
        z = ''
        for satuan in list_dalam_list:
            z += str(satuan)
            z += ' '
        print(z)

#Memutar
def putarputar():
    ukuran = int(input('Masukkan ukuran: '))
    angka = number_generate(ukuran)
    print_angka(angka)
    putar = input('Putar ke arah?: ')
    kali = int(input('Putar berapa kali: '))
    if putar == 'Kanan' or putar == 'kanan':
        for c in range(kali):
            list_kanan = []
            for i in range(len(angka)):
                # misal kita punya [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
                list_temp =[]
                for j in range((len(angka)-1),-1,-1):
                    list_temp.append(angka[j][i])
                list_kanan.append(list_temp)
            angka = list_kanan            
    elif putar == 'Kiri' or putar == 'kiri':
        for c in range(kali):
            list_kiri = []
            for i in range((len(angka)-1),-1,-1):
                list_temp =[]
                for j in range((len(angka))):
                    list_temp.append(angka[j][i])
                list_kiri.append(list_temp)    
            angka = list_kiri
    print_angka(angka)
                
while(True):
    angka = []
    putarputar()
    exit = input('Coba lagi [y/n]: ')
    if exit == 'y':
        True
    elif exit == 'n':
        print('Terima kasih')
        break  