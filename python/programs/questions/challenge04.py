
#Crie um programa que leia N numeros do usuario e adicione em uma lista. Mas não adicione números já existentes. 
#No final, os números deverão ser mostrados em ordem crescente.

#lista vazia
numeros = []

while True:
    op = str(input('Deseja adicionar? [Ss/Nn]'))
    
    if op == 'S' or op == 's':
        #numeros.append(float(input(f'Insira o numero na posicao {len(numeros)}: ')))
        n = float(input(f'Insira o numero na posicao {len(numeros)}: '))

        if n in numeros:
            print(f'O numero {n} não pode ser adicionado!! Já existente!!')
        else:
            numeros.append(n)
            print(f'O numero {n} foi adicionado com sucesso!!')

    elif op == 'N' or op == 'n':
        break
    
    else:
        print('Insira uma opção válida!!!')
    

print(f'<<< {len(numeros)} números foram adicionados até o momento!! >>>')

#cópia da lista numeros para numeros2 (cópia sem relação)
numeros2 = numeros[:]

#reordernação dos números da lista numeros
numeros.sort()

#impressão dos números da lista números em ordem crescente e mantendo a relação com o seu índice original
for num in numeros:
    print(f'Numero {num} na posição {numeros2.index(num)}')


