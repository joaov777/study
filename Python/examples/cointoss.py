#!/usr/bin/env python3

# HEAD OR TAILS? Who will win?
# This program automatically tosses the coin until
# Heads or Tails happen 5 times

# modules
import random
from time import sleep
import os

# counters
limit = 5
headsValue = 1
tailsValue = 1

def clearScreen():
    os.system('clear') if os.name == 'posix' else os.system('cls')


clearScreen()

while headsValue != limit or tailsValue != limit:
    
    print(f">> HEADS {headsValue} X {tailsValue} TAILS <<")

    toinCoss = random.randint(0,1)

    if toinCoss == 1:
        #print(f"Value: {toinCoss} --> Heads! - {headsValue}")
        headsValue+=1
    else:
        #print(f"Value: {toinCoss} --> Tails! - {tailsValue}")
        tailsValue+=1
    
    if headsValue > limit:
        print("Heads won!")
        break
    elif tailsValue > limit:
        print("Tails won!")
        break

    sleep(0.2)

    clearScreen()
    









