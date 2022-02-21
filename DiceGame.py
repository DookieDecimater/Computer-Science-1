#Dice Game
#Jackson Bauer
from random import randint
from time import sleep
    

def get_user_guess():
    user_guess = int(input('What number do you guess? 2-12 '))
    return user_guess


budget = 100

def roll_dice(wager, budget):
    first_roll =randint(1, 6)
    second_roll =randint(1, 6)
    total = first_roll + second_roll
    sleep(1)
    user_guess = get_user_guess()
    
    if wager > budget or wager < 1:
        print('Insufficient wager')
    elif user_guess >12 or user_guess < 2:
        print('Invalid guess')
    else:
        print('rolling...')
        sleep(1)
        print('House first roll is ' + str(first_roll) + '.')
        sleep(1)
        print('House second roll is ' + str(second_roll) + '.')
        sleep(1)
        print("House's total roll is " + str(total) + '.')
        sleep(3)
        
        if user_guess == total:
            wager = wager*12
            print('DING DING DING YOU WIN')
            return wager
        else:
            print('Oh so close, be a good sport, play again')
            return -wager


choice = input('Welcome to the Vanilla Unicorn Strip Club and Casino. If you want to play a dice game, input "yes". If you wish to leave, input "leave" ')
sleep(1)
print("sorry, that option isn't available at this time")
sleep(2)
#loop game
while budget > 0:
    wager = int(input('How much would you like to wager: '))
    budget = budget + roll_dice(wager, budget)
    print('new budget = ' + str(budget))
    user_choice = input('Do you want to keep playing? Press the enter key if yes, if no, press "q"')
    if user_choice == "q":
        print('You lose, your budget now equals' + str(budget) + 'dollars')
        break
    elif budget == 0:
        print('Goodbye')
        break
    
