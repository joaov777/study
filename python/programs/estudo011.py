
#Aprendendo dicionarios
# Tuplas são feitas com parênteses
# Listas são feitas por colchetes
# Dicionários são feitos por chaves

#lista
cores = ['vermelho','azul','preto','branco']

#atribuindo valores ao dicionário 
dados = {'nome':'Pedro','idade':25}

print(dados['nome'])
dados['sexo']='M'

print(dados['sexo'])

#excluindo o atributo idade
del dados['idade']

filme = {

    'titulo':'Star wars',
    'ano':'1977',
    'diretor':'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome':'Gustavo','sexo':'m','idade':22}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')

for k,v in pessoas.items():
    print(f'{k} = {v}')

#criando um dicinário dentre de uma lista
brasil = [ ]
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'Sao Paulo','sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)

#imprimindo Sao Paulo
print(brasil[1])

#imprimindo a sigla do dicionario para sao paulo
print(brasil[1]['sigla'])