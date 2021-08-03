#!/usr/bin/env python

# CHOOSE LEFT OR RIGHT
# This simple Python script is used to check a few of the language features
# regarding loops, functions, variables, packages, etc.


from subprocess import call
import os
from time import sleep
#import sleep

#verify user option
def checkOption(userOption):
    if userOption == "right":
        print("You chose right!!")
    elif userOption == "left":
        print("You chose left!!")
    else:
        print("Choose a valid option!!")

# clearing the screen
def clearScreen():
    os.system('clear') if os.name == 'posix' else 'cls'
    #_ = call('clear' if os.name == 'posix' else 'cls')


#### Main starts here

clearScreen()

while True:
    print(">> This is a basic program <<")

    choice = input('Insert right or left: ').lower()

    if choice.lower() == 'q' or choice.lower() == 'quit':
        print("You have just quit!")
        break
    print("Your system is:", os.name)
    checkOption(choice)
    input("Press any key to continue...")
    clearScreen()
    
    sleep(2)
    #time.sleep(10)
    
