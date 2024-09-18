# Código para descobrir a quantidade letra A em uma palavra.

# ENTRADA PARA O USUÁRIO DIGITAR A PALAVRA QUE DESEJAR
palavra = input('Digite a palavra: ').lower()

# É CRIADO UMA VARIAVEL QUE IRA SERVIR COMO UM CONTADOR PARA A QUANTIDADE DE LETRAS A QUE FOR APARECER NA PALAVRA FORNECIDA PELO USUÁRIO
contagem_letra_a = 0

# VERIFICA SE EXISTE O VALOR 'a' NA PALAVRA FORNECIDA PELO USUÁRIO,
# CASO NÃO TIVER, O PROGRAMA SE ENCERRA
if 'a' in palavra:
    print(f'Existe a Letra A na palavra: {palavra.upper()}')

    lista_palavra = list(palavra) # A FUNÇÃO list() A PALAVRA EM UMA LISTA E TRANSFORMA CADA CARACTER EM UM INDICE DA LISTA

    for i in lista_palavra: # ESTRUTURO UM LAÇO DE REPETIÇÃO PARA PERCORRER A LISTA E VERIFICAR SE O VALOR DO INDICE ATUAL É EQUIVALENTE AO VALOR "a", 
        #SE FOR, ENTÃO É INCREMENTADO NO CONTADOR DE LETRA A
        if i == 'a':
            contagem_letra_a += 1
    print(f'Existe {contagem_letra_a} Letras A na palavra: {palavra.upper()}')
else:
    print(f'Letra A é inexistente na palavra: {palavra.upper()}')