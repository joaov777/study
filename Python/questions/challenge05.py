
#Crie um programa que leia nome e peso de N pessoas  e guarde tudo em uma lista.
#No final, deverá mostrar:
# - A quantidade de pessoas cadastradas
# - Uma listagem das pessoas mais pesadas
# - Uma listagem das pessoas mais leves

import sys

#lista vazia
pessoas = []
dados = []

nome_pesado = ""
peso_pesado = ""

nome_leve = ""
peso_leve = ""

while True:
    op = str(input('Deseja adicionar? [Ss/Nn]'))

    if op == 'N' or op == 'n':
        break

    elif op == 'S' or op == 's':
        nome = str(input(f'Insira o nome da pessoa {len(pessoas)}: '))
        peso = int(input(f'Insira a idade da pessoa: {len(pessoas)}: '))

        if nome_pesado == "":
            nome_pesado = nome
            peso_pesado = peso
            nome_leve = nome
            peso_leve = peso

        else:
            if peso > peso_pesado:
                nome_pesado = nome 
                peso_pesado = peso

            if peso < peso_leve:
                nome_leve = nome
                peso_leve = peso

        dados.append(nome)
        dados.append(peso)
        
        pessoas.append([nome,peso])

    else:
        print(f'Opcao inserida não é valida!')






print(f'Quantidade de pessoas inseridas: {len(pessoas)}') 

#definindo o maior peso



#print(f'O maior peso foi de {max([l[-1] for l in pessoas])}. Peso de ')

print('As pessoas inseridas foram: ')
for n in range(len(pessoas)):
    print('-'*5)
    print(f'<<< Pessoa {n} >>> \nNome: {pessoas[n][0]} \nPeso: {pessoas[n][1]}')
    print('-'*5)

print(f'A pessoas mais pesada é {nome_pesado} e seu peso é {peso_pesado}')
print(f'A pessoa mais leve é {nome_leve} e seu peso é {peso_leve}')























