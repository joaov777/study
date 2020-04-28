
# Crie um programa que receba N número do usuário e que pare de receber números quando o número 12341234 for inserido. Logo, ao final é preciso que a soma entre os número seja mostrada.

n = x = 0
while True:
    n=float(input("Insira um número: "))

    if n == 12341234:
        break
    x+=n
print("O valor total da soma: {}".format(x))
