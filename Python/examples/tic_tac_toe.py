
from os import system, name
import sys
import time
import random

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

#check whether the player has a valid name
#criteria here is: only letter allowed for names
def check_player(player_name):
    if player_name.isalpha():
        return True
    else:
        return False

def game_title():
    print(f"### - TIC TAC TOE - ###")

def create_game(players):
   
    #current player
    curr = 1

    while True:
        clear_screen()
        game_title()

        curr = switch_player(curr)

        #create_board()

        #check_winner() 
        print(str(board[0]).strip('[]'))
        print(str(board[1]).strip('[]')) 
        print(str(board[2]).strip('[]'))

        player_move = str(input(f"{players[curr]}: "))

        if(check_move(player_move)):
            register_move(player_move,curr)
        else:
            print("Invalid Option!") ; input()
            curr = switch_player(curr)
    
def check_move(player_move):
    allowed_moves = [ "00", "01" ,"02" , "10" , "11" , "12" , "20" , "21" , "22" ]
    
    if (player_move in allowed_moves) and (player_move not in played_moves):
        played_moves.append(player_move)
        return True
    else:
        return False

def register_move(player_move,curr):
    
    if curr == 0:
        board[int(player_move[0])][int(player_move[1])] = "X"
    elif curr == 1:
        board[int(player_move[0])][int(player_move[1])] = "Y"

def switch_player(current_player):
    if current_player == 0:
        return 1
    elif current_player == 1:
        return 0 

#creating the board

row0 = ['#','#','#']
row1 = ['#','#','#']
row2 = ['#','#','#']
board = [row0,row1,row2]
players = []
played_moves = []

while True:

    clear_screen()
    game_title()
    print("(1) - New Game")
    print("(2) - Quit")
    option = input("Option: ")
    
    match option:
        case ("1"):
            while True:
            
                clear_screen()
                game_title()
                print("##> NEW GAME")

                player1 = input("Player 1: ")
                player2 = input("Player 2: ")

                if check_player(player1) and check_player(player2):
                    players.append(player1)
                    players.append(player2)
                    create_game(players)
                else:
                    print("You have inserted invalid names!") ; input()

        case ("2"):
            sys.exit()





























