# Código para descobrir se X número se encontra sequência Fibonnaci.

# Entrada para que o usuário possa digitar o valor que queira verificar
numero = int(input('Qual número você deseja saber se pertence a sequência: '))

a, b = 0, 1 # Adição dos primeiros valores padrões do Fibonacci
sequencia_fibonacci = [a, b] # Lista onde irá ser armazenado os valores da sequência Fibonacci

# Loop que irá se repetir enquanto o valor que o usuário digitou não estiver na lista,
# ou até que o número da sequência seja maior que o valor fornecido.
while numero not in sequencia_fibonacci:      
    proximo_numero_fibonacci = a + b # A variável 'proximo_numero_fibonacci' recebe a soma dos dois valores anteriores a ele ('a' e 'b')

    sequencia_fibonacci.append(proximo_numero_fibonacci) # O valor da soma entre 'a' e 'b' é adicionado na lista

    a = b # A variável 'a' passa a receber o valor atual de 'b'
    b = proximo_numero_fibonacci # o valor de 'b' passa a ser o último número de sequência

    # Verifica se o último valor adicionado na lista é maior que o valor que o usuário digitou,
    # se for maior, o loop é interrompido, pois é entendido que o valor fornecido não se encontra na sequência
    if proximo_numero_fibonacci > numero: 
        break


# Caso o valor fornecido esteja na sequência, irá imprimir no terminal a sequência junto do valor fornecido, 
# caso contrário, irá imprimir somente a sequência, porém sem o valor fornecido pelo usuário.
if numero in sequencia_fibonacci:
    print(f'O valor {numero} faz parte da sequência fibonacci')
    print(f'{sequencia_fibonacci}', end=' ')
else:
    print(f'O valor {numero} não faz parte da sequência fibonacci')
    print(f'{sequencia_fibonacci}', end=' ')