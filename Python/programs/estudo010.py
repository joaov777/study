
dados = list()

dados.append('Joao')
dados.append('25')

print(dados[0])
print(dados[1])

pessoas = list()

#inseriu uma copia da lista dados como posicao na lista pessoas
pessoas.append(dados[:])

print(pessoas[0])

#lista composta já declarada logo abaixo
pessoas = [ ['Pedro',25],['Maria',19],['Joao',32] ]

#imprimindo o nome da primeira posicao da primeira lista
print(pessoas[0][0])

#imprimindo o segundo nome
print(pessoas[1][1])

#imprime tudo da posicao 1
print(pessoas[1])

