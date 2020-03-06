list_data = []

def isi_list():
    data_entry = int(input('Berapa data yang ingin dimasukkan: '))
    for i in range(data_entry):
        data = int(input('Masukkan Angka: '))
        list_data.append(data)
    main_menu()

def lihat_list():   
    print(list_data)
    main_menu()

def ascending():
    for i in range(len(list_data)):
        for j in range(i+1, len(list_data)):
            if list_data[i] > list_data[j]:
                list_data[i], list_data[j] = list_data[j], list_data[i]
    print(list_data)
    main_menu()

def descending():
    for i in range(len(list_data)):
        for j in range(i+1, len(list_data)):
            if list_data[i] < list_data[j]:
                list_data[i], list_data[j] = list_data[j], list_data[i]
    print(list_data)
    main_menu()

def tinggirendah():
    min = list_data[0]
    max = list_data[0]
    for i in list_data:
        if i > max:
            max = i
        if i < min:
            min = i
    print('Angka Tertinggi ' + str(max))
    print('Angka Terendah '+ str(min))
    main_menu()

def ganjilgenap():
    ganjil = 0
    genap = 0
    for i in range(len(list_data)):
        if i %2 == 0:
            genap += 1
        elif i %2 == 1:
            ganjil +=1
    print('Jumlah angka yang terbilang ganji adalah {} dan genap adalah {}'.format(ganjil, genap))
    main_menu()

def main_menu():
    print("""    
    MAIN MENU
    1. Isi List
    2. Lihat List
    3. Sort List Ascending
    4. Sort List Descending
    5. Nilai tertinggi dan Terendah
    6. Jumlah List Ganjil dan Genap
    7. Exit """)
    pilihan = int(input('Pilih Menu: '))
    if pilihan == 1:
        isi_list()
    elif pilihan == 2:
        lihat_list()
    elif pilihan == 3:
        ascending()
    elif pilihan == 4:
        descending()
    elif pilihan == 5:
        tinggirendah()
    elif pilihan == 6:
        ganjilgenap()
    elif pilihan == 7:
        print('Terima Kasih')
        exit()
    else:
        print('Invalid Input')
        main_menu()
print(main_menu())

###############################################################

testList = [[1,2,3,4], 
[5,6,7,8], 
[9,10,11,12], 
[13,14,15,16]]

cetak = ''

inputan = input('Putar ke kanan atau ke kiri?: ')
if inputan == 'kanan':
    inputan2 = int(input('Ingin diputar berapa kali?: '))
    if (inputan2%4) == 0 and (inputan2%2) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                testList = testList
    elif (inputan2%3) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[len(testList)-1-j][i] = testList[i][j]
    elif (inputan2%2) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[len(testList)-1-i][len(testList)-1-j] = testList[i][j]
    else:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[j][len(testList)-1-i] = testList[i][j]

    for i in range(len(temp)):
        for j in range(len(temp)):
            cetak += str(temp[i][j]) + ' '
        cetak += '\n'
    print(cetak)

elif inputan == 'kiri':
    inputan2 = int(input('Ingin diputar berapa kali?: '))
    if (inputan2%4) == 0 and (inputan2%2) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                testList = testList
    elif (inputan2%3) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[j][len(testList)-1-i] = testList[i][j]
    elif (inputan2%2) == 0:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[len(testList)-1-i][len(testList)-1-j] = testList[i][j]
    else:
        temp = [i[:] for i in testList]
        for i in range(len(testList)):
            for j in range(len(testList)):
                temp[len(testList)-1-j][i] = testList[i][j]

    for i in range(len(temp)):
        for j in range(len(temp)):
            cetak += str(temp[i][j]) + ' '
        cetak += '\n'
    print(cetak)
    
else:
    print('Pilihan tidak ada!')




############################################################
# CARA 2

#Fungsi sort
#[1,2,425,3,0]
def fungsi_sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def fungsi_sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr    

# Fungsi minimum maximum

def minmax(list):
    angka_min = fungsi_sort_ascending(list)[0]
    angka_max = fungsi_sort_descending(list)[0]
    return print('Nilai tertinggi {} dan nilai terendah {}'.format(angka_max,angka_min))

#Fungsi odd and even count

def odd_even(list):
    genap = 0
    ganjil = 0
    for i in list:
        if i % 2 == 0:
            genap += 1
        else:
            ganjil += 1    
    return print('Jumlah angka ganjil ada {} dan angka genap ada {}'.format(ganjil, genap))

#Fungsi Insert Word to array
def insert_word(list):
    jumlah = int(input('Berapa kali memasukkan angka: '))
    for l in range(jumlah):
        while(True):
            try:
                a = int(input('Masukkan angka: '))
                list.append(a) 
                break
            except:
                print('Invalid input')
                 


#Fungsi menu utama
# def menuarray():
#     x = []
#     pilihan = 1
#     while(pilihan < 6):
#         print ('Main menu \n')
#         print ('1. Isi Array' + '\n'+ '2. Lihat Array' + '\n'+ '3. Sort Array' + '\n'+ '4. Nilai tertinggi dan terendah' 
#             +'\n'+'5. Jumlah Ganjil dan Genap' + '\n'+ '6. Keluar')
        
#         pilihan = int(input('Piilh yang mana?: '))

#         if (pilihan == 1):
#             jumlah = int(input('Berapa kali memasukkan angka: '))
#             for l in range(jumlah):
#                 a = int(input('Masukkan angka: '))
#                 x.append(a)  

#         if (pilihan == 2):
#             print (x)

#         if (pilihan == 3):
#             c = int(input('1. Ascending' + '\n'+ '2. Descending' + '\n'+ 'Pilih yang mana: '))
#             if c == 2:       
#                 fungsi_sort_descending(x)
#             elif c == 1:
#                 fungsi_sort_ascending(x)
#             else: 
#                 print('Invalid input, coba lagi')
#                 pilihan = 1    

#         if (pilihan == 4):
#             minmax(x)

#         if (pilihan == 5):
#             odd_even(x)

#         if (pilihan == 6):
#             print('Terima kasih')

#         if (pilihan <= 0 or pilihan > 6):
#             print('Invalid input, coba lagi')
#             pilihan = 1
               
# menuarray()


list_function = [insert_word, print, fungsi_sort_ascending, fungsi_sort_descending, minmax, odd_even]
def menu_lain():
    x = []
    pilihan = 1
    while(pilihan < 7):
        print ('Main menu \n')
        print ('1. Isi List' + '\n'+ '2. Lihat List' + '\n'+ '3. Sort List Ascending' + 
               '\n'+ '4. Sort List Desscending' + '\n' +
                '5. Nilai tertinggi dan terendah' 
                +'\n'+'6. Jumlah Ganjil dan Genap' + '\n'+ '7. Keluar')
        
        pilihan = int(input('Piilh yang mana?: '))      
        if (pilihan == 7):
            print('Terima kasih')
        elif (pilihan <= 0 or pilihan > 6):
            print('Invalid input, coba lagi')
            pilihan = 2
        else:
            list_function[pilihan-1](x)    

menu_lain()
