#ice cream flavor
#jackson bauer
from time import sleep
def guess():
    hint = ['g','its good with chocolate','its not a prime color','santa likes it', 'its green you bum']
    x = 0
    for i in hint:
        choice = input('Whats my favorite ice cream flavor? Your choices are vanilla, chocolate, mint, confetti, cherry, cookies n cream, peanut butter cup, and neopolitan ')
        if choice == 'mint':
            print('good job son. mint is my favorite ice cream flavor. its refreshing coolness is my drive for completing the school day. Chocolate chunks are a bonus')
            break
        else:
            print (hint[x+1])
            x = x+1
            sleep(2)
              
guess()