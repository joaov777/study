#CONDIÇÕES

import random


idade=int(input('Qual a sua idade? '))
nome=str(input('Qual seu nome? '))

#comandos juntos à esquerda é certeza de ser executado
#comandos com identação possivelmente podem ser executados
if idade <= 3:
    print('Carro mais novo')
else:
    print('Carro mais velho')   

#condicao simplificada
print('Carro mais novo' if idade <=3 else 'Carro mais velho')

print('='*15)

if nome == 'Gustavo':
    print('Olá, Gustavo!!')
else:
    print('Bom dia, {}'.format(nome))

print('='*15)

n1=float(input("Primeira nota: "))
n2=float(input("Segunda nota: "))
media=(n1+n2)/2
print("Sua média foi: {}".format(media))
if media >= 6.0:
    print("Sua média foi boa. Parabéns!!")
else:
    print("Sua média não foi boa. Estude mais!!")

#Condição simplificada
print("Parabéns" if media  >= 6.0 else "Estude Mais!!")

print('='*15)

#Generating a random number between 0 and 10
rnumber=random.randrange(10)
rnumberplayer=int(input("Tente adivinhar um numero entre 0 e 10 escolhido pelo computador \n Insira um numero inteiro entre 0 e 10: "))

if rnumberplayer == rnumber:
    print("Você acertou!!!")
else:
    print("Você errou!!")

print("Numero escolhido pelo jogador: {}".format(rnumberplayer))
print("Numero escolhido pelo computador: {} ".format(rnumber))








