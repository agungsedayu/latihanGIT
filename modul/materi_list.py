# LIST

# mobil = ['aliya', 'avanza', 12]
# motor = ['aliya', 'avanza', 12, True, ['jeruk','mangga']]
# print(motor)
# print(motor[0])
# print(motor[-1])
# print(motor[4])
# print(motor[2:])
# print(motor[::-1])

# INDEXING PERLU UNTUK MENGAKSES DATA
# LIST BISA DIPAKAI UNTUK LOOPING

# for x in motor:
#     print(x)

# print(motor)

# motor.append('BMW')
# print(motor)

# motor[-2] = 'Mercedes'  #untuk mengganti posisi spesifik ke index
# print(motor)

# print(motor.pop(3)) #untuk mengeluarkan data dari index

# listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]

# print(listTest[1])
# print(listTest[:2])
# print(listTest[2])
# print(listTest[2][1:])
# print(listTest[2][2])
# print(listTest[2][3][0])


# LIST COMPREHENSIF

# contoh = [i for i in range(5)]
# print(contoh)

# contoh = [str(i) for i in range(5)]  # bisa untuk merubah langsung ke str
# print(contoh)

# contoh = [i*j for i in range(5) for j in range(2)] # loop dalam loop
# print(contoh) 
# cara baca diatas
# for i in range(5):
    # for i in range(2):
        # i*j   

# bisa dimasukkan kondisional juga
# contoh = [i*j if i < 3 else i+j for i in range(5) for j in range(2)] # list komprehensif tidak ada elif, loopingnya selalu dibelakang kondisi
# print(contoh)
# cara baca diatas
# for i in range(5):
#     for i in range(2):
#         if i < 3:
#             i*j
#         else:
#             i+j

buah = ['jeruk', 'nanas', 'apel', 'mangga', 'pir', 'kiwi', 'semangka']
mobil = ['Alya', 'Avanza', 'Kijang', 'Terios', 'BMW', 'Brio', 'Innova']

# contoh= [i[:2] if len(i) > 4 else 'buah lain' for i in buah]
# print(contoh)

# for i in enumerate(buah):  # enumerate biasa digunakan di LOOP
#     print(i)               # enumerate unutk menunjukan index dan value
   
# for idx, val in enumerate(buah):
#     print(idx)
#     print(val)

# for idx, val in enumerate('Apel'):
#     print(idx)
#     print(val)

# for item in zip(buah, mobil):
#     print(item)

# for i, j in zip(buah, mobil):
#     print(i+ ' '+ j)

for i, j, k in zip(buah, mobil, range(7)):
    print(i+ ' '+ j+ ' '+ str(k))