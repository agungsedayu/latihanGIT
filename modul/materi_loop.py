# angka = 1

# while(angka <= 10):
#    print(angka)
#    angka += 1


# listItem = list(range(1,11,2))
# print(listItem)

# for item in range(1,11,2):
# 	print(item)


# y = 'Nomor urut '

# for item in range(1,11) :
#    print(y + str(item))

# z=''
# for item in range(0,5):
#    z += ' * '

# print(z)

# z =''
# for item in range(0,5): #karena str jadinya kesamping
#    z += ' * \n'

# print(z)

# z=''

# for item in range(5):
#    for item1 in range(0, item+1):
#       z += ' * '
#    z += '\n'

# print(z)

# LOOP STATEMENT (STATEMENT YANG MUNCUL HANYA DIDALAM LOOP(MAU WHILE ATAUPUN FOR IN))

# Break berhenti saat kondisinya sudah mencukupi, apapun itu dibawah break tidak akan jalan

print('Contoh Break')
for i in range(10):
   if i == 5:
      break
   else:
      print(i)


# PASS

# a = list(range(0,3))
# menjalankan dibawahnya (langsung ke print(item))
# for item in a:
#    if not item:
#       pass
#    else:
#       print(item * 2)
#    print(item)


# Continue

# a = list(range(0,3))
# # jika kontinue langsung balik keatas
# for item in a:
#    if not item:
#       continue
#    else:
#       print(item * 2)
#    print(item)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)