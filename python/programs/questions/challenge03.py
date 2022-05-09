
#Crie um programa que leia 5 numeros e salve-os em uma lista. Mostre o maior e o menor.

numeros = []

for n in range(0,5):
    numeros.append(float(input(f'Insira o numero {n}: ')))

print(f'O maior numero da lista é {max(numeros)} e está na posição {numeros.index(max(numeros))}')
print(f'O menor numero da lista é {min(numeros)} e está na posição {numeros.index(min(numeros))}')