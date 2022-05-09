

import random
import time
from os import system, name

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def return_heads_or_tails(random_number):
    if random_number == 1:
        return "Heads"
    else:
        return "Tails"


while True:
    
    clear_screen()
    print("###> HEADS OR TAILS? <###")
    option = input("Heads or Tails: ").lower()

    match option:
        case ("h" | "heads"):
            print("You have chosen Heads!")
            option = 1
        case ("t" | "tails"):
            print("You have chosen Tails!")
            option = 2
        case ("quit" | "q" | "exit"):
            print("Quitting...")
            time.sleep(2)
            exit()

    print(">>> GAME ON!!")
    print(">>> Flipping the coin....") 
    time.sleep(2)

    random_number = random.randint(1,2)

    if option == 1:
        print("Your choice: Heads")
    else:
        print("Your choice: Tails")

    print("Random coin: ", return_heads_or_tails(random_number))
    if option == random_number:
        print("You have won!")
    else:
        print("You have lost!")
    
    time.sleep(2)
    clear_screen()

