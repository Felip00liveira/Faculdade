#Exercício 1
soma = 0
for numero in range(1,11):
    if numero % 2 != 0:
        soma += numero
print(f'A soma dos números impares de 0 a 10 é: {soma}')