
#funções
#São rotinas que são executadas comumente em um software

#função que mostra um título com linhas customizadas
def mostralinha(mensagem,tipo):
    print(tipo*20)
    print(mensagem)
    print(tipo*20)

mostralinha("Vamos estudar funções!","x")
mostralinha("Mas a linha mudou agora?","-")

#recebendo N numeros --> gera uma tupla
def somanumeros(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f'Os valores {numeros} somados são: {s}')

somanumeros(1, 2, 3, 4, 5)

#criacao de uma lista
valores = [9, 8, 7, 6, 5, 4] 

def dobranumeros(valores):
    pos = 0
    while pos < len(valores):
        valores[pos]*=2
        pos+=1

#utilizando a funcao recém-criada --> dobrando os valores de cada posição
dobranumeros(valores)

#imprimindo os valores finais
print(valores)



#testando o retorno da função com return
def somar(n1,n2):
    return n1+n2

a=10
b=12
print(f'O valor da soma é: {somar(a,b)}')