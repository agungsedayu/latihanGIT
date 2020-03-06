##############################################################
# SOAL 1

# def nb_year(p0, percent, aug, p):
#     howyear = 1
#     while p0 < p:
#         p0 = p0 + (p0*percent/100) + aug
#         if p0 > p:
#             break
#         else:
#             howyear = howyear + 1
#     return howyear
       
# print(nb_year(1000, 2, 50, 1200))


###########################################################
# SOAL 2

# def tickets(peopleinline):
#     money = []
#     dualima = 0
#     limapuluh = 0
#     seratus = 0

#     for i in peopleinline :
#         if i == 25:
#             dualima += 1
#             money.append(i)
#         elif i == 50 and dualima > 0:
#             dualima -= 1
#             limapuluh += 1
#             money.append(i)
#         elif i == 50 and dualima == 0:
#             print('NO')
#             break
#         elif i == 100 and dualima >= 1 and limapuluh >=1:
#             seratus += 1
#             limapuluh -= 1
#             dualima -= 1
#             money.append(i)
#         elif i == 100 and dualima >= 3:
#             seratus += 1
#             dualima -= 3
#             money.append(i)
#         else:
#             print('NO')
#             break
#     if len(money) >= len(peopleinline):
#         print('YES')

# tickets([25, 25, 50, 50, 100])


###################################################################
# SOAL 3

n = 5
a = 1
b = 0
c = []
d = []
e = []
f = []
g = []

z = ''

for i in range(n):
    for j in range(0, int(i*-1.4)+int(n+2)):
        z += '  '
    for k in range(0, i+1):
        if i == 0:
            c.append(a)
        elif i == 1:
            d.append(a)
        elif i <= 2:
            e.append(a)
        elif i <= 3:
            f.append(a)
        elif i <= 4:
            g.append(a)

        z += str(a) + '   '
        a += 2
    z += '\n'

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0

for i in range(len(c)):
    sum1 += c[i]
for i in range(len(d)):
    sum2 += d[i]
for i in range(len(e)):
    sum3 += e[i]
for i in range(len(f)):
    sum4 += f[i]
for i in range(len(g)):
    sum5 += g[i]

print(z)
print('rowSumOddNumber(1); // {}'.format(sum1))
print('rowSumOddNumber(2); // {}'.format(sum2))
print('rowSumOddNumber(3); // {}'.format(sum3))
print('rowSumOddNumber(4); // {}'.format(sum4))
print('rowSumOddNumber(5); // {}'.format(sum5))


########################################################################


def nbYear(p0, percent, aug, p) :
    year = 0
    while p0 < p :
        p0 = p0 + (p0 * percent/100) + aug
        year += 1
    
    return year


#people in line
def tickets(peopleInLine):
    check = 'YES'
    list = []
    money = {25:0, 50:0, 100:0}
    for j in peopleInLine:
        if j == 25:
            money[25] += 1
            list.append(j)
        elif j == 50 and money[25] > 0:
            money[25] -= 1
            money[50] += 1
            list.append(j)
        elif j == 50 and money[25] == 0:
            check = 'NO'
            break
        elif j == 100 and money[50] >= 1 and money[25] >= 1:
            money[100] += 1
            money[50] -= 1
            money[25] -= 1
            list.append(j)      
        elif j == 100 and money[25] >= 3:
            money[100] += 1
            money[25] -= 3
            list.append(j)
        else:
            check = 'NO'
            break            
    
    if len(list) == len(peopleInLine):
        print('YES')
    print(check)

peopleInLine = [25, 25, 25, 100, 25, 50, 100, 100]


#RowSumOddNumbers
def rowSumOddNumbers(n) :
    numbers  = []
    nilai = 1
    for i in range(1, n+1) :
        temp = []
        for j in range(i) :
            temp.append(nilai)
            nilai += 2
        numbers.append(temp)
    print(numbers)
    
    #ngeprint segitiga
    z = ''
    for num, i in zip(numbers, range(len(numbers))) :
        for j in range(n-i) :
            z += '  '
        for k in num :
            #ljust berfungsi kayak padding, nambahin spasi di sebelah kanan huruf (jumlahnya sampai 4)
            z += str(k)
            z += ' '*(4 - len(str(k)))
            z += str(k).ljust(4, ' ')
        z += '\n' 
    print(z)

    sum_row = ''
    
    for num in numbers[-1]:
        if num == numbers[-1][-1]:
            sum_row += str(num)
        else:    
            sum_row += str(num)
            sum_row += ' + '
    sum_row += ' = {}'.format(sum(numbers[-1]))       
    
    if sum(numbers[-1]) == 1:
        print(1)
    else:
        print(sum_row)