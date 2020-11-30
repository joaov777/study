
# APRENDENDO UM POUCO MAIS SOBRE OPERAÇÕES ARITMETICAS

import math
import os
import random
import emoji


n1=float(input('Primeiro numero: '))
n2=float(input('Segundo numero: '))
print('O resultado final é: {}'.format(n1+n2))

nome=input('Qual o seu nome? ')
print('Prazer em te conhecer {}'.format(nome), end=' ') #This is a way not to break the lines
print('Aprenderemos bastante!!')

# o \n faz a quebra da linha
print('Esta linha será quebrada bem aqui \n, pois essa é outra linha.')

#Calculando o antecessor e o sucessor 
print('O numero antecessor é {} e o sucessor é {}'.format((n1+n2)-1, (n1+n2)+1))

raiz = math.sqrt(n1+n2)
print("A raiz quadrada de {} é: {}".format((n1+n2),raiz))
print("A raiz quadrada de {} é: {:.2f}".format((n1+n2),math.sqrt(n1+n2))) #Resultado da raiz com duas casas decimais

#Gerando um numero aleatorio com o modulo random
print('O numero aleatorio gerado foi: {:.1f}'.format(random.random())) #Numero aleatorio impresso com uma casa decimal

#Printing an emoji based on the module 'emoji'. Module downloaded by pip install emoji
print(emoji.emojize("Olá, mundo :earth_americas:", use_aliases=True))

#Imprimindo o valor da soma final fazendo arredondamento
print(math.floor(n1+n2))

