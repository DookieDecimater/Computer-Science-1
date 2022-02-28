#password generator
#jackson bauer

from random import randint


num = [1,2,3,4,5,6,7,8,9,0]
symbol = ['!', '*', '&', '%', '+', '~','=','?',')','(','^','`','>','<','-','$','"','|','@']
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
cap = ['Q','W','E','R','T','Y','U','I','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

length = int(input('Hi, I am a password generator. How long do you want your password to be? '))
total = []
def ran_char(num,symbol,letter,cap):
    charnum =  num[randint(0, len(num) -1)]
    charsymbol =  symbol[randint(0, len(num) -1)]
    charletter =  letter[randint(0, len(num) -1)]
    charcap =  cap[randint(0, len(num) -1)]
    ran_char = (charnum, charsymbol,charletter,charcap)
    char = ran_char[randint(0, len(ran_char) -1)]
    return char

for x in range(length):
    total.append(ran_char(num,symbol,letter,cap))
        
for x in total:
    print(x, end='')
    