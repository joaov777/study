#Este é um programa de teste sobre o estudo da linguagem Python
#Este é um comentário adicional
#Removi alguns espaços
import os

s = False

while s == False:

    os.system('clear')

    print(">>> CALCULADORA <<<")
    print("(1) - Inserir os dois numeros")
    print("(2) - Somar")
    print("(3) - Subtrair")
    print("(4) - Multiplicar")
    print("(5) - Dividir")
    print("(6) - Sair")
    opcao = int(input("Opcao: "))

    if opcao == 1 :
        os.system('clear')
        print("# INSERCAO DE NUMEROS #")
        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))

    elif opcao == 2 :
        os.system('clear')
        print("# SOMAR #")
        print("O resultado da soma e: " +str(n1+n2))
        input("")
    
    elif opcao == 3 :
        os.system('clear')
        print("# SUBTRAIR #")
        print("O resultado da subtracao e: " +str(n1-n2))
        input("") 

    elif opcao == 4 :
        os.system('clear')
        print("# MULTIPLICAR #")
        print("O resultado da multiplicacao e: " +str(n1*n2))
        input("") 

    elif opcao == 5 :
        os.system('clear')
        print("# DIVIDIR #")
        print("O resultado da divisao e: " +str(n1/n2))
        input("") 
    
    else :
        os.system('clear')
        print("Sair do programa!")
        s = True


