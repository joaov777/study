
# PROGRAMA QUE TESTA CONCEITOS GERAIS DO PYTHON JUNTAMENTE COM OS CONCEITOS PRIMITIVOS

n1=float(input('Numero 1: '))
n2=int(input('Numero 2: '))
n3=bool(input('Insira 1 ou 0: ')) #0 = true / 1 = false

nome='essa é uma string'

print(nome)

res=n1+n2

#print("O valor da soma entre os dois numeros e: "+str(res))
#print("A soma vale {}".format(n1+n2))
print("A soma vale: {}".format(res))
print("A soma vale:",res)
print("A soma entre {} e {} vale {}".format(n1,n2,res))

print(nome.isnumeric())
n = input('Digite algo: ')
print(n.isalpha())
print(n.isalnum())
print(n.islower())


