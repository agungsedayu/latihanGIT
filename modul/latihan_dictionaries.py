kata = input('Masukkan Kata: ')
d = {}

for i in kata.split():
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for key, val in d.items():
    print('Kata {} ada sebanyak {} buah'.format(key.capitalize(),val))
