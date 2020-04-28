#aprendendo sobre listas
#listas sao feitas com []
#listas sao mutaveis

#definindo uma lista de paises sulamericanos
paises=['Brazil','Argentina','Bolivia','Colombia','Peru']
print(paises) #imprimindo antes de fazer qualquer alteracao

#comprovando que listas sao mutaveis
paises[2]='Paraguai'
print(paises)

#adicionando um item
paises.append('Uruguai')
print(paises)

#inserindo um novo item em uma posicao especifica
paises.insert(0,'Venezuela')
print(paises)

#del paises[3] #removendo a posicao 3
#paises.pop(3) #remove a posicao 3 
#paises.remove('Uruguai') #remove o item pelo conteudo
#paises.pop() #elimina o ultimo elemento automaticamente

#checando se um elemento existe na lista
if 'Uruguai' in paises:
    paises.remove('Uruguai')

#declarando lista com ranges
valores=list(range(4,11)) #criando de 4 a 10 --> 4 e elemento 0, 5 e elemento 1, etc...

valores=[8,9,5,6,3,4,1,8,7,5]
valores.sort() #reodernando os valores.
valores.sort(reverse=True) #reodernando de forma decrescente

#descobrindo o tamanho da lista
print(len(valores))
print(f'Essa lista tem {len(valores)} posicoes!!')

if 5 in valores:
    print('O numero foi encontrado!!')

for  v in valores:
    print(f'Valor {v}... ',end='')

#recebendo valores e inserindo na lista
for c in range(0,5):
    valores.append(int(input('Insira item: ')))

a = [2,3,4,7]
b = a #listas a e b são iguais agora

#mudou a posicao 2 para o valor 8
b[2] = 8 #as duas listas sao alteradas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Somente não mudaria as duas listas se fosse feita uma cópia entre as listas
#b = a[:]









