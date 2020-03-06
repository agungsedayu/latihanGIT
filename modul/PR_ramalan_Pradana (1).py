import random

class ramalan:
    def __init__(self, uang):
        self.uang = uang
        self.odds = []
        self.ramalan = ['sangat buruk', 'buruk', 'cukup baik', 'baik', 'sangat Baik']
        

    def trial(self):
        total = []
        odds1 = []
        temporary = 0

        for num in range(81):
            total.append(num)

        while temporary != 80:
            for num in random.choices(total):
                if num < 80:
                    for j in random.choices(total):
                        if (num + j) < 80:
                            for k in random.choices(total):
                                if (num + j + k) == 80:
                                    odds1.append([num, j, k])
                                    temporary = 80

        if self.uang < 10000:
            self.odds.append([odds1[0][0], odds1[0][1], odds1[0][2], 10, 10])
            return random.randint(0, len(self.odds[0])-1)
            
        elif self.uang >= 10000 and self.uang <= 50000:
            self.odds.append([10, odds1[0][0], odds1[0][1], odds1[0][2], 10])
            return random.randint(0, len(self.odds[0])-1)

        elif self.uang > 50000:
            self.odds.append([10, 10, odds1[0][0], odds1[0][1], odds1[0][2]])
            return random.randint(0, len(self.odds[0])-1)

    def menu(self):
        while True:
                print('Pilih ramalan anda:\n1. Ramalan Pekerjaan\n2. Ramalan Kesehatan\n3. Ramalan Percintaan\n4. Keluar')
                inputan = int(input('Masukkan pilihan: '))
                if inputan == 1:
                    print('\nHasil ramalan: Pekerjaan anda akan {} \n'.format(self.ramalan[self.trial()]))
                elif inputan == 2:
                    print('\nHasil ramalan: Kesehatan anda akan {} \n'.format(self.ramalan[self.trial()]))
                elif inputan == 3:
                    print('\nHasil ramalan: Percintaan anda akan {} \n'.format(self.ramalan[self.trial()]))
                elif inputan == 4:
                    break
                else:
                    print('Tidak ada dalam menu')


ramal = ramalan(5000)
ramal.menu()