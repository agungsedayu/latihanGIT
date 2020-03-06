#  tidak jalan hanya menu

 import random
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