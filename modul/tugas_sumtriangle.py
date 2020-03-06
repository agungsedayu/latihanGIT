def sum_of_triangle(n):
    z = []
    start = 1
    for i in range(n):
        for j in range(1,i+2):
            if i < j:
                print('[' + str(start)+']', end = ' ')
            else:
                print(start, end = ' ')
            start +=1
        z.append(start-1)
        print('\n')
    x = 0
    for y in range(len(z)):
        x = x + z[y]
    print('Sum of each last part of the triangle is {}\n'.format(x))

sum_of_triangle(5)

#####################################################################

# CARA 2

def sum_triangular_numbers(n):
   if n < 0:
      return 0
   else:    
      number = []
      for i in range(1,n+1):
         number_temp = []
         for j in range(i,i*2):
            if i == 1 or i == 2:
               number_temp.append(j)
            else:
               number_temp.append(j + number[i-3][-1])
               # print(j)
               # print(number[i-3][-1])
               # print(number_temp)
         number.append(number_temp)
      sum_ = 0
      number_print = number.copy()
      z = ''
      for item in number:
         sum_ += item[-1]

      # for item in number_print:
      #    item[-1] = [item[-1]]

      for item in number_print:
         for val in item:
            if val == item[-1]:
               z  += '[{}]'.format(val)
            else:    
               z+=str(val)
               z+=' '
         z+='\n'
      print(z)        
      return print('sum of each last part of the triangle is {}'.format(sum_))

sum_triangular_numbers(5)