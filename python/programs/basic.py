



"""
age_allowed = 18
students_allowed = ["Mike", "Andrew", "Christine"]

def checkentrance(age):
    if int(age) >= age_allowed:
        print("Você pode entrar!")
    else:
        print("Você não pode entrar!")

age_insert = input("Insira a idade do aluno: ")

checkentrance(age_insert)


def check_operator(op,num1,num2):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("Invalid operator inserted!")


num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the second number: "))

check_operator(op,num1,num2)
"""

import sys

# Receives the command line parameter and uses function 
# check_age to process the information by returning a 
# message. 
#
# Python sys module provides access to any command-line
# arguments via the sys.argv. 
#
# sys.argv[0] ==> script name
# sys.argv[1] ==> script first command-line parameter


def check_age(age):
    if age < 18:
        print("Você não tem idade para entrar na festa!")
    elif age >=65:
        print("Você tem acompanhante?")
    else:
        print("Bem vindo(a)!")

check_age(int(sys.argv[1]))
"""


















