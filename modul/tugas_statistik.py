import math

list_angka = [1,3,3,3,4,4,2,4,10]

def mean(list) :
    sum = 0
    for i in list :
        sum += i
    hasil = sum / len(list)
    return hasil
# print(mean(list_angka))

def median(list) :
    list.sort()
    hasil = 0 
    if (len(list) % 2 != 0):
	    hasil = list[math.floor(len(list)/2)]
    else :
        mid1 = list[(int(len(list) / 2)) - 1]
        mid2 = list[int(len(list) / 2)]
        hasil = (mid1 + mid2) / 2
    return hasil
# print(median(list_angka))

def mode(list) :
    countlist = []
    for num in list :
        check = False
        for list1 in countlist :
            if(list1[0] == num) :
                list1[1] += 1
                check = True
        if(check == False) :
            countlist.append([num, 0])

    max_frequency = 0
    modes = []
    for list1 in countlist :
        if (list1[1] > max_frequency) :
            modes = [list1[0]]
            max_frequency = list1[1]
        elif (list1[1] == max_frequency) :
            modes.append(list1[0])

    if (len(modes) == len(countlist)) :
        modes = []
    return modes
# print(mode(list_angka))

def variances(list):
    z = 0
    for i in list:
        z += (i - mean(list))**2
    return z/(len(list))
# print(variances(list_angka))

def stadev(list):
    z = variances(list)
    std = math.sqrt(z)
    return std
# print(stadev(list_angka))

def skewness(list):
    z = 0
    for i in list:
        a = (i - mean(list))**3
        z += a
    b = z/len(list)
    c = (stadev(list))
    d = c**3
    e = b/d
    return e
# print(skewness(list_angka))

def kurtosis(list):
    z = 0
    for i in list:
        a = (i - mean(list))**4
        z += a
    b = z/len(list)
    c = (stadev(list))
    d = c**4
    e = b/d
    f = e-3
    return f
# print(kurtosis(list_angka))

list_function = [mean, median, mode, variances, stadev, skewness, kurtosis]
def statistic_sample(x,y):
    if x == list_angka and y == 'Mean':
        print(list_function[0](list_angka))
    elif x == list_angka and y == 'Median':
        print(list_function[1](list_angka))
    elif x == list_angka and y == 'Modus':
        print(list_function[2](list_angka))
    elif x == list_angka and y == 'Varian':
        print(list_function[3](list_angka))
    elif x == list_angka and y == 'Standard Deviasi':
        print(list_function[4](list_angka))
    elif x == list_angka and y == 'Skewness':
        print(list_function[5](list_angka))
    elif x == list_angka and y == 'Excess Kurtosis':
        print(list_function[6](list_angka))

statistic_sample(list_angka,'Skewness')