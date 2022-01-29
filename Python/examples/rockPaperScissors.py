#==========================================
# Title:  ROCK PAPER SCISSORS
# Author: github.com/joaov777
# Date:   28 Jan 2022
# Last update: 28 Jan 2022
# Python version: 3.10.0
#==========================================

import random


def play_game(user_choice):



    machine_choice = random.randint(0,2)

    print(f"Computer chose: {machine_choice}")

    if user_choice == 0 and machine_choice == 2:
        print("You win!")
    elif machine_choice > user_choice:
        print("You lose!")
    elif machine_choice == user_choice:
        print("Draw")
    elif user_choice > machine_choice:
        print("You win!")
    else:
        print("Invalid number!!")

while True:
    print("## ROCK PAPER SCISSORS ##")
    user_choice = int(input("Your choice: (0/1/2): "))

    play_game(user_choice)