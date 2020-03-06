import re
# months = ['February', 'March' , 'April' , 'May' , 'June' ]
# for month in months:
#     if re.search(r'a' , month): # research dipakai di if
#         print(month)

# if re.search(r'a', 'january maret aprtil june'):
#     print(Yes)


################################################################
# META HARACTER


# hello_list = ['hello', 'world', 'hello world', 'helloworld', '1hello world']
# for word in hello_list:
#     # if re.search(r'^hello', word): # ^
#     #     print(word)
#     if re.search(r'world$', word):  # $
        # print(word)

# cat_list = ['ct', 'cat', 'caat', 'caaaaaat', 'cbat', 'cbt']
# for cat in cat_list:
#     if re.search(r'ca*t', cat): # *
#         print(cat)
#     if re.search(r'ca+t', cat): # +
#         print(cat)
#     if re.search(r'ca?t', cat): # ?
#         print(cat)

# ab_list = ['ab', 'aob', 'aoob', 'aooob', 'aoooob']
# for item in ab_list:
#     if re.search(r'ao{1,3}b', item): # {}
        # print(item)
    # if re.search(r'ao{3}b', item): # {}
        # print(item)

#####
# META CHARACTER SET
#####

# string = 'February March April May June 123'
# match = re.findall(r'[a-zA-Z]+', string)
# match = re.findall(r'[a-zA-Z]', string)
# match = re.findall(r'[a-zA-Z]*', string)
# match = re.findall(r'[^a-zA-Z]', string)
# match = re.findall(r'M[a-zA-Z]+', string)
# match = re.findall(r'[a-zA-Z]+y', string)
# print(match)

# word = 'I want to eat rice 100.11 and 1012.442'
# print(re.findall(r'[a-zA-Z]+|\d+\.+\d+', word))

# Multiline case
# word = 'I want to eat rice\nI did not want to pay any money'
# print(re.findall(r'^I\s[A-Z]+', word, flags= re.M|re.I))
# print(re.findall(r'^I\s[A-Z]+', word, flags= re.I))
# print(re.findall(r'^I\s[A-Z]+', word, flags= re.M))

# word = "Where 1 cat owner's is never been there"
# print(re.sub(r'[^a-zA-Z\']+', ' ', word))

# word = "Only 2 time but 1 is enough. The ! is another sign"
# print(re.split(r'[0-9.!]', word))

regex = re.compile('[a-zA-Z0-9]+')
regex = re.compile('[a-zA-Z0-9\']+')
word = "Do not feed the monkey's. It is really bad !!!"
print(regex.findall(word))
print(regex.sub('',word))