
#MANIPULANDO CADEIAS DE TEXTO

frase='Curso em Python'
print(frase[9])
print(frase[9:15]) #imprimindo as posições de 9 ao 14
print(frase[9:12:2]) #imprime da posição 9 até a posição 21 pulando sempre 2 posições
print(frase[:5]) #imprime do início (0) até a posição 4.
print(frase[7:]) #imprime da posição 7 até o fim
print(frase[9::3]) #imprime da posição 9 até o fim pulando sempre 3 posições.

print(len(frase)) #retorna o tamanho da string
print(frase.count('o')) #conta quantas vezes a letra 'o' aparece

print(frase.count('o',0,13)) #Verifica a existencia do 'o' entre a posicao 0 e a posicao 13. 
print(frase.find('em')) #indica o inicio da posicão do padrão. Se for -1, então o padrão não existe.
print(frase.lower().find('python')) #Converte para minusculas e busca por 'Python'

print('Curso' in frase) #Retorna booleano caso o padrão seja encontrado

print(frase.replace('Python','Android')) #nao altera definitivamente
#frase = frase.replace('Python','Android') --> Com a atribuicao, efetivamente há a  mudança

print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #Somente o primeiro caractere em maiusculo
print(frase.title()) #faz o capitalize em todas as palavras.

print(frase.strip()) #retira caracteres inuteis no inicio e fim da string
print(frase.rstrip()) #retira somente os ultimos espaços inuteis (á direita)
print(frase.lstrip()) #retira somente os primeiros espaços inuteis (à esquerda)

print(frase.split()) #faz divisao considerando os espaços
dividido = frase.split() 
print(dividido[2]) #retorna a palavra Python


print('-'.join(frase)) #juncao baseado no padrao 

#Inserindo várias linhas ao mesmo tempo através de somente um print 
print("""Mas qual a diferença entre as formas mais diferentes?
Como assim poderíamos melhorar?
Eu até poderia lhe ajudar mais isso não nos torna diferentes.""")

print(frase.upper().count('O')) #transforma a string para letras maiusculas e logo procura pelas ocorrências da letra 'O'
print(len(frase.strip())) #tamanho da frase sem espaços inuteis









































