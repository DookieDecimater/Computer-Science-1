# #jackson bauer
# #practice makes perfect
# #1 is even
# #x = int(input('pick a number'))
# def is_even(x):
#     if (x % 2) == 0:
#         print('true')
#     else:
#         print('false')
# #is_even(x)
# 
# #2 is_int
# #x = float(input('choose a number'))
# def is_int(x):
#     if (x % 1) == 0:
#         print('true')
#     else:
#         print('false')
# #is_int(x)
# 
# #3 digit_sum
# #def digit_sum(x):
#     sum = 0
#     for digit in str(x):
#         sum += int(digit)
#     return sum
# #x = int(input('choose a number you want to sum'))
# #print(digit_sum(x))
# 
# #4 factorials
# #import math
# #x = int(input('what number do you want to factorial?'))
# #print(int(math.factorial(x)))
# 
# #5 is_prime
# #x= int(input('choose a random number to see if its prime'))
# 
# #def is_prime(x):
#     flag = False
#     if x > 1:
#         for i in range(2, x):
#             if (x % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         print('false')
#     else:
#         print('true')
# #is_prime(x)
#         
# #6 reverse
# string = str(input('write a word to reverse'))
# reversedstring = ''
# strlen = len(string)
# for count in range(strlen):
#     character = string[strlen - 1 - count]
#     reversedstring = reversedstring + character
#     
# print(reversedstring)

#7 anti vowel
# string = input('type a word yo')
# def anti_vowel():
#     newstr = string;
#     vowels = ('a','e','i','o','u');
#     for x in string.lower():
#         if x in vowels:
#             newstr = newstr.replace(x,'');
#     print(newstr);
# anti_vowel()

#8 scrabble score
# word = str(input('what word do you want to scramble score?')).lower()
# score = {'a':1, 'e':1, 'i':1, 'l':1, 'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
# def scrabble_score(word):
#     points= 0
#     for i in word:
#         if i in score:
#             points += score[i]
#     word = points
#     return word
# print(scrabble_score(word))

#9 censor
# text = str(input('type a funny sentence'))
# word = str(input('what word do you want to censor?'))
# def censor(text,word):
#     return text.replace(word, '*' * len(word))
# print(censor(text,word))
# censor(text,word)

#10 count

def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total = total + 1
    return total
#print(count([1,1,1],1))

#11 purify

def purify(numbers):
    flist = []
    for i in numbers:
        if i % 2 == 0:
            flist.append(i)
    return flist
#print (purify([1,2,3]))

# 12 product
def product(x):
    total = 1
    for i in x:
        total = total * i
    return total
#print (product([4,5,5]))

#13 remove duplicates
def remove_duplicates(x):
    nlist = []
    for i in x:
        if i not in nlist:
            nlist.append(i)
    return nlist
#print(remove_duplicates([1,1,2,2]))

#14 median
def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return(list[int(len(list)/2)] + list[int(list(len(list)/2 -1))]) /2
    else:
        return (list[int(len(list)/2)])
pprint(median[1,2,3,44,5,])