film = {'1':'Dilan', '2':'Koboy Kampus'}
kelompok = {"1":[],"2":[]}
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
row6=[]
row7=[]
row8=[]
film1_siang = {1:row1,2:row2}
film1_malam = {1:row3,2:row4}
film2_siang = {1:row5,2:row6}
film2_malam = {1:row7,2:row8}
dic_film = {1 : {1:film1_siang,2:film1_malam}, 2: {1:film2_siang,2:film2_malam}}

for i in range(2):
       for j in range(10):
              row1.append("O")
              row2.append("O")
              row3.append("O")
              row4.append("O")
              row5.append("O")
              row6.append("O")
              row7.append("O")
              row8.append("O")

dic_film = {'film1':[], 'film2':[]}
    
loop = True
while loop:
    print("""
    1. Pesan Tiket
    2. Lihat History
    3. Keluar""")
    pilih = int(input('Tentukan Pilihan: '))
    if pilih == 1:
        print("""
        List Film:
        1. Dilan
        2. Koboy Kampus""")
        film = int(input('Silahkan pilih film: '))
        if film == 1:
            print("""
            Pilih jadwal film Dilan:
            1. Siang
            2. Malam""")
            jadwal = int(input('Pilihan: '))
            tiketpesan = int(input('Pesan berapa tiket: '))
            if jadwal == 1:
                for i in range(tiketpesan):
                    for i in range(50):
                        row = int(input('\n Row: '))
                        seat = int(input('\n Seat: '))
                        taken_seat = '\n Tempat duduk \nRow: {} \nSeat: {}'.format(row,seat)
                        if row == 1:
                            film1_siang[1][seat-1]='X'
                            kelompok['1'].append([jadwal,seat,row])
                            break
                        else:
                            film1_siang[1][seat-1]='X'
                            kelompok['1'].append([jadwal,seat,row])
                            break
                    print(taken_seat)
                    print("".join(row1))
                    print("".join(row2))
            elif jadwal == 2:
                for i in range(tiketpesan):
                    for i in range(50):
                        row = int(input('\n Row: '))
                        seat = int(input('\n Seat: '))
                        taken_seats = '\n Tempat duduk \nRow: {} \nSeat: {}'.format(row,seat)
                        if row == 1:
                            film1_malam[1][seat-1]='X'
                            kelompok['1'].append([jadwal,seat,row])
                            break
                        else:
                            film1_malam[1][seat-1]='X'
                            kelompok['1'].append([jadwal,seat,row])
                            break
                    print(taken_seat)
                    print("".join(row3))
                    print("".join(row4))
        elif film == 2:
            print("""
            Pilih jadwal film Dilan:
            1. Siang
            2. Malam""")
            jadwal = int(input('Pilihan: '))
            tiketpesan = int(input('Pesan berapa tiket: '))
            if jadwal == 1:
                for i in range(tiketpesan):
                    for i in range(50):
                        row = int(input('\n Row: '))
                        seat = int(input('\n Seat: '))
                        taken_seat = '\n Tempat duduk \nRow: {} \nSeat: {}'.format(row,seat)
                        if row == 1:
                            film1_siang[2][seat-1]='X'
                            kelompok['2'].append([jadwal,seat,row])
                            break
                        else:
                            film1_siang[2][seat-1]='X'
                            kelompok['2'].append([jadwal,seat,row])
                            break
                    print(taken_seat)
                    print("".join(row5))
                    print("".join(row6))
            elif jadwal == 2:
                for i in range(tiketpesan):
                    for i in range(50):
                        row = int(input('\n Row: '))
                        seat = int(input('\n Seat: '))
                        taken_seats = '\n Tempat duduk \nRow: {} \nSeat: {}'.format(row,seat)
                        if row == 1:
                            film1_malam[2][seat-1]='X'
                            kelompok['2'].append([jadwal,seat,row])
                            break
                        else:
                            film1_malam[2][seat-1]='X'
                            kelompok['2'].append([jadwal,seat,row])
                            break
                    print(taken_seat)
                    print("".join(row7))
                    print("".join(row8))
    elif pilih == 2:
        print('Pesanan anda adalah: ')
    elif pilih == 3:
        print('Terima Kasih')
        loop = False
    else:
        print('Pilihan tidak teredia')


###########################################################################

film = {1:'The Incredibles', 2:'Toy Story'}
jadwal = {1: 'Siang', 2: 'Malam'}
kursi_history = {}

for i in film.values():
    for j in jadwal.values():
        kursi_history[i+j] = 0
#kursi_history = {The incrediblessiang:0, Toy Storysiang:0}

history = {}

def kursi():
    c = []
    for i in range(2):
        d = []
        for j in range(10):
             d.append('O') 
        c.append(d)
    return c          
    # [['o', 'o', 'o'],
    #  ['o', 'o', 'o']]


def pesan_tiket():
    print('List film:\n1. The Incredibles\n2. Toy Story')
    while(True):
        pilih_film = int(input('Silakan Pilih Film: '))
        if pilih_film == 1 or pilih_film == 2:
            break
    while(True):
        pilih_jadwal= int(input('Pilih Jadwal film {}:\n1. Siang\n2. Malam\nPilihan:'.format(film[pilih_film])))
        if pilih_jadwal == 1 or pilih_jadwal == 2:
            break
    while(True):
        tiket_kali = int(input('Pesan Tiket Berapa kali: '))
        if tiket_kali > 0 or tiket_kali <= 20:
            break    

    def pesan_kursi(kali):
        
        for i in range(kali):
            row = int(input('Row:'))
            seat = int(input('Seat:'))
            try:
                #[['O', 'O'],
                # ['O', 'O']]
                if kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][row-1][seat-1] == 'O':
                    kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][row-1][seat-1] = 'X'                
                else:
                    print('Kursi Tidak Tersedia')   
            except:
                print('Salah input') 
                         
            j = ''
            for k in range(2):
                for isi in kursi_history[film[pilih_film]+jadwal[pilih_jadwal]][k]:
               #for l in ['O', 'O', 'O']
                    j += isi
                j += '\n'  

            history[film[pilih_film]+jadwal[pilih_jadwal]+str(row)+str(seat)] = [film[pilih_film],jadwal[pilih_jadwal],row,seat]      
            print('Tempat Duduk\n'+j)   

# pilih film =1
# pilih_jadwal = 1
#kursi_history['theincrediblesiang'] == 0
    if kursi_history[film[pilih_film]+jadwal[pilih_jadwal]] == 0:
        kursi_history[film[pilih_film]+jadwal[pilih_jadwal]] = kursi()
        pesan_kursi(tiket_kali)
    else:
        pesan_kursi(tiket_kali)   

                      
def lihat_history():
    # {'the incrediblessiang11': ['the incredibles', 'siang', 1, 1]}
    for i in history.values():
        # print('Film {jadwal} Jadwal {film} Seat {seat} Row {row}'.format(film =i[0], jadwal=i[1], seat=i[2], row=i[3]))
        
        print(f"Film {i[0]} Jadwal {i[1]}")
        
while(True):
    pilih = int(input('Menu:\n1. Pesan Tiket\n2. Lihat History\n3. Keluar\nTentukan pilihan:'))
    if pilih == 1:
        pesan_tiket()
    elif pilih == 2:
        lihat_history()
    elif pilih == 3:
        break 