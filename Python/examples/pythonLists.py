
from os import system, name
import sys

## This program is intended for study purposes only
## It adds, deletes and shows fruits

def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def add_fruit(fruit_name):
    """
    This function adds one or several new fruits. Separate all fruits by single spaces. 
    """

    #if more than one fruit is added, they are separated by a single space
    all_fruits = fruit_name.split(" ")

    #check whether the fruit is already added or not
    for af in range(0,len(all_fruits)):
        for f in range(0,len(fruits)):
            if all_fruits[af] != fruits[f]:
                if len(all_fruits) > 1:
                    
                    fruits.extend(all_fruits[af])
                else:
                    print("ola"); input()
                    fruits.append(fruit_name[f])
            else:
                print(">> ERROR: " + all_fruits[af] + " already added!") ; input()
    
    #if fruit_name in fruits:
    #    print(">> ERROR: This fruit has already been added!") ; input()
    #    return

    #if more than one fruit is added at the same time
   # if len(all_fruits) > 1:
   #     fruits.extend(all_fruits)
   # else:
   #    fruits.append(fruit_name)

def delete_fruit(fruit_name):
    fruits.remove(fruit_name)

def list_all_fruits(fruits):
    print("The fruits added are: ", *fruits, sep = " ")

def menu_option(menu_option,number_option):
    print(f"{number_option}) {menu_option}")

fruits = []

while True:
    clear_screen()
    print("## The fruit party ##")
    menu_option("Add fruit",1)
    menu_option("Delete fruit",2)
    menu_option("See all fruits",3)
    #menu_option("Quit",4)
    option_chosen = input("Option: ")

    match option_chosen:
        case ("q" | "Q" | "quit" | "QUIT"):
           sys.exit()

        case ("1"):
            add_fruit(input("ADD FRUIT(s): "))

        case ("2"):
            delete_fruit(input("DELETE FRUIT(s): "))

        case ("3"):
            list_all_fruits(fruits)
            input()

