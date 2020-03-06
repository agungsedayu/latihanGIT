# TYPE DATA TUPLE

# t = (1, [0, "test"], { "a1" : True })

# print(type(t))
# print(t[1])
# print(t[2]["a1"])
# print(t[1][1])
# t[1][1] = "akan"
# print(t[1][1])
# t[1] = "mark"
# print(t[1])


# t = (1, [0, "test"], { "a1" : True }, (0,{ "test" : 5 },2)) # tuple inside tuple

# print(t[3][1]["test"])

##############################################

# TYPE DATA SETS

# s = { True, 1, 3, 1, 2, 2, 3, 'a', 'a', True, True, False, 'b', 1.4, 1.4 }

# print(s)
# print(type(s)) # untuk mengetahui tipe suatu data
# print(list(s)[1])

# l = [ True, 1, 3, 1, 2, 2, 3, 'a', 'a', True, True, False, 'b', 1.4, 1.4 ] # list
# print(set(l))
# print(list(set(l))[0])

############################################################

# LIST COMPREHENSION

# listNum = [ 1, 2, 3, 4, 5]
# listNum = [item * 2 for item in listNum]
# print(listNum)


# def times2(num) :
#     return num * 2

# listNum = [ 1, 2, 3, 4, 5]
# listNum = [times2(item) for item in listNum]
# print(listNum)

################################################################

# LAMBDA EXPRESSION

# hanya bisa dipakai satu kali
# fungsi kecil


# FUNCTION MAP
# map = melooping fungsi ke setiap parameter

# WITHOUT LAMBDA

# def times2(num) :
#     return num * 2

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum))
# print(listNum)

# WITH LAMBDA

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(lambda num: num * 2, listNum))
# listNum = list(map(lambda num: num * 2 if num <3 else num/2, listNum))
# listNum = list(map(str, listNum))
# print(listNum)

#################################################################

# FILTER
# UNTUK MERETURN YANG TRUE

# WITHOUT LAMBDA

# def genap(num) :
#     return num % 2 == 0

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(genap, listNum))
# print(listNum)

# WITH LAMBDA

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(lambda num: num % 2 == 0, listNum))
# print(listNum)

# FILETER JUGA BISA DI PAKAI UNTUK DICTIONAY dan list

# listnum = {'ini string': 'not string'}
# listnum = list(filter(lambda num: num<20 ,listnum))
# listnum = 'ini string'
# listnum = list(filter(lambda num: num != 'i', listnum))
# print(listnum)


listnum = [1,2,3,4,5]

# def filterlist(function,list_container):
#     z = []
#     for i in range(list_container):
#         if function(i):
#             z.append(i)
#     return z       
# print(filterlist(lambda num: num%2 == 0, listnum))

def maplist(function,list_container):
    z = []
    for i in list_container:
        z.append(function(i))
    return z
print(maplist(lambda num: num*2, listnum))

# data = ['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']
# search = input('Search: ')

# hasil = list(filter(lambda num: search.lower() in num.lower(), data))
# print(hasil)