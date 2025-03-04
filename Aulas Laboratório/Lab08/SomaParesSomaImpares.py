soma_pares = 0
soma_impares = 0
valor_inicial = int(input('Digite um primeiro valor: '))
valor_final = int(input('Digite um segundo valor: '))
for numero in range(valor_inicial,valor_final +1):
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero
print(f'A soma dos números pares é: {soma_pares}')
print(f'A soma dos números impares é: {soma_impares}')
print('A soma dos número impares e pares é: ', soma_pares+soma_impares)