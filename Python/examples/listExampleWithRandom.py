

import random
import time


def choose_person(person_name):
    the_chosen = random.randrange(0,len(person_name))
    # total_items = len(person_name)
    # the_chosen = random.randint(0, total_items - 1)
    print(f"> CONGRATULATIONS!! {person_name[the_chosen]} will pay the bill!!")

    #another implementation below
    #for i in range(len(person_name)):
    #   print(random.choice(person_name))


people = []

#people = ['Marcos','Andre','Sandro','Ana','Celia','Talia','Celine','Danubia','Ellen','Lucia','Neila','Makelli','Andressa','Mara','George','Matheus','Carlos','Carol','Joana','Amelia']
#print(names_separated[random.randrange(0,len(names_separated))])


number_of_people = int(input("How many people on the table? "))

for i in range(0,number_of_people):
    people.append(input(f"Person {i}: "))

while True:
    choose_person(people)
    time.sleep(2)

