import os

nome=input("Qual é o seu nome? ")
print("Bem-vindo ao clube, " +nome)

os.system('clear')

idade=input("Qual sua idade? ")
peso=input("Qual seu peso? ")

print("O usuário " + nome + " tem idade " +idade+ " e peso de " +peso)

dia=input("Insira o dia do seu aniversário: ")
mes=input("Insira o mes do seu aniversario: ")
ano=input("Insira o ano do seu aniversario: ")

print("A data do seu aniversário é: " + dia + "/" + mes + "/" + ano)


