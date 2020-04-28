#variáveis compostas (tuplas)

"""
As variáveis compostas podem ser:
- tuplas
- listas
- dicionários
"""

#tupla é uma variável que guarda N valores definidos
#tuplas são imutaveis
#tuplas somente são alteradas se o programa for parado e a tupla alterada
#tuplas são com ( )
#listas são com [ ]
#dicionários são com { }

paises = ('Brasil','Estados Unidos','Argentina') #tupla
paises2 = 'Croacia','Canada','Bolivia'


print(paises) #imprimindo todos os paises
print(paises2) #imprimindo todos os paises2

print(paises[1]) #imprimindo Estados Unidos
print(paises[-2]) #imprimindo Estados Unidos mas iniciando a contagem a partir do fim dos itens da tupla
print(paises2[2:]) #imprimindo do elemento 2 até o fim.
print(paises[-2:]) #imprimindo a partir do elemento -2 contando a partir do fim dos itens até o fim.

#maneira mais simples
for p in paises:
    print(f'O pais é: {p}')

#utilizando o tamanho do vetor de forma dinâmica
for p in range(0,len(paises)):
    print(f'O pais é: {paises[p]} na posição {p}')

for pos, p in enumerate(paises):
    print(f'Eu vou viajar para {paises} na posição {pos}')

#imprimindo em ordem alfabética
print(sorted(paises))

tupla01=(2,5,7)
tupla02=(7,8,4,12)
tupla03 = tupla01 + tupla02
print(tupla03)

#retornando o index do elemento de valor 8
print(tupla03.index(8))

print(max(tupla03)) #retorna o maior valor da tupla
print(min(tupla03)) #retorna o menor valor da tupla

pessoa=('Gustavo','39','Masculino','99.88')
print(pessoa)

#apagando a tupla
#um objeto tupla não suporta a deleção de itens específicos
del pessoa
