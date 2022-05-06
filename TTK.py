#jackson bauer
#tik tac toe

import time#imports time library
board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}#dictonary

count = 0       
winner = False      
play = True#defines play     
tie = False     
curr_player = ''    
player_details = [] 


def get_player_details(curr_player):
    if curr_player == 'A':
        return ['B','O']#stores player value
    else:
        return ['A','X']
    

def print_board():
   
    for i in board:#for loop
        print( i, ':', board[i], ' ', end='')
        if i%3 == 0:
            print()


def win_game(marker, player_id):
   
    if board[1] == marker and board[2] == marker and board[3] == marker or \
    board[4] == marker and board[5] == marker and board[6] == marker or \
    board[7] == marker and board[8] == marker and board[9] == marker or \
    board[1] == marker and board[4] == marker and board[7] == marker or \
    board[2] == marker and board[5] == marker and board[8] == marker or \
    board[3] == marker and board[6] == marker and board[9] == marker or \
    board[1] == marker and board[5] == marker and board[9] == marker or \
    board[3] == marker and board[5] == marker and board[7] == marker:
#win condition if statements
        print_board()
        time.sleep(1)
        print('congrats player', player_id, 'you win')
        return True

    else:
        return False


def insert_input(slot_num, marker):
    while board[slot_num] != ' ':
        print("that spots taken, choose another")
        slot_num = int(input())
    board[slot_num] = marker

def play_again():
    print("if you wish to play again, type 'yes' ")
    play_again = input()

    if play_again.lower() == 'yes':
        for z in board:
            board[z] = ' '
        return True
    else:
        print("smell ya later")
        return False
    
while play:

    print_board()

    player_details = get_player_details(curr_player)
    curr_player = player_details[0]#player A
    print("Player {} where do you want to go?".format(curr_player))
    input_slot = int(input())

    insert_input(input_slot, player_details[1])
    count += 1
    
    winner = win_game(player_details[1], curr_player)
    if count == 9 and not winner:
        print("scratch, you both lose")
        tie = True
        print_board()

    if winner or tie:
        play = play_again()
        if play:
            curr_player = ''
            count = 0