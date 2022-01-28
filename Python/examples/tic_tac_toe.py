
#==========================================
# Title:  TIC TAC TOE
# Author: github.com/joaov777
# Date:   27 Jan 2022
# Last update: 28 Jan 2022
# Python version: 3.10.0
#==========================================

from os import system, name
import sys
import time
import random
from typing import ParamSpecArgs

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

#check whether the player has a valid name
#name criteria: only letters allowed for names
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

        #create_board()
        print(str(board[0]).strip('[]'))
        print(str(board[1]).strip('[]')) 
        print(str(board[2]).strip('[]'))

        if(check_winner(board,curr,players)):
            user_choice = input("#> Do you want to play again? (yes/no): ").lower()
            if (user_choice == "yes") or (user_choice == "y"):
                main()
            elif (user_choice == "no") or (user_choice == "n"):
                sys.exit()
        curr = switch_player(curr)

        player_move = str(input(f"{players[curr]}: "))

        if(check_move(player_move)):
            register_move(player_move,curr)
        else:
            print("Invalid Option!") ; input()
            curr = switch_player(curr)

def check_winner(board,curr,players):

    #board
    # 00 01 02
    # 10 11 12
    # 20 21 22

    winning_conditions = [  
                            board[0][0] + board[0][1] + board[0][2], #row1
                            board[1][0] + board[1][1] + board[1][2], #row2
                            board[2][0] + board[2][1] + board[2][2], #row3
                            board[0][0] + board[1][0] + board[2][0], #col1
                            board[0][1] + board[1][1] + board[2][1], #col2
                            board[0][2] + board[1][2] + board[2][2], #col3
                            board[0][0] + board[1][1] + board[2][2], #diagonal1
                            board[0][2] + board[1][1] + board[2][0]  #diagonal2
                        ]

    p1_winner = ['XXX']
    p2_winner = ['OOO']

    for i in range(0,len(winning_conditions)):
        if (p1_winner[0] == winning_conditions[i]) or (p2_winner[0] == winning_conditions[i]):
            print("#> WE HAVE A WINNER!!") 
            print(f"#> {players[curr]} WON!!") ; input()
            return True
            #sys.exit()
    
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
        board[int(player_move[0])][int(player_move[1])] = "O"

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

def main():

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

main()
