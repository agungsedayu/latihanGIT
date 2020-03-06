# class bisa disebut blueprint

# class classy:
#     my_class = 7

# contoh = classy()
# print(contoh.my_class)

# contoh_lain = classy()
# print(contoh_lain.my_class)

# class Manusia:
#     def __init__(self,name,age):
#         self.nama = name
#         self.umur = age
#     def salamkenal(self):
#         print('Nama saya adalah {} dan sya berumur {}'.format(self.nama, self.umur))
        # return self.age * len(self.name)

# manusia1 = Manusia('Baron', 22)
# print(manusia1)
# print(manusia1.nama)
# print(manusia1.umur)
# print(manusia1.__dict__)
# print(manusia1.__dict__['nama'])
# manusia1.age = 35  #untuk mengganti data
# print(manusia1.age)
# manusia1.job = 'Data Scientist' #untuk menambahkan variables baru
# print(manusia1.job)
# manusia1.salamkenal()

# class anak(Manusia):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.kelamin = gender

# Nel = anak('Nel', 27, 'Male')
# Nel.salamkenal()

########################################################################
# LATIHAN

class bikinmenu:
    def __init__(self, name, food, price):
        self.nama = name
        self.makanan = food
        self.harga = price
        self.history = []

    def get_menu(self):
        print('Menu makanan\n 1. Ayam goreng harganya 1K\n 2. Nasi bakar harganya 2K\n 3. Sate kambing harganya 3K')

    def menu_price(self):
        x = int(input('Mau beli yang mana: '))
        if x == 1:
            print('{} telah membeli {} dengan harga {}'.format(self.nama, self.makanan[0], self.harga[0]))
            self.history.append(x)
        elif x == 2:
            print('{} telah membeli {} dengan harga {}'.format(self.nama, self.makanan[1], self.harga[2]))
            self.history.append(x)
        elif x == 3:
            print('{} telah membeli {} dengan harga {}'.format(self.nama, self.makanan[2], self.harga[3]))
            self.history.append(x)

    # def history(self):

Paul = bikinmenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])
Paul.get_menu()

Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.menu_price()