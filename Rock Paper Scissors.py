#jackson bauer
#rock paper scissors
from random import randint
from time import sleep

def decide_winner():
    uscore = 0
    cscore = 0
    while uscore < 3 and cscore < 3:
        
            
        user_choice = input('Choose beween rock, paper, or scissors ').upper()
       
    
        options = ['rock','scissors','paper']
        computer_choice = options[randint(0,2)]
        
        print('Computer Selecting...')
        sleep(2)
        print('Computer chose '+computer_choice)
        sleep(2)
        
        if user_choice == computer_choice:
            print('It is a Tie!')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print ('User wins!')
            uscore = uscore + 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print ('User wins!')
            uscore = uscore + 1
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print ('User wins!')
            uscore = uscore + 1
        else:
            print ('Computer wins, better luck next time.')
            cscore = cscore + 1
        print('User Score:' + str(uscore) + ' ' + 'Computer Score' + str(cscore) )
        sleep(4)
        
        if uscore == 3:
            print('Congrats, you win!')
        else:
            print('You Lose')
        
decide_winner()


