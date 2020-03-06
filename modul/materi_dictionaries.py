# dictionaries = key, value
#  nama index di dictionary adalah key

# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"] };

# print(d["key1"])
# print(d["key2"])
# print(d["kucing"])
# print(d["kucing"][1])

# for i in d:
#     print(i)

# for i in d.keys:
#     print(i)

# print(d.keys())

# print(list(d.keys())) # untuk melist dkeys

# print('kucing' in list(d.keys()))  # untuk mengecek ada tidaknya key dalam list keluarnya True/False

# print(d.values()) # untuk memunculkan valuenya

# print(d.items()) # untuk mendapatkan key maupun valuenya secara langsung

# for key, val in d.items():
#     print(key)
#     print(val)

# d['key3'] = 'kucing1' # untuk menambahkan data pada dict, harus bikin key baru
# d['key2'] = 'anjing'  # untuk mengganti val pada dict
# del d['key1'] # untuk menghilangkan key+val pada dict
# print(d)  

# Untuk comperehensive
# list_lain = ['Buah', 'Kucing', 'Mobil']
# dictio = {key:val for val, key in enumerate(list_lain)} # untuk membalik key,val = val,key terus di enumerate
# print(dictio)

