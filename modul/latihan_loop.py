# SOLVET IT 1

# z =''

# for item in range (5,0,-1):
#     for item1 in range(0, item):
#         z +=' * '
#     z+='\n'

# print(z)


# SOLVE IT 2

# z =''

# for item in range (5,0,-1):
#     for item1 in range(0, item):
#         z +=' * '
#     z+='\n'
# for item in range (1,5):
#     for item1 in range(0, item+1):
#         z +=' * '
#     z+='\n'

# print(z)

# SOLVE IT 3

# z = ''

# for item in range(10):
#     print((' * '*(1+2*item)).center(1+6*10))

# print(z)

# SOLVE IT 4

# z= ''

# for item in reversed(range(10)):
#     print((' * '*(1+2*item)).center(1+6*10))

# print(z)

# SOLVE IT 5

# z=''

# for item in range(5):
#     print((' * '*(1+2*item)).center(1+6*10))
# for item in reversed(range(5)):
#     print((' * '*(1+2*item)).center(1+6*10))

# print(z)

# SOLVE IT 6
# BELOM SELESAI

# z = ''
# for item in range(1,5):
#     for item1 in range(item):
#         print('* ', end = "")
#     for item2 in range(8-2*item):
#         print('  ', end = "")
#     for item3 in range(item):
#         print('* ', end = "")
#     z +='\n'

# print(z) 

# z =''
# x =''

# for item in range (5,0,-1):
#     for item1 in range(0, item):
#         z +=' * '
#     z+='\n'
# for item in range (1,5):
#     for item1 in range(0, item+1):
#         z +=' * '
#     z+='\n'

# for item in range (5,0,-1):
#     for item1 in range(0, item):
#         x +=' * '
#     x+='\n'
# for item in reversed(range (1,5)):
#     for item1 in range(0, item+1):
#         x +=' * '
#     x+='\n'

# print(z+x)
# print(x)
# print(z)

size = int(input('Masukkan Besar Bintang: '))
z = ''
for j in range (size+1):
    if j < size:
        for k in range (1,size*2):
            if k <=size-j or k >= size+j:
                z += ' * '
            else:
                z += '   '
        z += '\n'            
    else:
        for l in range (size-2, -1, -1):
            for m in range (1,size*2):
                if m <=size-l or m >= size+l:
                    z += ' * '
                else:
                    z += '   '
            z += '\n'

print(z)