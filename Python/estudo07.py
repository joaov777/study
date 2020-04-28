
# LOOPS

# printing Oi six times
for i in range(6):
    print("Oi")

#printing  2,3,4 and 5
for c in range(2,6):
    print(c)

#printing in reverse by -1
for a in range(6,0,-1):
    print(a)

#printing from 0 to 6 by 2 numbers -->0,2,4,6
for a in range(0,7,2):
    print(a)

print("="*15)

#usando while

c=1
while c < 10:
    print(c)
    c+=1

print("="*15)

#When chosen 0, it exits
n=1
while n != 0:
    n = int(input('Digite um valor: '))

#testing infinite loop
while True:
    numero=int(input("Insira um numero: "))

    if numero < 10:
        print("O numero e menor que 10!!")
    else:
        print("O numero é maior ou iguala 10!!")
        break

#testing fstrings > Pthon 3.6
teste="teste"
print(f'O texto é {teste}')

nome="Jose"
idade="15"
print(f'O usuario {nome} tem {idade} anos!!') #PYTHON 3
print('O usuario {} tem {} anos!!'.format(nome,idade)) #PYTHON 3
print('O usuario %s tem %s anos!!' % (nome, idade)) #PYTHON 2 - deprecated






